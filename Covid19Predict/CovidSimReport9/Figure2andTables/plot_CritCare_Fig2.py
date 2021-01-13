import math
import numpy as np
import matplotlib.pyplot as plt

data_noInt = np.genfromtxt('../DataFiles_Fig2/NoInt_R0=2.4.avNE.severity.xls', skip_header = 1)
data_Int = np.genfromtxt('../DataFiles_Fig2/PC_100_91_R0=2.4.avNE.severity.xls', skip_header = 1)
data_Int1 = np.genfromtxt('../DataFiles_Fig2/CI_100_91_R0=2.4.avNE.severity.xls',skip_header=1)
data_Int2 = np.genfromtxt('../DataFiles_Fig2/CI_HQ_100_91_R0=2.4.avNE.severity.xls', skip_header = 1)
data_Int3 = np.genfromtxt('../DataFiles_Fig2/CI_HQ_SDOL70_100_91_R0=2.4.avNE.severity.xls', skip_header = 1)
data_Int4 = np.genfromtxt('../DataFiles_Fig2/CI_SD_100_91_R0=2.4.avNE.severity.xls', skip_header = 1)
data_Int5 = np.genfromtxt('../DataFiles_Fig2/CI_HQ_SD_100_91_R0=2.4.avNE.severity.xls', skip_header = 1)
data_Int6 = np.genfromtxt('../DataFiles_Fig2/PC_CI_HQ_SDOL70_100_91_R0=2.4.avNE.severity.xls', skip_header = 1)

plt.plot(data_noInt[:,0], data_noInt[:,13]/652,label='Do nothing',color='black',lw=1.8)
plt.plot(data_Int[:,0], data_Int[:,13]/652, label='PC',color='orange',lw=1.8)
plt.plot(data_Int1[:,0], data_Int1[:,13]/652, label='CI',color='blue',lw=1.8)
plt.plot(data_Int2[:,0], data_Int2[:,13]/652, label='CI_HQ',color='red',lw=1.8)
plt.plot(data_Int3[:,0], data_Int3[:,13]/652, label='CI_HQ_SDOL70',color='purple',lw=1.8)
plt.plot(data_Int4[:,0], data_Int4[:,13]/652, label='CI_SD',color='brown',lw=1.8,ls='dashed')
plt.plot(data_Int5[:,0], data_Int5[:,13]/652, label='CI_HQ_SD',color='pink',lw=1.8,ls='dashed')
plt.plot(data_Int6[:,0], data_Int6[:,13]/652, label='PC_CI_HQ_SDOL70',color='grey',lw=1.8,ls='dashed')

plt.xlabel('Time (day of year)',fontsize=11)
plt.ylabel('Critical care beds occupied per 100000',fontsize=11)

plt.title('$R_0 = 2.4$')

plt.xlim(50.0, 350.0)
plt.ylim(0.0,300.0)

plt.legend(loc='upper right',fontsize=8)

plt.tight_layout()

plt.savefig('Figure2_report9.pdf',dpi=900)
plt.show()
