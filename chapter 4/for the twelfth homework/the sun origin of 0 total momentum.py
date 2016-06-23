import matplotlib.pyplot
import math

k=float(input('please input the mass of the sun divided by the mass of the Jupiter='))


Gms=4*math.pi*math.pi
Gme=Gms/330000
Gmj=Gms/k

x1=[0]
y1=[0]
x2=[1]
y2=[0]
x3=[5.20]
y3=[0]
vx1=[0]
vy1=[-0.0004415*math.sqrt(Gms/1)]
vx2=[0]
vy2=[math.sqrt(Gms/1)]
vx3=[0]
vy3=[math.sqrt(Gms/5.2)]
t=[0]
dt=0.002


while t[-1]<20:

    r12=math.sqrt((x1[-1]-x2[-1])**2+(y1[-1]-y2[-1])**2)
    r13=math.sqrt((x1[-1]-x3[-1])**2+(y1[-1]-y3[-1])**2)
    r23=math.sqrt((x2[-1]-x3[-1])**2+(y2[-1]-y3[-1])**2)

    ox1=-Gme*(x1[-1]-x2[-1])/(r12**3)-Gmj*(x1[-1]-x3[-1])/(r13**3)
    ox2=-Gms*(x2[-1]-x1[-1])/(r12**3)-Gmj*(x2[-1]-x3[-1])/(r23**3)
    ox3=-Gms*(x3[-1]-x1[-1])/(r13**3)-Gme*(x3[-1]-x2[-1])/(r23**3)

    oy1=-Gme*(y1[-1]-y2[-1])/(r12**3)-Gmj*(y1[-1]-y3[-1])/(r13**3)
    oy2=-Gms*(y2[-1]-y1[-1])/(r12**3)-Gmj*(y2[-1]-y3[-1])/(r23**3)
    oy3=-Gms*(y3[-1]-y1[-1])/(r13**3)-Gme*(y3[-1]-y2[-1])/(r23**3)

    vx1.append(vx1[-1]+ox1*dt)
    vx2.append(vx2[-1]+ox2*dt)
    vx3.append(vx3[-1]+ox3*dt)

    vy1.append(vy1[-1]+oy1*dt)
    vy2.append(vy2[-1]+oy2*dt)
    vy3.append(vy3[-1]+oy3*dt)

    x1.append(x1[-1]+vx1[-1]*dt)
    x2.append(x2[-1]+vx2[-1]*dt)
    x3.append(x3[-1]+vx3[-1]*dt)

    y1.append(y1[-1]+vy1[-1]*dt)
    y2.append(y2[-1]+vy2[-1]*dt)
    y3.append(y3[-1]+vy3[-1]*dt)

    t.append(t[-1]+dt)
    
fig=matplotlib.pyplot.figure(figsize=[8,8])
matplotlib.pyplot.plot(x1,y1,label='Sun',linewidth=2)
matplotlib.pyplot.plot(x2,y2,label='Earth')
matplotlib.pyplot.plot(x3,y3,label='Jupiter')
matplotlib.pyplot.legend(loc='upper right')

matplotlib.pyplot.xlabel('x(AU)')
matplotlib.pyplot.ylabel('y(AU)')
matplotlib.pyplot.title('ms=mj')
