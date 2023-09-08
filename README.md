# SISFAR (Step-wise Integrator Solution For Atmospheric Reentry)

The program takes in initial orbital parameters and simulates, step by step, the trajectory of the spacecraft with those initial parameters through Earth's atmosphere, presenting the data in a graph post calculation.

If running through python, the program requires PyQt5, math, matplotlib and sys (math and sys are built into python).
Simply double click on Launcher.py.

If you do not have python, run the program through Launcher.exe after downloading it from releases. This is slower than running through Launcher.py.

-----------------------------------------------------------------------------------
Mathematics used:
https://engineering.purdue.edu/AAE450s/trajectories/Atmospheric%20Re-Entry.pdf

Earth Atmospheric Model:
https://www.grc.nasa.gov/www/k-12/airplane/atmosmet.html

Mars Atmospheric Model:
https://www.grc.nasa.gov/www/k-12/airplane/atmosmrm.html

Venus Atmospheric Model:
https://ntrs.nasa.gov/api/citations/19690011554/downloads/19690011554.pdf

**NOTE** The Venus atmospheric model was made in 1968, before actual surveying of its atmosphere began. It is a projection based off Mariner 5 and Venera 4 data.