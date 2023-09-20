#first if we dont have the mathplotlib in the system, then we have to install it using the commamd pip install mathplotlib
#after that we can start coding
from matplotlib import pyplot as plt
x=[1,2,3,4,5,6,7,1000,700000]
y=[300,599,600,1000,10000,56000,78,39999,456]
plt.plot(x,y)
plt.xlabel("rate of interest")
plt.ylabel("deduction")

plt.show()
