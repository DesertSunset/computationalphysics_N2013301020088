from __future__ import division
from math import *
from pylab import *
from matplotlib import pyplot




length = 9.8
g = 9.8
deltat = 0.04

theta1_=11.46
q1 = 0.5
force1 = 1.2
frequency1 = 2/3
theta1 = [theta1_*pi/180]
omega1 = [0]
t1 = [0]
omega39=[0]
omega3124=[0]
omega3128=[0]

while t1[-1] <= 5000:
    if abs(theta1[-1])>=pi:
        theta1[-1]=-theta1[-1]
        omega1.append(omega1[-1] - (g/length)*numpy.sin(theta1[-1])*deltat - q1*omega1[-1]*deltat + force1*numpy.sin(frequency1*t1[-1])*deltat)
        theta1.append(theta1[-1] + (omega1[-1] - (g/length)*numpy.sin(theta1[-1])*deltat - q1*omega1[-1]*deltat + force1*numpy.sin(frequency1*t1[-1])*deltat)*deltat)
        t1.append(t1[-1] + deltat)
        if t1[-1]%(2*pi/frequency1)<=0.04:
            omega39.append(omega1[-1])
        else:
            omega39.append(None)
        if (t1[-1]-(3*pi)/4)%(3*pi)<=0.04:
            omega3124.append(omega1[-1])    
        else:
            omega3124.append(None)    
        if (t1[-1]-(3*pi)/8)%(3*pi)<=0.04:
            omega3128.append(omega1[-1]) 
        else:
            omega3128.append(None)            

    else:
        omega1.append(omega1[-1] - (g/length)*numpy.sin(theta1[-1])*deltat - q1*omega1[-1]*deltat + force1*numpy.sin(frequency1*t1[-1])*deltat)
        theta1.append(theta1[-1] + (omega1[-1] - (g/length)*numpy.sin(theta1[-1])*deltat - q1*omega1[-1]*deltat + force1*numpy.sin(frequency1*t1[-1])*deltat)*deltat)
        t1.append(t1[-1] + deltat)
        if t1[-1]%(2*pi/frequency1)<=0.04:
            omega39.append(omega1[-1])
        else:
            omega39.append(None)
        if (t1[-1]-(3*pi)/4)%(3*pi)<=0.04:
            omega3124.append(omega1[-1])    
        else:
            omega3124.append(None)    
        if (t1[-1]-(3*pi)/8)%(3*pi)<=0.04:
            omega3128.append(omega1[-1]) 
        else:
            omega3128.append(None)            



theta_array1 = array(theta1)
omega1_array1 = array(omega1)
omega39_array1 = array(omega39)
omega3124_array1 = array(omega3124)
omega3128_array1 = array(omega3128)
t_array1 = array(t1)




matplotlib.pyplot.figure(figsize=(8,6))
matplotlib.pyplot.scatter(theta_array1,omega39_array1 ,label="figure3.9",color="blue",linewidth=1,linestyle='-')
matplotlib.pyplot.scatter(theta_array1,omega3124_array1,label="excise3.12 with pi/2 force",color="red",linewidth=1,linestyle='-')
matplotlib.pyplot.scatter(theta_array1,omega3128_array1,label="excise3.12 with pi/4 force",color="green",linewidth=1,linestyle='-')
matplotlib.pyplot.xlabel("theta(radians)")
matplotlib.pyplot.ylabel("omega(radians)")
matplotlib.pyplot.title("angular velocity versus angle when Force=1.2")
matplotlib.pyplot.xlim(-3.5,3.5)
matplotlib.pyplot.ylim(-2,3.5)
matplotlib.pyplot.grid(True)
matplotlib.pyplot.legend(loc='best')
matplotlib.pyplot.show()
    

       