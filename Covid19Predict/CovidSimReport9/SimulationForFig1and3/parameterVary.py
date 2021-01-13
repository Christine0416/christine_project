import random

def makeFileVariation( inputPath, outputPath, changeMap ):

  inputFile = open( inputPath, "r" )
  outputFile = open( outputPath, "w" )

  nextChange = None
  skipLines = 0
  for line in inputFile:

    if nextChange:
      outputFile.write( nextChange + "\n" )
      skipLines = len( nextChange.split( "\n" ) )
      nextChange = None

    if skipLines:
      skipLines -= 1
      continue

    for targetParameter in changeMap.keys():
      if targetParameter in line:
        nextChange = str( changeMap[ targetParameter ] )

    outputFile.write( line )

def fuzzParameters( inputPath, outputPath ):

  inputFile = open( inputPath, "r" )
  outputFile = open( outputPath, "w" )

  varyNextLine = False
  skipLines = 0
  for line in inputFile:

    if varyNextLine:

      newLine = ""
      separator = " "
      if "\t" in line:
        separator = "\t"
      for parameter in line.strip().split(separator):

        value = float( parameter )
        if value == 0.0 or value == 1.0:
          newLine += parameter + " "
        else:
          newLine += str( value*random.uniform( 0.1, 1.1 ) ) + " "
        #newLine += str( value*random.uniform( 0.3, 1.3 ) ) + " "

      outputFile.write( newLine + "\n" )
      skipLines = 1
      varyNextLine = False

    if skipLines:
      skipLines -= 1
      continue

    if line[0] == "[":
      varyNextLine = True

    outputFile.write( line )
