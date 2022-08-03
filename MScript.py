import math
import time
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches

def Simulation(self):
    #Collects vars
     M = float(self.M.toPlainText())
     C = float(self.C.toPlainText())
     A = float(self.A.toPlainText())
     Li = float(self.L.toPlainText())
     h = float(self.h.toPlainText())
     v = float(self.v.toPlainText())
     gam = float(self.gam.toPlainText())
     gam = (gam*(math.pi/180))
     At = self.At.checkState()
     Act = self.Act.checkState()
     Vt = self.Vt.checkState()
     ht = self.ht.checkState()
     rant = self.rant.checkState()
     rana = self.rana.checkState()
    #Necessary Preliminary Calculations
     W = M*3.721
     L = Li/C
     B = W/(C*A)
     hi = h
     g = 3.721
     dt = 0.1

     t = 0
     ran = 0
     n = 0
    #SIMULATION
     plt.rcParams["figure.figsize"] = [14.00, 8.00]
     plt.rcParams["figure.autolayout"] = True
     while h > 0.1:
            #Clock
                t = t + dt
                n = n + 1
                x = t
            #Atmos Sim
                if h > 7000:
                    T = -23.4 - (0.00222*h)
                    P = 0.699 * (math.e**(-0.00009*h))
                elif h <= 7000:
                    T = -31 - (0.000998*h)
                    P = 0.699 * (math.e**(-0.00009*h))
            #Dynamic Pressure Sim
                p = P/(0.1921*(T+273.1))
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
                gam = dt*((((-(Q*g)/B)*(L))+(math.cos(gam)*(g-((v**2)/(3389500+h)))))/v) + gam
            #Altitude Sim
                h = dt*(-v)*math.sin(gam) + h
                print(h)
            #Range Sim
                ran = dt*((3389500*v*math.cos(gam))/(3389500+h)) + ran
            #Graphics
                o = h
                z = ran
                y = v
                j = acel
                if n%2 == 0:
                    #Check Graph State
                    if At + rant >= 2:
                        plt.plot(x, z, marker="o", markersize=1, markeredgecolor="purple", markerfacecolor="purple")
                    if At + ht >= 2:
                        plt.plot(x, o, marker="o", markersize=1, markeredgecolor="blue", markerfacecolor="blue")
                    if At + Vt >= 2:
                        plt.plot(x, y, marker="o", markersize=1, markeredgecolor="red", markerfacecolor="red")
                    if At + Act >= 2:
                        plt.plot(x, j, marker="o", markersize=1, markeredgecolor="green", markerfacecolor="green")
                    if rana == 2:
                        plt.plot(o, z, marker="o", markersize=1, markeredgecolor="purple", markerfacecolor="purple")
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