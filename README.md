# SISFAR (Step-wise Integrator Solution For Atmospheric Reentry)

CURRENTLY ONLY SUPPORTS EARTH ATMOSPHERIC ENTRY
-
-----------------------------------------------------------------------------------
KEY
-
Purple = Downrange Distance on Earth from simulation start

Blue = Height above mean sea level

Red = Velocity

Green = Acceleration

X axis = time

-----------------------------------------------------------------------------------

Coefficient of lift is set to 0 by default (ballistic reentry).

Coefficient of lift can be inputed by changing the numerator value at line 48

Eg:
{L = 0/C} by default -----> {L = 0.1/C} as changed

-----------------------------------------------------------------------------------

Domain and range can be modified at lines 62 and 63 respectively.

-----------------------------------------------------------------------------------
Mathematics used:
https://engineering.purdue.edu/AAE450s/trajectories/Atmospheric%20Re-Entry.pdf
