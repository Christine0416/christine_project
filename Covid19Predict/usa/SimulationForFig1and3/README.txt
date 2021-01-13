runSimulation.py takes no input, and will checkout CovidSim from GitHub, compile and run it.

To alter the scenario used (e.g. PC_CI_HQ_SDOL70 vs CI_HQ_SDOL70) edit the paramReference value near the start of runSimulation.py. Note that results for one scenario will overwrite the other, so be sure to move the output directories to somewhere else before re-running.

Results will take several hours to compute, using 10 CPU threads and 30-40 GB of RAM

Once you have results for both scenarios you can use the scripts in the Figure1 and Figure3 directories to reproduce those figures
