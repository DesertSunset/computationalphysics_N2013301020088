from pylab import *

v=[]

v.append(float(input('please input the inital velocity:')))
a=(float(input('please input the a constant for an applied force:')))
b=(float(input('please input the b constant for friction:')))
t=numpy.linspace(0,0.1,1000)

for i in range(999):
    v.append(v[i]+(a-b*v[i])*t[1]

plot(t,v) 
show()
