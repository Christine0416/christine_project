import os, subprocess

from CovidSimReport9.SimulationForFig1and3.parameterVary import makeFileVariation

threadNumber = 8
runNumber = 10
rValue = 2.4

# Input from CovidSim
simulatorDirectory = os.path.join( os.getcwd(), "covid-sim" )
sourceDirectory = os.path.join( simulatorDirectory, "src" )
dataDirectory = os.path.join( simulatorDirectory, "report9" )
# preParamReference = os.path.join( dataDirectory, "GB_mitigation", "preGB_R0=2.0.txt" )
preParamReference = os.path.join( dataDirectory, "GB_mitigation", "preUS_R0=2.0.txt" )

#paramReference = os.path.join( dataDirectory, "GB_mitigation", "p_CI_HQ_SDOL70.txt" )
paramReference = os.path.join( dataDirectory, "GB_mitigation", "p_PC_CI_HQ_SDOL70.txt" )

#populationInput = os.path.join( dataDirectory, "population", "wpop_eur.txt.gz" )
# populationText = os.path.join( dataDirectory, "population", "GB_pop2018_nhs.txt" )
populationText = os.path.join( dataDirectory, "population", "wpop_us_terr.txt" )

# Local paths
workingDirectory = os.getcwd()
buildDirectory = os.path.join( workingDirectory, "build" )
referenceOutput = os.path.join( workingDirectory, "referenceOutput" )
simulator = os.path.join( buildDirectory, "src", "CovidSim" )
populationBinary = os.path.join( referenceOutput, "GB_pop2018_nhs.bin" )
networkBinary = os.path.join( referenceOutput, "Network_United_Kingdom_T8_R2.4.bin" ) # Network varies with thread number and R

# Check for existing git repo
if not os.path.exists( simulatorDirectory ):

  # Git checkout CovidSim
  subprocess.run( "git clone https://github.com/Christine0416/covid-sim", check=False, shell=True )
  os.chdir( simulatorDirectory )
  # subprocess.run( "git checkout 92d414769c6387a08ab65d9830f7f9775fdd3a71", check=True, shell=True )
  subprocess.run( "git checkout 2d8d0b893ce29bc83ca91017088eed390b4c8758", check=True, shell=True )

  os.chdir( workingDirectory )

  # Turn on all required output data
  makeFileVariation( preParamReference, "localCopy.txt", { "[OutputSeverityAdminUnit]": 1, "[OutputAge]": 1,
                                                           "[OutputControls]": 1, "[OutputNonSeverity]": 1, "[OutputSeverityAge]": 1 } )
  subprocess.run( "mv localCopy.txt " + preParamReference, check=True, shell=True )

# Check for existing reference
if not os.path.exists( populationBinary ):

  # Build
  os.makedirs( buildDirectory, exist_ok=True )
  os.makedirs( referenceOutput, exist_ok=True )
  os.chdir( buildDirectory )
  subprocess.run( "cmake3 " + simulatorDirectory, check=False, shell=True )
  subprocess.run( "make" , check=False, shell=True )
  os.chdir( workingDirectory )

  # Unzip population file
  #import shutil, gzip
  #with gzip.open( populationInput, 'rb' ) as f_in:
  #  with open( populationText, 'wb' ) as f_out:
  #    shutil.copyfileobj( f_in, f_out )

  # Reference run
  os.makedirs( referenceOutput, exist_ok=True )
  referenceCommand = simulator
  referenceCommand += " /c:" + str(threadNumber)
  referenceCommand += " /NR:" + str(runNumber)
  referenceCommand += " /PP:" + preParamReference
  referenceCommand += " /P:" + paramReference
  referenceCommand += " /O:" + referenceOutput
  referenceCommand += " /D:" + populationText
  referenceCommand += " /M:" + populationBinary     # Cache for later
  referenceCommand += " /S:" + networkBinary        # Cache for later
  referenceCommand += " /R:" + str( rValue / 2.0 )  # Input parameter file R=2 scaled to give R=2.4
  referenceCommand += " /CLP1:100 /CLP2:91 /CLP3:121 /CLP4:121" #report9
  referenceCommand += " 98798150 729101 17389101 4797132"
  referenceCommand += "; mv " + referenceOutput + ".* " + referenceOutput  # Move results to output dir
  subprocess.run( referenceCommand, check=False, shell=True )
  print( referenceCommand )

# Any run using the reference binary files
def runWithCache( preParamPath, paramPath, outputPath, varyIndex ):
  global threadNumber, populationBinary, networkBinary, rValue, simulator

  outputPath += str( varyIndex )
  os.makedirs( outputPath, exist_ok=True )

  # Create parameter variation
  variationParameters = os.path.join( outputPath, "Parameters.txt" )
  if varyIndex > 0:

    makeFileVariation( paramPath, variationParameters, { "[Relative household contact rate after closure]": 1.0 + (0.1*(varyIndex-1)) } )

  else:
    makeFileVariation( paramPath, variationParameters, {} )

  command = simulator
  command += " /c:" + str(threadNumber)
  command += " /NR:" + str(runNumber)
  command += " /PP:" + preParamPath
  command += " /P:" + variationParameters
  command += " /O:" + outputPath
  command += " /D:" + populationBinary     # Use cache
  command += " /L:" + networkBinary        # Use cache
  command += " /R:" + str( rValue / 2.0 )  # Input parameter file R=2 scaled to give R=2.4
  command += " /CLP1:100 /CLP2:91 /CLP3:121 /CLP4:121" #report9
  command += " 98798150 729101 17389101 4797132"
  command += "; mv " + outputPath + ".* " + outputPath  # Move results to output dir
  return subprocess.Popen( command, shell=True )

processes = []

# Validate binaries
validateOutput = os.path.join( workingDirectory, "validateOutput" )
processes.append( runWithCache( preParamReference, paramReference, validateOutput, 0 ) )

# Variation runs
variationOutput = os.path.join( workingDirectory, "variationOutput" )
for i in range( 1, 12 ):
  processes.append( runWithCache( preParamReference, paramReference, variationOutput, i ) )

for process in processes:
  process.wait()

print( "All variations complete" )
