"""Syed Nabeel Mehdi"""
############### Import Libraries ###############
from matplotlib.mlab import window_hanning,specgram
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


############### Import Modules ###############
import mic_read

############### Constants ###############
SAMPLES_PER_FRAME = 10 #Number of mic reads concatenated within a single window
nfft = 1024 #NFFT value for spectrogram
overlap = 512 #overlap value for spectrogram
rate = mic_read.RATE #sampling rate

############### Functions ###############
"""
get_sample:
gets the audio data from the microphone
inputs: audio stream and PyAudio object
outputs: int16 array
"""
def get_sample(stream,pa):
    data = mic_read.get_data(stream,pa)
    return data

"""
get_specgram:
takes the FFT to create a spectrogram of the given audio signal
input: audio signal, sampling rate
output: 2D Spectrogram Array, Frequency Array, Bin Array
see matplotlib.mlab.specgram documentation for help
"""
def get_specgram(signal,rate):
    arr2D,freqs,bins = specgram(signal,window=window_hanning,
                                Fs = rate,NFFT=nfft,noverlap=overlap, mode = 'magnitude')
    return arr2D,freqs,bins

"""
update_fig:
updates the image, just adds on samples at the start until the maximum size is
reached, at which point it 'scrolls' horizontally by determining how much of the
data needs to stay, shifting it left, and appending the new data.
inputs: iteration number
outputs: updated image
"""
def update_fig(n):
    data = get_sample(stream,pa)
    arr2D,freqs,bins = get_specgram(data,rate)
    im_data = im.get_array()
    if n < SAMPLES_PER_FRAME:
        im_data = np.hstack((im_data,arr2D))
        im.set_array(im_data)
    else:
        keep_block = arr2D.shape[1]*(SAMPLES_PER_FRAME - 1)
        im_data = np.delete(im_data,np.s_[:-keep_block],1)
        im_data = np.hstack((im_data,arr2D))
        im.set_array(im_data)
        #f = open('aud_period.txt',"a")
        np.savetxt("aud_period.txt", arr2D, delimiter=',',fmt="%.2f")
        """weights = (arr2D.sum(axis=1))
        sort = np.sort(weights)
        harmonics = (sort[-6:])
        index = []
        for i in range(weights.size):
            for j in range(harmonics.size):
                if (weights[i]==harmonics[j]):
                    index.append(i)
        Freq = (np.genfromtxt('aud_freq.txt',dtype=float,usecols=0))
        C = 0
        for i in range(6):
            j = index[i]
            A = np.round_(Freq[j],decimals=0)
            B = np.round_(weights[j],decimals=1)
            #print(type(A.astype(int)))
            Trimmer = [3402,3187,3203,2972,3445,3531]
            #print(level,varin)
            if A in Trimmer and varin > 500000 :
                C =C + 1
            if C==2:
                print("Trimmer")
            else:
                print(12)"""

                #(np.round_(freqs[np.argmax(np.sum(arr2D,axis =1))], decimals = 1))
    return im,

############### Initialize Plot ###############
fig = plt.figure()
"""
Launch the stream and the original spectrogram
"""
stream,pa = mic_read.open_mic()
data = get_sample(stream,pa)
arr2D,freqs,bins = get_specgram(data,rate)

"""
Setup the plot paramters
"""
extent = (bins[0],bins[-1]*SAMPLES_PER_FRAME,freqs[-1],freqs[0])
plt.subplot()
im = plt.imshow(arr2D,aspect='auto',extent = extent,interpolation="spline36",cmap = plt.cm.gist_heat, )
plt.xlabel('Time (s)')
plt.axis([0,1.7,7500,00])
plt.ylabel('Frequency (Hz)')
plt.title('Real Time Spectogram')
plt.gca().invert_yaxis()
#plt.colorbar() #enable if you want to display a color bar

############### Animate ###############
anim = animation.FuncAnimation(fig,update_fig,blit = False,
                               interval=50)

try:
    plt.show()
except:
    print("Plot Closed")

############### Terminate ###############
stream.stop_stream()
stream.close()
pa.terminate()
print("Program Terminated")
