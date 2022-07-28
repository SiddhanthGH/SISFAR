import time
import math
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches

M = float(input("Mass of craft: "))
W = M*9.81
C = float(input("Drag coefficient of craft: "))
A = float(input("Surface area of craft: "))
L = float(input("Lift coefficient of craft: "))/C
B = W/(C*A)
h = float(input("Starting altitude in meters ASL: "))
hi = h
v = float(input("Initial velocity: "))
gam = float(input("Degrees from local horizantal in degrees: "))
gam = gam*(math.pi/180)
g = 9.81
dt = 0.1

t = 0
ran = 0
n = 0

plt.rcParams["figure.figsize"] = [14.00, 8.00]
plt.rcParams["figure.autolayout"] = True

while h > 0.1:
    #Clock
        t = t + dt
        n = n + 1
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
        acel = abs((v-u)/dt)
        if acel <= g:
            dt = 0.2
        elif acel > g:
            dt = 0.1
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
        j = acel
        if n%2 == 0:
            plt.plot(x, z, marker="o", markersize=1, markeredgecolor="purple", markerfacecolor="purple")
            plt.plot(x, o, marker="o", markersize=1, markeredgecolor="blue", markerfacecolor="blue")
            plt.plot(x, y, marker="o", markersize=1, markeredgecolor="red", markerfacecolor="red")
            plt.plot(x, j, marker="o", markersize=1, markeredgecolor="green", markerfacecolor="green")
#Plot Graph
plt.xlim()
plt.ylim()
plt.xlabel("time / s")
plt.ylabel("Downrange / m | Altitude / m | Velocity / ms^-1 | Acceleration / ms^-2")
plt.grid()
#Add Legend
red_patch = mpatches.Patch(color='red', label='Velocity')
blue_patch = mpatches.Patch(color='blue', label='Altitude')
green_patch = mpatches.Patch(color='green', label='Acceleration')
purple_patch = mpatches.Patch(color='purple', label='Downrange')
plt.legend(handles=[red_patch, blue_patch, green_patch, purple_patch])
#Print Final Data
print("time (s): ", t)
print("velocity (m/s): ", v)
print("Downrange (km): ", ran/1000)
plt.show()