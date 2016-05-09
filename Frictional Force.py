from pylab import *
import numpy
import matplotlib
import matplotlib.pylab as plt

v=[]
a=0
b=0

v0=float(input('please input the inital velocity:'))
v.append(v0)
a=(float(input('please input the a constant for an applied force:')))
b=(float(input('please input the b constant for friction:')))
time=(float(input('please input the total time:')))
n=(float(input('please input the time step:')))


t=numpy.linspace(0,int(time),int(n))

for i in range(999):
    v.append(v[i]+(a-b*v[i])*t[1])
    

v_a = a/b-(a-b*v0)*(numpy.exp(-b*t))/b

d=abs(v_a-v)/v_a*100

fig, ax1 = matplotlib.pyplot.subplots()
ax2 = ax1.twinx()
ax1.plot(t,v,label="Euler method",color="blue",linewidth=3,linestyle='--')
ax1.plot(t,v_a,label="analytic method",color="red",linewidth=3,linestyle=':')
ax2.plot(t,d,label="error",color="green",linewidth=3,linestyle=':')
ax1.set_xlabel("Time(t)")
ax1.set_ylabel("Velocity")
ax2.set_ylabel('error(%)')
title("Frictional Force")
ax1.legend(loc=1)
ax2.legend(loc=5)
plt.show()