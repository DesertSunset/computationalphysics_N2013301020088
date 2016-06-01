from __future__ import division
from pylab import *


def z(r):
    x=[1]
    y=[0]
    z=[0]
    dxdt=[0]
    dydt=[0]
    dzdt=[0]
    t=[0]
    dt=0.001
    sigma=10
    b=8/3
    x0=[]
    y0=[]
    z01=[]
    z02=[]
    for i in range(499999):
        dxdt.append(sigma*(y[-1]-x[-1]))
        dydt.append(-x[-1]*z[-1]+r*x[-1]-y[-1])
        dzdt.append(x[-1]*y[-1]-b*z[-1])
        x.append(x[-1]+dxdt[-1]*dt)
        y.append(y[-1]+dydt[-1]*dt)
        z.append(z[-1]+dzdt[-1]*dt)
        t.append(t[-1]+dt)
        if t[-1]>30:
            if abs(x[-1])<0.01:
                y0.append(y[-1])
                z02.append(z[-1])
            if abs(y[-1])<0.01:
                x0.append(x[-1])
                z01.append(z[-1])
    return x0,y0,z01,z02

subplot(1,2,2)
scatter(z(25)[0],z(25)[2],s=0.1,label="r=25",color="blue",linewidth=2,linestyle='-')
xlabel("x")
title("z versus x when y=0")
ylabel("z")
grid(True)
legend(loc='best') 


subplot(1,2,1)
scatter(z(25)[1],z(25)[3],s=0.1,label="r=25",color="blue",linewidth=2,linestyle='-')
xlabel("y")
title("phase space plot: z versus y when x=0")
ylabel("z")
grid(True)
legend(loc='best') 
