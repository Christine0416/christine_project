import math
import numpy as np
import matplotlib.pyplot as plt

data_noInt = np.genfromtxt('../DataFiles_Fig4/NoInt_cal1_R0=3.0.avNE.severity.xls', skip_header = 1)
data_Int = np.genfromtxt('../DataFiles_Fig4/PC_CI_HQ_SD_cal1_R0=2.5.avNE.severity.xls', skip_header = 1)
data_Int2 = np.genfromtxt('../DataFiles_Fig4/PC_CI_HQ_SD_cal1_R0=3.0.avNE.severity.xls', skip_header = 1)
data_Int3 = np.genfromtxt('../DataFiles_Fig4/PC_CI_HQ_SD_cal1_R0=3.5.avNE.severity.xls', skip_header = 1)
data_Int4 = np.genfromtxt('../DataFiles_Fig4/PC_CI_HQ_SD_cal1_R0=4.0.avNE.severity.xls', skip_header = 1)
data_noInt_ad = np.genfromtxt('../DataFiles_Fig4/NoInt_cal1_R0=2.5.avNE.severity.adunit.xls', skip_header = 1)
data_Int_ad = np.genfromtxt('../DataFiles_Fig4/PC_CI_HQ_SD_cal1_R0=3.0.avNE.severity.adunit.xls', skip_header = 1)
data_Int2_ad = np.genfromtxt('../DataFiles_Fig4/PC_CI_HQ_SD_cal1_R0=3.0.avNE.severity.adunit.xls', skip_header = 1)
data_Int3_ad = np.genfromtxt('../DataFiles_Fig4/PC_CI_HQ_SD_cal1_R0=3.5.avNE.severity.adunit.xls', skip_header = 1)
data_Int4_ad = np.genfromtxt('../DataFiles_Fig4/PC_CI_HQ_SD_cal1_R0=4.0.avNE.severity.adunit.xls', skip_header = 1)

plt.plot(data_noInt[:,0], data_noInt[:,35] - data_noInt_ad[:,452],label='Do nothing - $R_0 = 3.0$',color='black',lw=1.5)
plt.plot(data_Int[:,0], data_Int[:,35] - data_Int_ad[:,452], label='PC_CI_HQ_SD - $R_0 = 2.5$',color='orange',lw=1.5)
plt.plot(data_Int2[:,0], data_Int2[:,35] - data_Int2_ad[:,452], label='PC_CI_HQ_SD - $R_0 = 3.0$',color='blue',lw=1.5)
plt.plot(data_Int3[:,0], data_Int3[:,35] - data_Int3_ad[:,452], label='PC_CI_HQ_SD - $R_0 = 3.5$',color='red',lw=1.5)
plt.plot(data_Int4[:,0], data_Int4[:,35] - data_Int4_ad[:,452], label='PC_CI_HQ_SD - $R_0 = 4.0$',color='purple',lw=1.5)

cumDe = np.genfromtxt('../EW_Scotland_Deaths.dat')

plt.scatter(cumDe[0,1],cumDe[0,2]+cumDe[0,3],color='black',s=15,label='Reported deaths')
for i in range(0,np.shape(cumDe[:,0])[0]):
  plt.scatter(cumDe[i,1],cumDe[i,2]+cumDe[i,3],color='black',s=15)

plt.yscale('log')

plt.xlabel('Time (day of year)',fontsize=12)
plt.ylabel('Cumulative deaths',fontsize=12)

#plt.title('UK - NI, calibration day 100')

plt.xlim(40.0, 200.0)
plt.ylim(100.0,100000.0)

plt.legend(loc='upper left',fontsize=8)

plt.tight_layout()

plt.savefig('cumul_Deaths_UK-NI_cal100.pdf',dpi=900)
plt.show()
