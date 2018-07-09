import pyaudio
import numpy as np
import time


TIME = 600
CHUNK = 1024
RATE = 44100

p=pyaudio.PyAudio()

def Fxec():
    for i in range(int(TIME*44100/1024)): #go for a few seconds
        stream=p.open(format=pyaudio.paInt16,channels=2,rate=RATE,input=True,frames_per_buffer=CHUNK)
        t = (round(time.time()*1000))
        data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
        peak=np.average(np.abs(data))*2
        bars="#"*int(500*peak/2**16)
        varin =np.round((np.var(data)))
        f= open("aud.txt","a")
        f.write("%04d,%05d,%05d"%(t,peak,varin)+"\n")
        f.close()
        stream.stop_stream()
        stream.close()
        print (int (peak))
Fxec()
