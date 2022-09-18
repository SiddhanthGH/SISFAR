# SISFAR (Step-wise Integrator Solution For Atmospheric Reentry)

The program takes in initial orbital parameters and simulates, step by step, the trajectory of the spacecraft with those initial parameters through Earth's atmosphere, presenting the data in a graph post calculation.

If running through python, the program requires PyQt5, math, matplotlib and sys (math and sys are built into python).
When running through python simply double click on Launcher.py. Ensure that Launcher.py and SIScript are kept in the same folder.

The release build now comes in a folder with all the necessary prerequisites. If you do not have python, run the program through
Launcher.exe. This is slower than running through Launcher.py as it adds 5 seconds to the boot up time.

-----------------------------------------------------------------------------------
Mathematics used:
https://engineering.purdue.edu/AAE450s/trajectories/Atmospheric%20Re-Entry.pdf
