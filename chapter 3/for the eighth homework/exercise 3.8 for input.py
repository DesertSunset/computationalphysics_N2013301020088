from __future__ import division
from numpy import *
from pylab import *


theta_=float(input('please input the initial theta :'))
theta = [theta_*pi/180]
omega = [0]

t = [0]
length = 1.0
g = 9.8
deltat = 0.04


while t[-1] <= 10:
    omega.append(omega[-1] - (g/length)*sin(theta[-1])*deltat)
    theta.append(theta[-1] + omega[-1]*deltat)
    t.append(t[-1] + deltat)

theta_array = array(theta)
t_array = array(t)

plot(t_array,theta_array)

title('damped pendulum with driving force')
xlabel('time (s)')
ylabel('angle (radians)')


xlim(0,10)
ylim(-1,1)

grid(True)

show()