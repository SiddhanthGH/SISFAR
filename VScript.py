import math
from matplotlib import pyplot as plt

def Simulation(self):
    #Get Variables
    mass = float(self.M.toPlainText())
    drag_coef = float(self.C.toPlainText())
    surface_area = float(self.A.toPlainText())
    lift_coef = float(self.L.toPlainText())
    initial_alt = float(self.h.toPlainText())
    initial_vel = float(self.v.toPlainText())
    initial_angle = math.radians(float(self.gam.toPlainText()))

    #Check states
    At = self.At.checkState()
    Act = self.Act.checkState()
    Vt = self.Vt.checkState()
    ht = self.ht.checkState()
    rant = self.rant.checkState()
    rana = self.rana.checkState()

    #Preliminary Calculations
    gravity_accel = 3.72
    weight = mass*gravity_accel
    lift = lift_coef/drag_coef
    bal_coef = weight/(drag_coef*surface_area)
    dt = 0.1

    t = 0
    time = [0]
    range = [0]
    alt = [initial_alt]
    vel = [initial_vel]
    accel = [0]
    AoA = [initial_angle]
    curr_alt = initial_alt
    curr_vel = initial_vel
    curr_angle = initial_angle
    curr_range = 0

    plt.rcParams["figure.figsize"] = [14.00, 8.00]
    plt.rcParams["figure.autolayout"] = True

    while curr_alt >= 0.1 :
        #Clock
        t = t + dt
        time.append(t)

        #Atmos Sim (High Density Min Solar Activity Used)
        if curr_alt >= 0:
            p = 112
        if curr_alt >= 5000:
            p = 87.1
        if curr_alt >= 10000:
            p = 66.8
        if curr_alt >= 15000:
            p = 50.6
        if curr_alt >= 20000:
            p = 37.9
        if curr_alt >= 25000:
            p = 27.8
        if curr_alt >= 30000:
            p = 20
        if curr_alt >= 35000:
            p = 14.2
        if curr_alt >= 40000:
            p = 9.72
        if curr_alt >= 45000:
            p = 6.4
        if curr_alt >= 50000:
            p = 4.01
        if curr_alt >= 55000:
            p = 2.36
        if curr_alt >= 60000:
            p = 1.25
        if curr_alt >= 65000:
            p = 0.564
        if curr_alt >= 70000:
            p = 0.25
        if curr_alt >= 75000:
            p = 0.108
        if curr_alt >= 80000:
            p = 0.0451
        if curr_alt >= 85000:
            p = 0.0179
        if curr_alt >= 90000:
            p = 0.0067
        if curr_alt >= 95000:
            p = 0.00239
        if curr_alt >= 100000:
            p = 0.000804
        if curr_alt >= 110000:
            p = 0.0000737
        if curr_alt >= 120000:
            p = 0.0000056
        if curr_alt >= 130000:
            p = 0.000000676
        if curr_alt >= 140000:
            p = 0.0000000838
        if curr_alt >= 150000:
            p = 0.000000015
        if curr_alt >= 160000:
            p = 0.00000000415
        if curr_alt >= 180000:
            p = 0.0000000000692
        if curr_alt >= 200000:
            p = 0.0000000000164
        if curr_alt >= 210000:
            p = 0
        #Dynamic Pressure Sim
        Q = (p*(curr_vel**2))/2
        #Velocity Sim
        past_vel = curr_vel
        curr_vel = (dt*gravity_accel*((-Q/bal_coef)+math.sin(initial_angle))) + past_vel
        vel.append(curr_vel)
        curr_accel = (curr_vel-past_vel)/dt
        accel.append(curr_accel)
        #Angle Sim
        past_angle = curr_angle
        curr_angle = dt*((((-(Q*gravity_accel)/bal_coef)*(lift))+(math.cos(curr_angle)*(gravity_accel-((curr_vel**2)/(6051800+curr_alt)))))/curr_vel) + past_angle
        AoA.append(math.degrees(curr_angle))
        #Altitude Sim
        past_alt = curr_alt
        curr_alt = dt*(-curr_vel)*math.sin(curr_angle) + past_alt
        alt.append(curr_alt)
        #Range Sim
        past_range = curr_range
        curr_range = dt*((6051800*curr_vel*math.cos(curr_angle))/(6051800+curr_alt)) + past_range
        range.append(curr_range)

    if At == 2:
        plt.subplot(2, 3, 6)
        plt.plot(time,AoA,color='yellow')
        plt.xlabel("time / s")
        plt.ylabel("AoA / deg")
        plt.grid()   
        if rant == 2:
            plt.subplot(2, 3, 1)
            plt.plot(time,range, color = 'purple')
            plt.xlabel("time / s")
            plt.ylabel("Downrange / m")
            plt.grid()
        if ht == 2:
            plt.subplot(2, 3, 2)
            plt.plot(time,alt, color = 'blue')
            plt.xlabel("time / s")
            plt.ylabel("Altitude / m")
            plt.grid()    
        if Vt == 2:
            plt.subplot(2, 3, 3)
            plt.plot(time, vel, color='red')
            plt.xlabel("time / s")
            plt.ylabel("Velocity / ms^-1")
            plt.grid()
        if Act == 2:
            plt.subplot(2, 3, 4)
            plt.plot(time,accel, color='green')
            plt.xlabel("time / s")
            plt.ylabel("acceleration / ms^-2")
            plt.grid()
        if rana == 2:
           plt.subplot(2, 3, 5)
           plt.plot(range,alt,color='purple')
           plt.xlabel("Downrange / m")
           plt.ylabel("Altitude / m")
           plt.grid()
    else:
        if rant == 2:
            plt.plot(time,range, color = 'purple')
            plt.xlabel("time / s")
            plt.ylabel("Downrange / m")
            plt.grid()
        if ht == 2:
            plt.plot(time,alt, color = 'blue')
            plt.xlabel("time / s")
            plt.ylabel("Altitude / m")
            plt.grid()    
        if Vt == 2:
            plt.plot(time, vel, color='red')
            plt.xlabel("time / s")
            plt.ylabel("Velocity / ms^-1")
            plt.grid()
        if Act == 2:
            plt.plot(time,accel, color='green')
            plt.xlabel("time / s")
            plt.ylabel("acceleration / ms^-2")
            plt.grid()
        if rana == 2:
           plt.plot(range,alt,color='purple')
           plt.xlabel("Downrange / m")
           plt.ylabel("Altitude / m")
           plt.grid()

    plt.xlim()
    plt.ylim()
    plt.show()