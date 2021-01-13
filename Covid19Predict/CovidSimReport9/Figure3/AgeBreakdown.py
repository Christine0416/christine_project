import sys
import numpy as np
import json
import matplotlib.pyplot as pl
import csv
import matplotlib as mpl

# Set the plot line colours
myColours=[]
#for i in range(0, 17):
#  myColours.append( ( i/16.0, 0.0, 1.0 - (i/16.0) ) )
#for colour in pl.cm.plasma( np.linspace( 0.05, 0.8, 17 ) ):
for colour in pl.cm.viridis( np.linspace( 0.05, 0.8, 17 ) ):
#for colour in pl.cm.inferno( np.linspace( 0.05, 0.8, 17 ) ):
   myColours.append( colour )
mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color=myColours)

ageTotals = [
3814507.0,
4421029.0,
4199254.0,
3899857.0,
3932816.0,
4351803.0,
4721333.0,
4592851.0,
4267033.0,
4263877.0,
4361712.0,
4160776.0,
3340665.0,
2816566.0,
2951720.0,
2207184.0,
2990930.0]

#------------------------------
#These lists correspond to the row-1 of various .xls files that CovidSim outputs
#You will see later that my plotting function sums numbers over everything appearing in one of these lists
#So for example if you wanted to sum deaths over age 60-85 you wold create ['D60-65', 'D65-70', 'D70-75', 'D75-80', 'D80-85']

#This first set is in the ones caled "United_Kingdom_<scenario>.avNE.age.xls"
deathCategories = ['D0-5', 'D5-10','D10-15', 'D15-20', 'D20-25', 'D25-30', 'D30-35', 'D35-40', 'D40-45', 'D45-50', 'D50-55', 'D55-60', 'D60-65', 'D65-70', 'D70-75', 'D75-80', 'D80-85']

criticalCategories = [ 'C0-5', 'C5-10', 'C10-15', 'C15-20', 'C20-25', 'C25-30', 'C30-35', 'C35-40', 'C40-45', 'C45-50', 'C50-55', 'C55-60', 'C60-65', 'C65-70', 'C70-75', 'C75-80', 'C80-85' ]

incidenceCategories = [ 'I0-5', 'I5-10', 'I10-15', 'I15-20', 'I20-25', 'I25-30', 'I30-35', 'I35-40', 'I40-45', 'I45-50', 'I50-55', 'I55-60', 'I60-65', 'I65-70', 'I70-75', 'I75-80', 'I80-85' ]

#This second set pertains the the files called "United_Kingdom_<scenario>.avNE.severity.xls"
caseSumCats = ['cumMild', 'cumILI', 'cumSARI', 'cumCritical',  'cumCritRecov',  'cumDeaths' ] #age breakdown different categories to combined severity output
deathSumCats = ['cumDeaths' ]

# Sum over different death categories because of bug in the Covid-sim age breakdown output
caseIncCats = ['incMild', 'incILI', 'incSARI', 'incCritical',  'incCritRecov',  'incDeath_ILI', 'incDeath_SARI', 'incDeath__Critical' ]
deathIncCats = ['incDeath_ILI', 'incDeath_SARI', 'incDeath__Critical' ]

ICU1 = ['Critical' ]
ICU2 = ['CriticalP' ]
ICU3 = ['incCritical' ]
ICU4 = ['incCriticalP' ]


#-------------- Main function to read a .csv file and return all the data  -------------
#It returns a list of dictionaries for each day
# [ {..day1 .}  , {...day2 ..},  {..day3..}  ..... ]

def readCSV( inputfile, ndays=100, nstart=0 ):

    fh = open( inputfile )

    DRobj = csv.DictReader( fh, dialect='excel-tab' )

    firstRow = next(DRobj)
    print('Reading file '+inputfile)
    print('keys: ',firstRow.keys())

    daylist = []
    for row in DRobj :
        if float(row['t']) <nstart :continue
        if float(row['t']) >=ndays :break
        day = { key: float(row[key])  for key in row.keys() }
        daylist.append(day)
    return daylist


#-------------------- Funciton to create a plot for list of scenarios -------------
# A scenario corresponds to a given parameter file in param_files
# This sums all the numbers specified by catlist

def timePlot( scenariolist, labellist, catlist, title='', ylim = 0, scale=1., ytitle='' ):

    for i in range(len(scenariolist)):
        scenario = scenariolist[i]
        label = labellist[i]
        day = []
        dtot = []
        for dayitem in scenario:
            deaths = 0
            for cat in catlist[i]: deaths += dayitem[cat]
            day.append(dayitem['t'])
            dtot.append(deaths)
        scale = 100.0 / ageTotals[i]
        dtotscaled = [ x*scale for x in dtot ]
        pl.plot( day, dtotscaled, label=label, linewidth=3 )

    pl.title(title, fontsize=12, fontweight="bold")
    pl.xlabel('Time (day of year)', fontsize=12 )
    pl.ylabel(ytitle, fontsize=12 )
    pl.ticklabel_format(axis="y")
    pl.legend(labellist, prop={'size': 12} , loc='upper left')
    if ylim > 0: pl.ylim(0., ylim)

#--------------------------
def main():

    #This is where you list what you want to plop
    ndays = 400
    scenariolist1=[]
    scenariolist2=[]
    labellist=[]
    caseIncCatsList=[]
    deathIncCatsList=[]

    for i in range( 0, 17 ):
      scenariolist1.append( readCSV( '../afterClosureScan8T10R.CI_HQ_SDOL70/validateOutput0/validateOutput0.avNE.severity.age.xls', ndays=ndays ) )
      scenariolist2.append( readCSV( '../afterClosureScan8T10R.PC_CI_HQ_SDOL70/validateOutput0/validateOutput0.avNE.severity.age.xls', ndays=ndays ) )
      labellist.append( 'Age ' + str(i*5) + " - " + str((i+1)*5) )

      # Get the category names at each age group
      caseIncCatsAge = []
      for cat in caseIncCats:
        caseIncCatsAge.append( cat + "_" + str(i) )
      caseIncCatsList.append( caseIncCatsAge )

      deathIncCatsAge = []
      for cat in deathIncCats:
        deathIncCatsAge.append( cat + "_" + str(i) )
      deathIncCatsList.append( deathIncCatsAge )

    # Fix last label
    labellist[16] = "Age 80+"


    # Plot all scanarios for a given "category" on a single plot to compare
    # This sums all the numbers specified by the categories argment  (third argument)
    
    fig = pl.figure(figsize=(16, 12), dpi=80)
    pl.subplot(2,2,1)
    timePlot( scenariolist1, labellist, caseIncCatsList, title='CI_HQ_SDOL70', ylim=1.4, ytitle='Daily cases (percentage of age group)' )
    pl.subplot(2,2,2)
    timePlot( scenariolist1, labellist, deathIncCatsList, title='CI_HQ_SDOL70', ylim=0.06, ytitle='Daily deaths (percentage of age group)' )
    pl.subplot(2,2,3)
    timePlot( scenariolist2, labellist, caseIncCatsList, title='PC_CI_HQ_SDOL70', ylim=1.4, ytitle='Daily cases (percentage of age group)' )
    pl.subplot(2,2,4)
    timePlot( scenariolist2, labellist, deathIncCatsList, title='PC_CI_HQ_SDOL70', ylim=0.06, ytitle='Daily deaths (percentage of age group)' )


    fig.tight_layout()
    #pl.show()
    pl.savefig( "AgeBreakdown.pdf" )

main()
