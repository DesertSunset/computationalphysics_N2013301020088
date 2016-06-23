from __future__ import division 
import matplotlib 
import numpy as np 
import matplotlib.cm as cm 
import matplotlib.mlab as mlab 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D 
from copy import deepcopy
from pylab import *

v = []


for i in range(101):    
    row_i = []
    for j in range(101):
        if i == 0 or i == 100 or j == 0 or j == 100:
            voltage = 0
        elif 40<=i<=70 and j == 40:
            voltage = 1
        elif 40<=i<=70 and j == 70:
            voltage = -1
        else:
            voltage = 0
        row_i.append(voltage)
    v.append(row_i)

    
def update_V(v):

    delta_V = 0

    for j in range(56):    
        for i in range(101):
            if i == 0 or i==100 or j == 0:  
                pass
            elif 40<=i<=55 and j == 40:
                pass
            elif 40<=i<=55 and j == 70:
                pass
            else:
                voltage_new = (v[i+1][j]+v[i-1][j]+v[i][j+1]+v[i][j-1])/4
                voltage_old = v[i][j]
                delta_V += abs(voltage_new - voltage_old)
                v[i][j] = voltage_new
                v[110-i][j]=-v[i][j] 
    return v, delta_V
    
def Laplace_calculate(v):
    
    epsilon = 10**(-5)*100**2
    delta_V = 0
    N_iter = 0

    while delta_V >= epsilon or N_iter <= 10:
        v1, delta_V = update_V(v)
        v2, delta_V = update_V(v1)
        v = v2
        N_iter += 1
    

            
    return v2
    

                
x = np.linspace(0,100,101)
y = np.linspace(0,100,101)
X, Y = np.meshgrid(x, y)
Z =Laplace_calculate(v)

plt.figure()
CS = plt.contour(X,Y,Z,10)
plt.clabel(CS, inline=1, fontsize=12)
plt.title('voltage near capacitor')
plt.xlabel('x(m)')
plt.ylabel('y(m)')