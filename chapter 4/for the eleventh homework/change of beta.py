import matplotlib.pyplot
import math

vy0=float(input('please input the initial velocity of the planet :'))

x1=[0]
y1=[0]

def circle(q):
    x2=[1]
    y2=[0]
    vx1=[0]
    vy1=[0]
    vx2=[0]
    vy2=[vy0*math.pi]
    t=[0]
    dt=0.002
    GM=4*math.pi*math.pi


    while t[-1]<1:

        r=math.sqrt((x1[-1]-x2[-1])**2+(y1[-1]-y2[-1])**2)
        ox2=-GM*(x2[-1]-x1[-1])/(r**(q+1))
        oy2=-GM*(y2[-1]-y1[-1])/(r**(q+1))
        vx2.append(vx2[-1]+ox2*dt)
        vy2.append(vy2[-1]+oy2*dt)
        x2.append(x2[-1]+vx2[-1]*dt) 
        y2.append(y2[-1]+vy2[-1]*dt)
        t.append(t[-1]+dt)
        
    return x2,y2

x21=circle(2)[0]
y21=circle(2)[1]

x22=circle(2.01)[0]
y22=circle(2.01)[1]

x23=circle(2.1)[0]
y23=circle(2.1)[1]

x24=circle(2.5)[0]
y24=circle(2.5)[1]

x25=circle(3)[0]
y25=circle(3)[1]

fig=matplotlib.pyplot.figure(figsize=[8,8])
matplotlib.pyplot.scatter(x1,y1,label='sun')
matplotlib.pyplot.scatter(x21,y21,label='planet beta=2',s=2,color='red')
matplotlib.pyplot.scatter(x22,y22,label='planet beta=2.01',s=2,color='green')
matplotlib.pyplot.scatter(x23,y23,label='planet beta=2.1',s=2,color='purple')
matplotlib.pyplot.scatter(x24,y24,label='planet beta=2.5',s=2,color='orange')
matplotlib.pyplot.scatter(x25,y25,label='planet beta=3',s=4,color='pink')

matplotlib.pyplot.legend(loc='upper right')

matplotlib.pyplot.xlabel('x(AU)')
matplotlib.pyplot.ylabel('y(AU)')
matplotlib.pyplot.title('v0=2')
matplotlib.pyplot.xlim(-1,1.2)
matplotlib.pyplot.ylim(-1,1)

matplotlib.pyplot.show()