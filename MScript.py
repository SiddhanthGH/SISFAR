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

        #Atmos Sim
        if curr_alt > 7000:
            T = -23.4 - (0.00222*curr_alt)
            P = 0.699 * (math.e**(-0.00009*curr_alt))
        elif curr_alt <= 7000:
            T = -31 - (0.000998*curr_alt)
            P = 0.699 * (math.e**(-0.00009*curr_alt))
        #Dynamic Pressure Sim
        p = P/(0.1921*(T+273.1))
        Q = (p*(curr_vel**2))/2
        #Velocity Sim
        past_vel = curr_vel
        curr_vel = (dt*gravity_accel*((-Q/bal_coef)+math.sin(initial_angle))) + past_vel
        vel.append(curr_vel)
        curr_accel = (curr_vel-past_vel)/dt
        accel.append(curr_accel)
        #Angle Sim
        past_angle = curr_angle
        curr_angle = dt*((((-(Q*gravity_accel)/bal_coef)*(lift))+(math.cos(curr_angle)*(gravity_accel-((curr_vel**2)/(3389500+curr_alt)))))/curr_vel) + past_angle
        AoA.append(math.degrees(curr_angle))
        #Altitude Sim
        past_alt = curr_alt
        curr_alt = dt*(-curr_vel)*math.sin(curr_angle) + past_alt
        alt.append(curr_alt)
        #Range Sim
        past_range = curr_range
        curr_range = dt*((3389500*curr_vel*math.cos(curr_angle))/(3389500+curr_alt)) + past_range
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