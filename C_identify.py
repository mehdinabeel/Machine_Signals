import numpy as np
import time
from scipy.stats import kurtosis
from scipy.stats import sem
SECS = 1 #No. of seconds change to detect


def audLevel():
    aud = (np.genfromtxt(str('aud.txt'), delimiter=",",dtype=float,usecols=1))
    varin = (np.genfromtxt(str('aud.txt'), delimiter=",",dtype=float,usecols=2))
    level = (np.average(aud[-30:]))
    varins = (np.average(aud[-30:]))
    return level,varins #2.5 seconds

# Get Frequencies

def specgram():
    try:
        arr2D = (np.genfromtxt(str('aud_period.txt'), delimiter=",",dtype=float))
        weights = (arr2D.sum(axis=1))
        sort = np.sort(weights)
        harmonics = (sort[-6:])
        index = []
        for i in range(weights.size):
            for j in range(harmonics.size):
                if (weights[i]==harmonics[j]):
                    index.append(i)
        Freq = (np.genfromtxt('aud_freq.txt',dtype=float))
        C = []
        for i in range(6):
            try:
                j = index[i]
                A = np.round_(Freq[j],decimals=0)
                #B = np.round_(weights[j],decimals=1)
                C.append(int(A))
            except IndexError:
                pass
        return C
    except ValueError:
        pass

#Take vibration and other data etc
def Data():
    try:
        f2name = 'realtime.txt'
        Vx = (np.genfromtxt(str(f2name), delimiter=",",dtype=float,usecols=1))
        Vy = (np.genfromtxt(str(f2name), delimiter=",",dtype=float,usecols=2))
        Vz = (np.genfromtxt(str(f2name), delimiter=",",dtype=float,usecols=3))
        Mx = (np.genfromtxt(str(f2name), delimiter=",",dtype=float,usecols=4))
        My = (np.genfromtxt(str(f2name), delimiter=",",dtype=float,usecols=5))
        Mz = (np.genfromtxt(str(f2name), delimiter=",",dtype=float,usecols=6))
        L = ((np.genfromtxt(str(f2name), delimiter=",",dtype=float,usecols=7)))
        Mmag = (np.sqrt(Mx[-18:]**2+My[-18:]**2+Mz[-18:]**2))
        Vmag = (np.sqrt(Vx[-18:]**2+Vy[-18:]**2+Vz[-18:]**2))
        return Vmag,Mmag,L
    except ValueError:
        return 1,1,1
try:
    while True:
        Vmag,Mmag,L = Data()
        list = specgram()
        level,varins = audLevel()

        #CHECK AND VALIDATE



        #NC = [345,560,3500-3000,2153]
        #PRINTER = [474,1600-1750]
        magPar = (np.average(Mmag))
        vibPar = (sem(Vmag))

        Machine ="Machine"
        state ="Not Sensing"
        if (magPar>15 and magPar<50 and vibPar<0.02 ):
            Machine = "Pocket NC Machine"
            #if (kurtosis(Mmag[-SECS*20:])<0 and np.amax(Mmag[-SECS*20:])<30 and level < 100):
            #    state = 'OFF'
            if (level<100 ):
                state = 'Idle'
            if(level>100):
                state = 'Work in progress'
            else:
                state = " "
        if (magPar>100 and magPar<160 ):
            Machine = "3D Printer"
            #if (kurtosis(Mmag[-SECS*20:])<0 and np.amax(Mmag[-SECS*20:])<30 and level < 100):
            #    state = 'OFF'
            if(level<200):
                state = 'Idle'
            if(level>200):
                state = 'Work in progress'

        print(Machine +" : " + state + ", Dominant Freqs :-")
        print(list)
        print('\n')

        time.sleep(2)

except KeyboardInterrupt:
        pass
