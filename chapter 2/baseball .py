# -*- coding: utf-8 -*-

from pylab import *
from matplotlib import pyplot
import math
import numpy

g = 9.8
S0m=4.1e-4

v_=float(input('please input the inital velocity :'))
theta_=float(input('please input the firing angle :'))
v_wind=float(input('please input the velocity of the wind :'))
w0=float(input('please input the angular velocity :'))



class initial_state:
    def __init__(self, _v = 0, v_wind = 0, _theta = 0):
        _rad = _theta*math.pi/180
        self.vx = _v * math.cos(_rad)
        self.vy = _v * math.sin(_rad)
        self.v_wind = v_wind
        self.vz =0   
        
class flight_state:
    def __init__(self, _x = 0, _y = 0, _z = 0, _vx = 0, _vy = 0, _vz = 0, _t = 0):
        self.x = _x
        self.y = _y
        self.z = _z     
        self.vx = _vx
        self.vy = _vy
        self.vz = _vz        
        self.t = _t

class cannon1:
    def __init__(self, _fs = flight_state(0, 0, 0, 0, 0), _dt = 0.1):
        self.cannon_flight_state = []
        self.cannon_flight_state.append(_fs)
        self.dt = _dt

    def next_state1(self, current_state):
        v = sqrt((current_state.vx-v_wind) * (current_state.vx-v_wind) + current_state.vy * current_state.vy)
        b2m =0.0039+0.0058/(1+math.exp((v-35)/5))
        pp0 = (1 - 6.5e-3 * current_state.y / 288.15) ** (2.5)
        next_x = current_state.x + current_state.vx * self.dt
        next_vx = current_state.vx - pp0 * b2m * v * (current_state.vx-v_wind) * self.dt
        next_y = current_state.y + current_state.vy * self.dt
        next_vy = current_state.vy - g * self.dt - pp0 * b2m * v * current_state.vy * self.dt
        next_z = current_state.z + current_state.vz * self.dt
        next_vz = current_state.vz
        return flight_state(next_x, next_y,next_z, next_vx, next_vy, next_vz,current_state.t + self.dt)


    def shoot1(self):
        while not(self.cannon_flight_state[-1].y < 0):
            self.cannon_flight_state.append(self.next_state1(self.cannon_flight_state[-1]))

        r = - self.cannon_flight_state[-2].y / self.cannon_flight_state[-1].y
        self.cannon_flight_state[-1].x = (self.cannon_flight_state[-2].x + r * self.cannon_flight_state[-1].x) / (r + 1)
        self.cannon_flight_state[-1].y = 0

    def show_trajectory1(self):
        x1 = []
        y1 = []
        z1 = []
        for fs in self.cannon_flight_state:
            x1.append(fs.x)
            y1.append(fs.y)
            z1.append(fs.z)
            global x1
            global y1
            global z1
            
class cannon2(cannon1):
    def __init__(self, _fs = flight_state(0, 0, 0, 0, 0,0,0), _dt = 0.1):
        self.cannon_flight_state2 = []
        self.cannon_flight_state2.append(_fs)
        self.dt = _dt            

    def next_state2(self, current_state):
        global g, b2m ,S0m
        v = sqrt((current_state.vx-v_wind) * (current_state.vx-v_wind) + current_state.vy * current_state.vy)
        b2m =0.0039+0.0058/(1+math.exp((v-35)/5))
        pp0 = (1 - 6.5e-3 * current_state.y / 288.15) ** (2.5)
        next_x = current_state.x + current_state.vx * self.dt
        next_vx = current_state.vx - pp0 * b2m * v * (current_state.vx-v_wind) * self.dt-S0m* (current_state.vz) *w0* self.dt
        next_y = current_state.y + current_state.vy * self.dt
        next_vy = current_state.vy - g * self.dt - pp0 * b2m * v * current_state.vy * self.dt
        next_z = current_state.z + current_state.vz * self.dt
        next_vz = current_state.vz + S0m* (current_state.vx-v_wind) *w0* self.dt
        return flight_state(next_x, next_y,next_z, next_vx, next_vy, next_vz,current_state.t + self.dt)


    def shoot2(self):
        while not(self.cannon_flight_state2[-1].y < 0):
            self.cannon_flight_state2.append(self.next_state2(self.cannon_flight_state2[-1]))

        r = - self.cannon_flight_state2[-2].y / self.cannon_flight_state2[-1].y
        self.cannon_flight_state2[-1].x = (self.cannon_flight_state2[-2].x + r * self.cannon_flight_state2[-1].x) / (r + 1)
        self.cannon_flight_state2[-1].y = 0

        
    def show_trajectory2(self):
        x2 = []
        y2 = []
        z2 = []
        for fs in self.cannon_flight_state2:
            x2.append(fs.x)
            y2.append(fs.y)
            z2.append(fs.z)
            global x2
            global y2
            global z2

class cannon3(cannon1):
    def __init__(self, _fs = flight_state(0, 0, 0, 0, 0,0,0), _dt = 0.1):
        self.cannon_flight_state3 = []
        self.cannon_flight_state3.append(_fs)
        self.dt = _dt            

    def next_state3(self, current_state):
        global g, b2m ,S0m
        v = sqrt((current_state.vx-v_wind) * (current_state.vx-v_wind) + current_state.vy * current_state.vy)
        b2m =0.0039+0.0058/(1+math.exp((v-35)/5))
        pp0 = (1 - 6.5e-3 * current_state.y / 288.15) ** (2.5)
        next_x = current_state.x + current_state.vx * self.dt
        next_vx = current_state.vx - pp0 * b2m * v * (current_state.vx-v_wind) * self.dt+S0m* (current_state.vy) *w0* self.dt
        next_y = current_state.y + current_state.vy * self.dt
        next_vy = current_state.vy - g * self.dt - pp0 * b2m * v * current_state.vy * self.dt+S0m* (current_state.vx-v_wind) *w0* self.dt
        next_z = current_state.z + current_state.vz * self.dt
        next_vz = current_state.vz 
        return flight_state(next_x, next_y,next_z, next_vx, next_vy, next_vz,current_state.t + self.dt)


    def shoot3(self):
        while not(self.cannon_flight_state3[-1].y < 0):
            self.cannon_flight_state3.append(self.next_state3(self.cannon_flight_state3[-1]))

        r = - self.cannon_flight_state3[-2].y / self.cannon_flight_state3[-1].y
        self.cannon_flight_state3[-1].x = (self.cannon_flight_state3[-2].x + r * self.cannon_flight_state3[-1].x) / (r + 1)
        self.cannon_flight_state3[-1].y = 0

        
    def show_trajectory3(self):
        x3 = []
        y3 = []
        z3 = []
        for fs in self.cannon_flight_state3:
            x3.append(fs.x)
            y3.append(fs.y)
            z3.append(fs.z)
            global x3
            global y3
            global z3

    
    def show_out1(self):   

        matplotlib.pyplot.figure(figsize=(8,6))
        matplotlib.pyplot.plot(x1,y1,label="without the effect of backspin",color="red",linewidth=3,linestyle='--')
        matplotlib.pyplot.plot(x2,y2,label="with the effect of backspin(w in -y direction) ",color="blue",linewidth=3,linestyle='--')
        matplotlib.pyplot.plot(x3,y3,label="with the effect of backspin(w in -z direction) ",color="green",linewidth=3,linestyle='--')
        matplotlib.pyplot.xlabel("x(m)")
        matplotlib.pyplot.title("adiabatic drag baseball with the wind in the front view")
        matplotlib.pyplot.ylabel("y(m)")
        matplotlib.pyplot.legend(loc='best')
        matplotlib.pyplot.show()
       
    def show_out2(self):   

        matplotlib.pyplot.figure(figsize=(8,6))
        matplotlib.pyplot.plot(x1,z1,label="without the effect of backspin",color="red",linewidth=3,linestyle='--')
        matplotlib.pyplot.plot(x2,z2,label="with the effect of backspin(w in -y direction)",color="blue",linewidth=3,linestyle='--')
        matplotlib.pyplot.plot(x3,z3,label="with the effect of backspin(w in -z direction)",color="green",linewidth=3,linestyle='--')
        matplotlib.pyplot.xlabel("x(m)")
        matplotlib.pyplot.title("adiabatic drag baseball with the wind in the vertical view")
        matplotlib.pyplot.ylabel("z(m)")
        matplotlib.pyplot.legend(loc='best')
        matplotlib.pyplot.show()



#给定初速度大小和角度
a = initial_state(v_,v_wind,theta_)
b = cannon1(flight_state(0, 500, 0,a.vx, a.vy,a.vz, 0), _dt = 0.1)
b.shoot1()
b.show_trajectory1()
c = cannon2(flight_state(0, 500, 0,a.vx, a.vy,a.vz, 0), _dt = 0.1)
c.shoot2()
c.show_trajectory2()
d = cannon3(flight_state(0, 500, 0,a.vx, a.vy,a.vz, 0), _dt = 0.1)
d.shoot3()
d.show_trajectory3()
d.show_out1()
d.show_out2()
show()


print "①the maximun range(x) withput the effect of backspin is "
print x1[-1]
print "②the maximun range(x) with the effect of backspin(w in -y direction) is "
print x2[-1]
print "③the maximun range(x) with the effect of backspin(w in -z direction) is "
print x3[-1]
print "④the horizontal displace(z) with the effect of backspin(w in -y direction) is "
print z2[-1]



