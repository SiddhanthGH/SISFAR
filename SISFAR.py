import time
import math
from matplotlib import pyplot as plt

W = float(input("Weight of craft: "))
C = float(input("Drag coefficient of craft: "))
A = float(input("Surface area of craft: "))

B = W/(C*A)
print(B)

h = float(input("Starting altitude in meters ASL: "))
v = float(input("Initial velocity: "))
gam = float(input("Degrees from local horizantal in degrees: "))
gam = gam*(math.pi/180)
g = 9.81

dt = float(input("Enter time step: "))
t = 0
j = 0
ran = 0

plt.rcParams["figure.figsize"] = [10.00, 6.50]
plt.rcParams["figure.autolayout"] = True

while True:
    #Clock
        t = t + dt
        x = t
    #Atmos Sim
        if h >= 25000:
            T = -131.21 + (0.00299*h)
            P = 2.488 * (((T+273.1)/216.6)**(-11.388))
        elif h < 25000:
            if h >= 11000:
                T = -56.46
                P = 22.65 * (math.e**(1.73-(0.000157*h)))
            elif h < 11000:
                T = 15.04 - (0.00649*h)
                P = 101.29 * (((T+273.1)/288.08)**5.256)
  
    #Dynamic Pressure Sim
        p = P/(0.2869*(T+273.1))
        Q = (p*(v**2))/2
    #Velocity Sim
        u = v
        v = (dt*g*((-Q/B)+math.sin(gam))) + v
        L = 0/C
    #Angle Sim
        gam = dt*((((-(Q*g)/B)*(L))+(math.cos(gam)*(g-((v**2)/(6371000+h)))))/v) + gam
    #Altitude Sim
        h = dt*(-v)*math.sin(gam) + h
        print(h)
    #Range Sim
        ran = dt*((6371000*v*math.cos(gam))/(6371000+h)) + ran
    #Graphics
        o = h
        z = ran
        y = v
        if t > 0.1:
            j = abs((v-u)/dt)
        plt.xlim(0, 1000)
        plt.ylim(0, 2000000)
        plt.grid()
        plt.plot(x, z, marker="o", markersize=2, markeredgecolor="purple", markerfacecolor="purple")
        plt.plot(x, o, marker="o", markersize=2, markeredgecolor="blue", markerfacecolor="blue")
        plt.plot(x, y, marker="o", markersize=2, markeredgecolor="red", markerfacecolor="red")
        plt.plot(x, j, marker="o", markersize=2, markeredgecolor="green", markerfacecolor="green")
    #Off Check
        if v <= 7:
            print("time (s): ", t)
            print("velocity (m/s): ", v)
            print("Downrange (km): ", ran/1000)
            plt.show()
            break
        if h < 0.1:
            print("time (s): ", t)
            print("velocity (m/s): ", v)
            print("Downrange (km): ", ran/1000)
            plt.show()
            break