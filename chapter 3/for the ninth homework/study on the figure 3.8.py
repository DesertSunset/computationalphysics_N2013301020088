from __future__ import division
from math import *
from pylab import *
from matplotlib import pyplot




length = 9.8
g = 9.8
deltat = 0.04

q1 = 0.5
force1 = 0
frequency1 = 2/3
theta1 = [0.2]
omega1 = [0]
t1 = [0]

while t1[-1] <= 200:
    if abs(theta1[-1])>=pi:
        theta1[-1]=-theta1[-1]
        omega1.append(omega1[-1] - (g/length)*numpy.sin(theta1[-1])*deltat - q1*omega1[-1]*deltat + force1*numpy.sin(frequency1*t1[-1])*deltat)
        theta1.append(theta1[-1] + (omega1[-1] )*deltat)
        t1.append(t1[-1] + deltat)
    else:
        omega1.append(omega1[-1] - (g/length)*numpy.sin(theta1[-1])*deltat - q1*omega1[-1]*deltat + force1*numpy.sin(frequency1*t1[-1])*deltat)
        theta1.append(theta1[-1] + (omega1[-1] )*deltat)
        t1.append(t1[-1] + deltat)

theta_array1 = array(theta1)
omega1_array1 = array(omega1)
t_array1 = array(t1)

q2 = 0.5
force2 = 0.5
frequency2 = 2/3
theta2 = [0.2]
omega2 = [0]
t2 = [0]

while t2[-1] <= 200:
    if abs(theta2[-1])>=pi:
        theta2[-1]=-theta2[-1]
        omega2.append(omega2[-1] - (g/length)*numpy.sin(theta2[-1])*deltat - q2*omega2[-1]*deltat + force2*numpy.sin(frequency2*t2[-1])*deltat)
        theta2.append(theta2[-1] + (omega2[-1] )*deltat)
        t2.append(t2[-1] + deltat)
    else:
        omega2.append(omega2[-1] - (g/length)*numpy.sin(theta2[-1])*deltat - q2*omega2[-1]*deltat + force2*numpy.sin(frequency2*t2[-1])*deltat)
        theta2.append(theta2[-1] + (omega2[-1] )*deltat)
        t2.append(t2[-1] + deltat)

theta_array2 = array(theta2)
omega2_array2 = array(omega2)
t_array2 = array(t2)


q3 = 0.5
force3 = 1.2
frequency3 = 2/3
theta3 = [0.2]
omega3 = [0]
t3 = [0]

while t3[-1] <= 200:
    if abs(theta3[-1])>=pi:
        theta3[-1]=-theta3[-1]
        omega3.append(omega3[-1] - (g/length)*numpy.sin(theta3[-1])*deltat - q3*omega3[-1]*deltat + force3*numpy.sin(frequency3*t3[-1])*deltat)
        theta3.append(theta3[-1] + (omega3[-1] )*deltat)
        t3.append(t3[-1] + deltat)
    else:
        omega3.append(omega3[-1] - (g/length)*numpy.sin(theta3[-1])*deltat - q3*omega3[-1]*deltat + force3*numpy.sin(frequency3*t3[-1])*deltat)
        theta3.append(theta3[-1] + (omega3[-1])*deltat)
        t3.append(t3[-1] + deltat)

theta_array3 = array(theta3)
omega3_array3 = array(omega3)
t_array3 = array(t3)



figure(figsize=(8,6))
scatter(theta_array1,omega1_array1,label="Force=0",color="blue",linewidth=0.01,linestyle='-')
scatter(theta_array2,omega2_array2,label="Force=0.5",color="red",linewidth=0.01,linestyle='-')
scatter(theta_array3,omega3_array3,label="Force=1.2",color="green",linewidth=0.01,linestyle='-')
xlabel("theta(radians)")
title("omega versus theta")
ylabel("omega (radians)")
xlim(-4,4)
ylim(-3,3)
grid(True)
legend(loc='best')
show()
       