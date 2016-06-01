from __future__ import division
from numpy import *
from pylab import *
from matplotlib import pyplot




length = 1.0
g = 9.8
deltat = 0.04

theta1_=45
q1 = 0.1
force1 = 2
frequency1 = 2
theta1 = [theta1_*pi/180]
omega1 = [0]
t1 = [0]

while t1[-1] <= 100:
    omega1.append(omega1[-1] - (g/length)*theta1[-1]*deltat - q1*omega1[-1]*deltat + force1*sin(frequency1*t1[-1])*deltat)
    theta1.append(theta1[-1] + omega1[-1]*deltat)
    t1.append(t1[-1] + deltat)

theta_array1 = array(theta1)
t_array1 = array(t1)

theta2_=45
q2 = 0.5
force2 = 2
frequency2 = 2
theta2 = [theta2_*pi/180]
omega2 = [0]
t2 = [0]

while t2[-1] <= 100:
    omega2.append(omega2[-1] - (g/length)*theta2[-1]*deltat - q2*omega2[-1]*deltat + force2*sin(frequency2*t2[-1])*deltat)
    theta2.append(theta2[-1] + omega2[-1]*deltat)
    t2.append(t2[-1] + deltat)

theta_array2 = array(theta2)
t_array2 = array(t2)


theta3_=45
q3 = 1
force3 = 2
frequency3 = 2
theta3 = [theta3_*pi/180]
omega3 = [0]
t3 = [0]

while t3[-1] <= 100:
    omega3.append(omega3[-1] - (g/length)*theta3[-1]*deltat - q3*omega3[-1]*deltat + force3*sin(frequency3*t3[-1])*deltat)
    theta3.append(theta3[-1] + omega3[-1]*deltat)
    t3.append(t3[-1] + deltat)

theta_array3 = array(theta3)
t_array3 = array(t3)



matplotlib.pyplot.figure(figsize=(8,6))
matplotlib.pyplot.plot(t_array1,theta_array1,label="q=",color="blue",linewidth=2,linestyle='-')
matplotlib.pyplot.plot(t_array2,theta_array2,label="q=",color="red",linewidth=2,linestyle='-')
matplotlib.pyplot.plot(t_array3,theta_array3,label="q=",color="yellow",linewidth=2,linestyle='-')
matplotlib.pyplot.xlabel("t(s)")
matplotlib.pyplot.title("Force= ,Frequency=")
matplotlib.pyplot.ylabel("angle (radians)")
matplotlib.pyplot.xlim(0,100)
matplotlib.pyplot.ylim(-1,1)
matplotlib.pyplot.legend(loc='best')
matplotlib.pyplot.show()
       