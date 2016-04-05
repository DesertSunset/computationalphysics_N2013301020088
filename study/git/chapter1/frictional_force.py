from pylab import *

v=[]
t=[0]
a=0
b=0
n=0

v.append(float(input('please input the inital velocity:')))
time=(float(input('please input the total time:')))
a=(float(input('please input the a constant for an applied force:')))
b=(float(input('please input the b constant for friction:')))
dt=float(input('please input the time step:'))
n=int(time / dt)

for i in range(1,n):
    v.append(v[i-1]+(a-b*v[i-1])*dt)
    t.append(t[i-1]+dt)

print v

plot(t,v,'--*')
show()
