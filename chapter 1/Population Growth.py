from pylab import *
import numpy
import matplotlib
import matplotlib.pylab as plt

N=[]
a=0
b=0

N0=float(input('please input the inital population:'))
N.append(N0)
a=(float(input('please input the a constant for the birth:')))
b=(float(input('please input the b constant for deaths:')))
time=(float(input('please input the total time:')))
n=(float(input('please input the time step:')))


t=numpy.linspace(0,int(time),int(n))

for i in range(999):
    N.append(N[i]+(a*N[i]-b*N[i]*N[i])*t[1])
    
m=numpy.exp(a*t)

N_a= (a*numpy.exp(a*t))/(a/N0-b+b*numpy.exp(a*t)) 

d=abs(N_a-N)/N_a*100

fig, ax1 = matplotlib.pyplot.subplots()
ax2 = ax1.twinx()
ax1.plot(t,N,label="Euler method",color="blue",linewidth=3,linestyle='--')
ax1.plot(t,N_a,label="analytic method",color="red",linewidth=3,linestyle=':')
ax2.plot(t,d,label="error",color="green",linewidth=3,linestyle=':')
ax1.set_xlabel("Time(t)")
ax1.set_ylabel("Number")
ax2.set_ylabel('error(%)')
title("Population Growth")
ax1.legend(loc=1)
ax2.legend(loc=5)
plt.show()