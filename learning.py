import numpy as np
import matplotlib.pyplot as plt
import datetime
import matplotlib.animation as animation
from scipy import stats


def main():

    main = plt.figure(2)
    main.suptitle('Main title')
    Vplot = main.add_subplot(411)
    Mplot = main.add_subplot(412)
    Aplot = main.add_subplot(413)
    Lplot = main.add_subplot(414)

    timestamp = 1530117662.670
    value = datetime.datetime.fromtimestamp(timestamp)
    time_date= (value.strftime('%Y-%m-%d %H:%M:%S'))

    def animate(i):
        audio = []
        others = []
        Tstamp1 =[]

        f1name = "aud.txt"
        aud = (np.genfromtxt(str(f1name), delimiter=",",dtype=float,usecols=1))

        with open('measure.txt','r') as f:
            for line in f:
                line = line.replace("[", "")
                line = line.replace("]", "")
                line = line.replace("\n", "")
                line = line.replace("Accelerometer:", "")
                line = line.replace("Magnetic field:", "")
                line = line.replace("Light:", "")
                line = line.replace('"', "")
                line = line.replace(';', ",")
                others.append(line)
            f.close()

        r = open('realtime.txt','w')
        for lines in others:
            r.write('%s \n'%lines)
        r.close()
        

        f2name = "realtime.txt"
        Tstamp2 = (np.genfromtxt(str(f2name), delimiter=",",dtype=float,usecols=0))
        Vx = (np.genfromtxt(str(f2name), delimiter=",",dtype=float,usecols=1))
        Vy = (np.genfromtxt(str(f2name), delimiter=",",dtype=float,usecols=2))
        Vz = (np.genfromtxt(str(f2name), delimiter=",",dtype=float,usecols=3))
        Vmag = np.sqrt(Vx**2+Vy**2+Vz**2)
        Mx = (np.genfromtxt(str(f2name), delimiter=",",dtype=float,usecols=4))
        My = (np.genfromtxt(str(f2name), delimiter=",",dtype=float,usecols=5))
        Mz = (np.genfromtxt(str(f2name), delimiter=",",dtype=float,usecols=6))
        light = (np.genfromtxt(str(f2name), delimiter=",",dtype=float,usecols=7))
        Mmag = np.sqrt(Mx**2+My**2+Mz**2)

        #stats here



        Vplot.clear()
        Mplot.clear()
        Aplot.clear()
        Lplot.clear()
        test = np.mean(aud[-50])
        if test>200:
            x="microwave ON"
        else:
            x="waiting"
        main.suptitle("hello")
        Vplot.plot(Vmag[-300:], 'b')
        Mplot.plot(Mmag[-300:], 'r')
        Aplot.plot(aud[-480:], 'g')
        Lplot.plot(light[-300:], 'k')


    ani = animation.FuncAnimation(main, animate, interval=50)
    plt.show(2)
main()
