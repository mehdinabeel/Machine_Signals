from tkinter import *
import numpy as np

TRAIN = 74 #training data
def main():
    # Audio level/volume of last few seconds
    def audLevel():
        aud = (np.genfromtxt(str('aud.txt'), delimiter=",",dtype=float,usecols=1))
        varin = (np.genfromtxt(str('aud.txt'), delimiter=",",dtype=float,usecols=2))
        level = int(np.average(aud[-120:]))
        return level,varin[-120:]

    # Get Frequencies
    def specgram():
        arr2D = (np.genfromtxt(str('aud_period.txt'), delimiter=",",dtype=float))
        weights = (arr2D.sum(axis=1))
        sort = np.sort(weights)
        harmonics = (sort[-6:])
        index = []
        for i in range(weights.size):
            for j in range(harmonics.size):
                if (weights[i]==harmonics[j]):
                    index.append(i)
        Freq = (np.genfromtxt('aud_freq.txt',dtype=float,usecols=0))
        C = []
        for i in range(6):
            j = index[i]
            A = np.round_(Freq[j],decimals=0)
            #B = np.round_(weights[j],decimals=1)
            C.append(int(A))
        return C
    level,varin = audLevel()
    #Take vibration and other data etc
    def Data():
        f2name = 'realtime.txt'
        Vx = (np.genfromtxt(str(f2name), delimiter=",",dtype=float,usecols=1))
        Vy = (np.genfromtxt(str(f2name), delimiter=",",dtype=float,usecols=2))
        Vz = (np.genfromtxt(str(f2name), delimiter=",",dtype=float,usecols=3))
        Vmag = (np.sqrt(Vx**2+Vy**2+Vz**2))
        Mx = (np.genfromtxt(str(f2name), delimiter=",",dtype=float,usecols=4))
        My = (np.genfromtxt(str(f2name), delimiter=",",dtype=float,usecols=5))
        Mz = (np.genfromtxt(str(f2name), delimiter=",",dtype=float,usecols=6))
        L = ((np.genfromtxt(str(f2name), delimiter=",",dtype=float,usecols=7)))
        Mmag = (np.sqrt(Mx**2+My**2+Mz**2))
        return Vmag,Mmag,L


    Vmag,Mmag,L = Data()




    window = Tk()
    window.title("DIME Lab : Machine Identification System")
    window.geometry('1200x200')

    lbl = Label(window, text= "  "*30)
    lbl.grid(column=0, row=0)
    lbl.config(font=("Calibri", 22))

    def clicked():
        window.destroy()
        main()
    btn = Button(window, text="Identify", command=clicked)
    btn.place(anchor="c")
    btn.grid(column=1, row=0)

    ryt = Label(window, text= "  "*4)
    ryt.grid(column=2, row=0)
    ryt.config(font=("Calibri", 22))

    Result = Label(window, text="RESULT_VAR")
    Result.grid(column=1, row=1)
    Result.config(font=("Calibri", 22))

    FR = Label(window, text= ("6 Dominant Freqs. in Hz:", specgram()))
    FR.grid(column=1, row=3)
    FR.config(font=("Calibri", 14))

    M = Label(window, text= ("Magnetic Flux in µ :", int(np.average(Mmag[-TRAIN:]))))
    M.grid(column=1, row=4)
    M.config(font=("Calibri", 14))

    V = Label(window, text= ("Vibration in m/s**2 :", int(np.average(Vmag[-TRAIN:]))))
    V.grid(column=1, row=5)
    V.config(font=("Calibri", 14))

    A = Label(window, text= ("Amplitude  of sound :", level))
    A.grid(column=1, row=6)
    A.config(font=("Calibri", 14))

    Va = Label(window, text= ("Variance in A signal :", int(np.average(varin))))
    Va.grid(column=1, row=7)
    Va.config(font=("Calibri", 14))

    s = Label(window, text= (" "))
    s.grid(column=1, row=8)
    s.config(font=("Calibri", 50))
    def check():
        TrimFreq = [3531,2455,2498,2929,3316,3273,3402,1637,3187,3445,1421]
        TMag = 72
        TVib = 10
        TAmp = 635
        TVar = 200000


    window.mainloop()
main()
