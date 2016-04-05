from pylab import *

n_uranium=[]
t=[0]
tau=0
dt=0
n=0

n_uranium.append(float(input('please input the n_uranium:')))
time=(float(input('please input the total time:')))
tau=float(input('please input the time constant:'))
dt=float(input('please input the time step:'))
n=int(time / dt)

for i in range(1,n):
    n_uranium.append(n_uranium[i-1]-n_uranium[i-1]/tau*dt)
    t.append(t[i-1]+dt)

plot(t,n_uranium,'--*')
show()


