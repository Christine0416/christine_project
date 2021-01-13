import os, subprocess

simulatorDirectory = os.path.join( os.getcwd(), "covid-sim" )
workingDirectory = os.getcwd()

print(workingDirectory)

# Check for existing git repo
if not os.path.exists( simulatorDirectory ):

   # Git checkout CovidSim
   subprocess.run( "git clone https://github.com/mrc-ide/covid-sim", check=True, shell=True )
   os.chdir( simulatorDirectory )
   subprocess.run( "git checkout 92d414769c6387a08ab65d9830f7f9775fdd3a71", check=True, shell=True )
   os.chdir(workingDirectory) 

   os.chdir('covid-sim')
   os.makedirs('build')
   os.chdir('build')

   os.system('pwd') 

   subprocess.run(['cmake','..'], check=True)
   subprocess.run(['make'])
   os.system('cp src/CovidSim ../report9/GB_mitigation')

   os.chdir(workingDirectory)

   os.system('pwd')

   os.system('cp covid-sim_runonce_GB.batch covid-sim/report9/GB_mitigation') 
   os.system('cp runonce.sh covid-sim/report9/GB_mitigation')

   os.chdir('covid-sim/report9/GB_mitigation')
   os.system('sbatch covid-sim_runonce_GB.batch')
   
#   os.system('cp covid-sim/data/populations/wpop_eur.txt.gz .')
#   os.system('gunzip wpop_eur.txt.gz')

#   os.makedirs('MeanT16_NR10')

#   os.system('sbatch covid-sim_batch_calib_UK.batch')

