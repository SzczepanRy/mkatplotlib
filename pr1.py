import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#basic linechart



########################################

#resize the fraph

plt.figure(figsize=(5,3),dpi=100)# cdpi should be higher


x = [0,1,2,3,4]
y = [0,2,3,6,8]

#plt.plot(x,y , label="2x" ,color="red" , linewidth=5 , marker=".",markersize=12 )
#shortcut
plt.plot(x,y,"r.-",label="2x" )


#line tow 
#(min,max,step)
x2 = np.arange(0,4,0.5)
p = plt.plot(x2,x2**2,label="x^2")



plt.title("title")
plt.ylabel("ylabel")
plt.xlabel("xlabel")


#sets the space between marks
plt.xticks([0,1,2,3])
plt.yticks([0,2,4,6])

#to display the label 
plt.legend()

plt.savefig("./graphs/mygraph.png")#+ dpi=200

plt.show()

##########################################


#basic heatmap

# a = np.random.random((16, 16))
a = np.diag(range(15))

plt.imshow(a, cmap='hot', interpolation='nearest')

plt.show()

#############################################
#graph heatmap 

x = [0,1,2,3,4]
y = [0,2,6,6,8]


def make2D(x,y):
    arr=[]
    for i in range(y):
        row=[]
        for z in range(x):
            row.append(0)
        arr.append(row)
    return arr

arr = make2D(10 ,10)
print(arr)

for i in range(len(x)):
    if(x[i] == i ):
        arr[y[i] ][i] = y[i]     
    

print(arr)

plt.imshow(arr, cmap='hot',origin='lower', interpolation='nearest') # try origin image[::-1],
plt.show()

################################################

# Fixing random state for reproducibility
np.random.seed(19680801)

dt = 0.0005
t = np.arange(0.0, 20.5, dt) #set an array of inputs

s1 = np.sin(2 * np.pi * 100 * t)
s2 = 2 * np.sin(2 * np.pi * 100 * t)



# create a transient "chirp"
s2[t <= 10] = 0
s2[12 <= t] = 0

# add some noise into the mix
nse = 0.01 * np.random.random(size=len(t))



x = s1 + s2 + nse  # the signal
NFFT = 1024  # the length of the windowing segments
Fs = 1/dt  # the sampling frequency

# x = arr , NFFT = 1024 fs = 2000

fig, (ax1, ax2) = plt.subplots(nrows=2, sharex=True)
ax1.plot(t, x)
ax1.set_ylabel('Signal')


Pxx, freqs, bins, im = ax2.specgram(x, NFFT=NFFT, Fs=Fs) # t = x
# The `specgram` method returns 4 objects. They are:

# - Pxx: the periodogram

# - freqs: the frequency vector

# - bins: the centers of the time bins

# - im: the .image.AxesImage instance representing the data in the plot
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Frequency (Hz)')
ax2.set_xlim(0, 20)

plt.show()
