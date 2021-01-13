import os, subprocess

simulatorDirectory = os.path.join( os.getcwd(), "covid-sim" )
workingDirectory = os.getcwd()

print(workingDirectory)

# Check for existing git repo
   
os.makedirs('MeanT16_NR10_GBmitigation')

os.system('cp covid-sim_batch_GB.batch covid-sim/report9/GB_mitigation')
os.system('cp batch_GBmitigation.sh covid-sim/report9/GB_mitigation') 

os.chdir('covid-sim/report9/GB_mitigation')

os.system('sbatch covid-sim_batch_GB.batch')

