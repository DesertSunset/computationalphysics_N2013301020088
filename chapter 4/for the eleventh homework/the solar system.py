import matplotlib.pyplot
import math

vy0=float(input('please input the initial velocity of the planet :'))


x1=[0]
y1=[0]
x2=[1]
y2=[0]
vx1=[0]
vy1=[0]
vx2=[0]
vy2=[vy0*math.pi]
t=[0]
dt=0.002
GM=4*math.pi*math.pi


while t[-1]<10:

    r=math.sqrt((x1[-1]-x2[-1])**2+(y1[-1]-y2[-1])**2)
    ox2=-GM*(x2[-1]-x1[-1])/(r**3)
    oy2=-GM*(y2[-1]-y1[-1])/(r**3)
    vx2.append(vx2[-1]+ox2*dt)
    vy2.append(vy2[-1]+oy2*dt)
    x2.append(x2[-1]+vx2[-1]*dt) 
    y2.append(y2[-1]+vy2[-1]*dt)
    t.append(t[-1]+dt)
    
fig=matplotlib.pyplot.figure(figsize=[8,8])
matplotlib.pyplot.scatter(x1,y1,label='sun')
matplotlib.pyplot.plot(x2,y2,label='planet',color='red')
matplotlib.pyplot.legend(loc='upper right')

matplotlib.pyplot.xlabel('x(AU)')
matplotlib.pyplot.ylabel('y(AU)')
matplotlib.pyplot.title('v0=3')

matplotlib.pyplot.show()