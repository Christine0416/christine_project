The files here will generate the data for the GB mitigation scenarios presented in Report 9 for R0 = 2.4. There is also a python script for generating Figure 2.  The first step is to run covid_run_GBmitigation_runonce.py.  This will extract CovidSim from the GitHub repository, compile it, and run it once to generate the necessary population files. Once this has completed, you can then run covid_run_GBmitigation.py which will run the simulation for all of the GB mitigation scenarios presented in Report 9, for R0 = 2.4. 

Once all of the GB mitigation scenarios have been run, plot_CritCare_Fig2.py will generate Figure 2 and will save it as a PDF.

You may, however, need to modify covid-sim_runonce_GB.batch and covid-sim_batch_GB.batch to be suitable for your compute cluster.  
