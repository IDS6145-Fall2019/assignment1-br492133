import matplotlib.pyplot as plt
import numpy as np
import sobol_seq

np.random.seed(71492)
fig, ((ax1, ax4, ax7, ax10, ax13), (ax2, ax5, ax8, ax11, ax14), (ax3, ax6, ax9, ax12, ax15)) = plt.subplots(3, 5)
fig.suptitle('1D Random Distributions Generators')

n_bins = 35

#___________________________________
#Normal Dist
np.random.seed(4689136)
data1 = np.random.normal(loc=0.0, scale=1.0, size=(100,1))
ax1.hist(data1, bins=n_bins)
ax1.set(title='N=100')
ax1.set_ylabel('Standard Normal')
ax1.set_yticklabels([])
ax1.set_xticklabels([])

print("check")


np.random.seed(78712)
data4 = np.random.normal(loc=0.0, scale=1.0, size=(500,1))
ax4.hist(data4, bins=n_bins)
ax4.set(title='N=500')
ax4.set_yticklabels([])
ax4.set_xticklabels([])

print("check2")

np.random.seed(409756)
data7 = np.random.normal(loc=0.0, scale=1.0, size=(1000,1))
ax7.hist(data7, bins=n_bins)
ax7.set(title='N=1000')
ax7.set_yticklabels([])
ax7.set_xticklabels([])

print("check3")

np.random.seed(170436)
data10 = np.random.normal(loc=0.0, scale=1.0, size=(2000,1))
ax10.hist(data10, bins=n_bins)
ax10.set(title='N=2000')
ax10.set_yticklabels([])
ax10.set_xticklabels([])

print("check4")

np.random.seed(64701236)
data13 = np.random.normal(loc=0.0, scale=1.0, size=(5000,1))
ax13.hist(data13, bins=n_bins)
ax13.set(title='N=5000')
ax13.set_yticklabels([])
ax13.set_xticklabels([])

print("check5")

#-----------------------------
#Exponential Dist

np.random.seed(8973215)
data2 = np.random.normal(scale=1.0, size=(100,1))
ax2.hist(data2, bins=n_bins)
ax2.set_ylabel('Exponential')
ax2.set_yticklabels([])
ax2.set_xticklabels([])

print("check6")

np.random.seed(9387314)
data5 = np.random.normal(scale=1.0, size=(500,1))
ax5.hist(data5, bins=n_bins)
ax5.set_yticklabels([])
ax5.set_xticklabels([])

print("check7")

np.random.seed(1981)
data8 = np.random.normal(scale=1.0, size=(1000,1))
ax8.hist(data8, bins=n_bins)
ax8.set_yticklabels([])
ax8.set_xticklabels([])

print("check8")

np.random.seed(107429)
data11 = np.random.normal(scale=1.0, size=(2000,1))
ax11.hist(data11, bins=n_bins)
ax11.set_yticklabels([])
ax11.set_xticklabels([])

print("check9")

np.random.seed(1892742)
data14 = np.random.normal(scale=1.0, size=(5000,1))
ax14.hist(data14, bins=n_bins)
ax14.set_yticklabels([])
ax14.set_xticklabels([])

print("check10")
#________________________________________
#Uniform Dist

np.random.seed(18721451)
data3 = np.random.uniform(-1,1, size = (100,1))
ax3.hist(data3, bins=n_bins)
ax3.set_ylabel('Uniform')
ax3.set_yticklabels([])
ax3.set_xticklabels([])

print("check11")

np.random.seed(7162498)
data6 = np.random.uniform(-1,1, size = (500,1))
ax6.hist(data3, bins=n_bins)
ax6.set_yticklabels([])
ax6.set_xticklabels([])

print("check12")

np.random.seed(4170189256)
data9 = np.random.uniform(-1,1, size = (1000,1))
ax9.hist(data9, bins=n_bins)
ax9.set_yticklabels([])
ax9.set_xticklabels([])

print("check13")

np.random.seed(12897150)
data12 = np.random.uniform(-1,1, size = (2000,1))
ax12.hist(data12, bins=n_bins)
ax12.set_yticklabels([])
ax12.set_xticklabels([])

print("check14")

np.random.seed(8309174)
data15 = np.random.uniform(-1,1, size =(5000,1))
ax15.hist(data15, bins=n_bins)
ax15.set_yticklabels([])
ax15.set_xticklabels([])

print("check15")
#---------------------------------

plt.show()
