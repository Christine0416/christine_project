This archive contains raw data for our publication "The long term predictions from Imperial College CovidSim Report 9", along with scripts to reproduce the tables and figures in that publication from the raw data files.

The data was produced using the CovidSim package (https://github.com/mrc-ide/covid-sim), so we also include scripts to check-out, compile, and run this simulation such that all raw data can be identically reproduced.
Note that simulations will take several hours to run.
Although the data files are labelled with the .xls extension, this is purely a historical quirk: they are plain text in the Tab Separated Value format.
We do not use the majority of the observables that are simulated, but this data is still included for the sake of completeness.
Documentation for the simulator and its outputs can be found here: https://github.com/mrc-ide/covid-sim/tree/master/docs

Note that the directories afterClosureScan8T10R.CI_HQ_SDOL70 and afterClosureScan8T10R.PC_CI_HQ_SDOL70 are both used to produce Figures 1 and 3, and contain subdirectories with raw data from several simulations with varying initial parameters.
CI_HQ_SDOL70 and PC_CI_HQ_SDOL70 refer to public health intervention scenarios described in the paper.
Similarly, directories DataFiles_Fig2 and DataFiles_Fig4 contain raw data outputs from simulations of a variety of these scenarios, and are used to create Figures 2 and 4 respectively.
(EW_Scotland_Deaths.dat is public data from the National Records of Scotland, as referenced in the paper)

All other directories contain scripts to reproduce the corresponding figures, or to reproduce the raw data from simulation.
Additional README files can be found inside.
