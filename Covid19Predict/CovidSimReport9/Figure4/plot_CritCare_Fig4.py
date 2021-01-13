import math
import numpy as np
import matplotlib.pyplot as plt

data_noInt = np.genfromtxt('../DataFiles_Fig4/NoInt_cal1_R0=3.0.avNE.severity.xls', skip_header = 1)
data_Int = np.genfromtxt('../DataFiles_Fig4/PC_CI_HQ_SD_cal1_R0=2.5.avNE.severity.xls', skip_header = 1)
data_Int2 = np.genfromtxt('../DataFiles_Fig4/PC_CI_HQ_SD_cal1_R0=3.0.avNE.severity.xls', skip_header = 1)
data_Int3 = np.genfromtxt('../DataFiles_Fig4/PC_CI_HQ_SD_cal1_R0=3.5.avNE.severity.xls', skip_header = 1)
data_Int4 = np.genfromtxt('../DataFiles_Fig4/PC_CI_HQ_SD_cal1_R0=4.0.avNE.severity.xls', skip_header = 1)

data_noInt_ad = np.genfromtxt('../DataFiles_Fig4/NoInt_cal1_R0=3.0.avNE.severity.adunit.xls', skip_header = 1)
data_Int_ad = np.genfromtxt('../DataFiles_Fig4/PC_CI_HQ_SD_cal1_R0=2.5.avNE.severity.adunit.xls', skip_header = 1)
data_Int2_ad = np.genfromtxt('../DataFiles_Fig4/PC_CI_HQ_SD_cal1_R0=3.0.avNE.severity.adunit.xls', skip_header = 1)
data_Int3_ad = np.genfromtxt('../DataFiles_Fig4/PC_CI_HQ_SD_cal1_R0=3.5.avNE.severity.adunit.xls', skip_header = 1)
data_Int4_ad = np.genfromtxt('../DataFiles_Fig4/PC_CI_HQ_SD_cal1_R0=4.0.avNE.severity.adunit.xls', skip_header = 1)

plt.plot(data_noInt[:,0], (data_noInt[:,13]-data_noInt_ad[:,78])/652.0,label='Do nothing - $R_0 = 3.0$',color='black',lw=2.0)
plt.plot(data_Int[:,0], (data_Int[:,13]-data_Int_ad[:,78])/652.0, label='PC_CI_HQ_SD - $R_0 = 2.5$',color='orange',lw=2.0)
plt.plot(data_Int2[:,0], (data_Int2[:,13]-data_Int2_ad[:,78])/652.0, label='PC_CI_HQ_SD - $R_0 = 3.0$',color='blue',lw=2.0)
plt.plot(data_Int3[:,0], (data_Int3[:,13]-data_Int3_ad[:,78])/652, label='PC_CI_HQ_SD - $R_0 = 3.5$',color='red',lw=2.0)
plt.plot(data_Int4[:,0], (data_Int4[:,13]-data_Int4_ad[:,78])/652, label='PC_CI_HQ_SD - $R_0 = 4.0$',color='purple',lw=2.0)

plt.xlabel('Time (day of year)',fontsize=12)
plt.ylabel('Critical care beds occupied per 100000',fontsize=12)

plt.xlim(0.0, 350.0)
plt.ylim(0.0,150.0)

plt.legend(loc='upper left',fontsize=7)

plt.tight_layout()

plt.savefig('CritCare_UK-NI_cal100.pdf',dpi=900)
plt.show()
