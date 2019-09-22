import matplotlib.pyplot as plt
import numpy as np
import sobol_seq

np.random.seed(71492)
fig, ((ax1, ax4, ax7, ax10, ax13)) = plt.subplots(1, 5)
fig.suptitle('Quasi-Random Distributions Generators')

n_bins = 35

#___________________________________
#Normal Dist
np.random.seed(4689136)

np.random.seed(931682)
data1_1 = sobol_seq.i4_sobol_generate(1, 100)
ax1.hist(data1_1, bins=n_bins)
ax1.set_ylabel('Quasi-Random')
ax1.set(title='N=100')
ax1.set_yticklabels([])
ax1.set_xticklabels([])

print("check")


np.random.seed(78712)
data4_1 = sobol_seq.i4_sobol_generate(1, 500)
ax4.hist(data4_1, bins=n_bins)
ax4.set(title='N=500')
ax4.set_yticklabels([])
ax4.set_xticklabels([])

print("check2")

np.random.seed(409756)
data7_1 = sobol_seq.i4_sobol_generate(1, 1000)
ax7.hist(data7_1, bins=n_bins)
ax7.set(title='N=1000')
ax7.set_yticklabels([])
ax7.set_xticklabels([])

print("check3")

np.random.seed(170436)
data10_1 = sobol_seq.i4_sobol_generate(1, 2000)
ax10.hist(data10_1, bins=n_bins)
ax10.set(title='N=2000')
ax10.set_yticklabels([])
ax10.set_xticklabels([])

print("check4")

np.random.seed(64701236)
data13_1 = sobol_seq.i4_sobol_generate(1, 5000)
ax13.hist(data13_1, bins=n_bins)
ax13.set(title='N=5000')
ax13.set_yticklabels([])
ax13.set_xticklabels([])

print("check5")
#---------------------------------

plt.show()
