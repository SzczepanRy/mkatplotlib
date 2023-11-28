import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#basic linechart



########################################

#resize the fraph

plt.figure(figsize=(5,3),dpi=100)# cdpi should be higher


x = [0,1,2,3,4]
y = [0,2,4,6,8]

#plt.plot(x,y , label="2x" ,color="red" , linewidth=5 , marker=".",markersize=12 )
#shortcut
plt.plot(x,y,"r.-",label="2x" )


#line tow 
#(min,max,step)
x2 = np.arange(0,4,0.5)
plt.plot(x2,x2**2,label="x^2")



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