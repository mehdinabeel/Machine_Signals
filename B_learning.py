import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def main():

    main = plt.figure(2)
    main.suptitle('Main title')
    Vplot = main.add_subplot(411)
    Mplot = main.add_subplot(412)
    Aplot = main.add_subplot(413)
    Lplot = main.add_subplot(414)


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
        #Vplot.set_title("Vibrations in m/s**2",{'fontsize':8})
        Mplot.clear()
        #Mplot.set_title("Magnetic flux in µT",{'fontsize':8})
        Aplot.clear()
        #Mplot.set_title("Amplitude of sound",{'fontsize':8})
        Lplot.clear()
        #Lplot.set_title("Light in flux",{'fontsize':8})
        test = np.mean(aud[-50])
        if test>200:
            x="microwave ON"
        else:
            x="waiting"
        main.suptitle("DIME LAB : Machine Identification System",fontsize = 9,y=1)
        Vplot.plot(Vmag[-250:], 'r')
        Mplot.plot(Mmag[-250:], 'b')
        Aplot.plot(aud[-520:], 'g')
        Lplot.plot(light[-250:], 'w')
        Lplot.set_xticklabels([])
        Vplot.set_facecolor('black')
        Vplot.axes.get_xaxis().set_ticklabels([])
        Mplot.set_facecolor('black')
        Mplot.axes.get_xaxis().set_ticklabels([])
        Aplot.set_facecolor('black')
        Aplot.axes.get_xaxis().set_ticklabels([])
        Lplot.set_facecolor('black')
        Lplot.set_title('Light (lux)', fontsize = 8)
        Vplot.set_title('Vibrations (m/s**2)', fontsize = 8)
        Aplot.set_title('Sound Amplitude', fontsize = 8)
        Mplot.set_title('Magnetic Flux (µT)', fontsize = 8  )
        plt.tight_layout()
        ind = np.arange(5)



    ani = animation.FuncAnimation(main, animate, interval=50)
    plt.show(2)
main()
