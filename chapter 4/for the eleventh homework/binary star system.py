import matplotlib.pyplot
import math


k=float(input('please input the radio of mass between the sun and the planet (M/m):'))


x1=[0]
y1=[0]
x2=[1]
y2=[0]
vx1=[0]
vy1=[math.sqrt(1/(1+k))*math.pi]
vx2=[0]
vy2=[-math.sqrt((k**2)/(1+k))*math.pi]
t=[0]
dt=0.002
Gm=4*math.pi*math.pi
GM=k*Gm


while t[-1]<1:

    r=math.sqrt((x1[-1]-x2[-1])**2+(y1[-1]-y2[-1])**2)
    ox1=-Gm*(x1[-1]-x2[-1])/(r**3)
    ox2=-GM*(x2[-1]-x1[-1])/(r**3)
    oy1=-Gm*(y1[-1]-y2[-1])/(r**3)
    oy2=-GM*(y2[-1]-y1[-1])/(r**3)
    vx1.append(vx1[-1]+ox1*dt)
    vx2.append(vx2[-1]+ox2*dt)
    vy1.append(vy1[-1]+oy1*dt)
    vy2.append(vy2[-1]+oy2*dt)
    x1.append(x1[-1]+vx1[-1]*dt)
    x2.append(x2[-1]+vx2[-1]*dt) 
    y1.append(y1[-1]+vy1[-1]*dt)
    y2.append(y2[-1]+vy2[-1]*dt)
    t.append(t[-1]+dt)
    
fig=matplotlib.pyplot.figure(figsize=[8,8])
matplotlib.pyplot.plot(x1,y1,label='sun')
matplotlib.pyplot.plot(x2,y2,label='planet')
matplotlib.pyplot.legend(loc='upper right')

matplotlib.pyplot.xlabel('x(AU)')
matplotlib.pyplot.ylabel('y(AU)')
matplotlib.pyplot.title('k=100')
matplotlib.pyplot.xlim(-2,4)
matplotlib.pyplot.ylim(-1,5)


matplotlib.pyplot.show()
        