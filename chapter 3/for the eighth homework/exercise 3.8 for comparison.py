from __future__ import division
from numpy import *
from pylab import *
from matplotlib import pyplot




length = 1.0
g = 9.8
deltat = 0.04

theta1_=15
theta1 = [theta1_*pi/180]
omega1 = [0]
t1 = [0]

while t1[-1] <= 10:
    omega1.append(omega1[-1] - (g/length)*sin(theta1[-1])*deltat)
    theta1.append(theta1[-1] + omega1[-1]*deltat)
    t1.append(t1[-1] + deltat)

theta_array1 = array(theta1)
t_array1 = array(t1)

theta2_=45
theta2 = [theta2_*pi/180]
omega2 = [0]
t2 = [0]

while t2[-1] <= 10:
    omega2.append(omega2[-1] - (g/length)*sin(theta2[-1])*deltat )
    theta2.append(theta2[-1] + omega2[-1]*deltat)
    t2.append(t2[-1] + deltat)

theta_array2 = array(theta2)
t_array2 = array(t2)


theta3_=90
theta3 = [theta3_*pi/180]
omega3 = [0]
t3 = [0]

while t3[-1] <= 10:
    omega3.append(omega3[-1] - (g/length)*sin(theta3[-1])*deltat )
    theta3.append(theta3[-1] + omega3[-1]*deltat)
    t3.append(t3[-1] + deltat)

theta_array3 = array(theta3)
t_array3 = array(t3)



matplotlib.pyplot.figure(figsize=(8,6))
matplotlib.pyplot.plot(t_array1,theta_array1,label="theta=",color="blue",linewidth=1,linestyle='-')
matplotlib.pyplot.plot(t_array2,theta_array2,label="theta=",color="red",linewidth=1,linestyle='-')
matplotlib.pyplot.plot(t_array3,theta_array3,label="theta=",color="green",linewidth=1,linestyle='-')
matplotlib.pyplot.xlabel("t(s)")
matplotlib.pyplot.title("nonlinear pendulum")
matplotlib.pyplot.ylabel("angle (radians)")
matplotlib.pyplot.xlim(0,10)
matplotlib.pyplot.ylim(-2,2)
matplotlib.pyplot.legend(loc='best')
matplotlib.pyplot.show()
       