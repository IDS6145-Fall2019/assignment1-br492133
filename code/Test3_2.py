import matplotlib.pyplot as plt
import numpy as np
import sobol_seq

np.random.seed(71492)
data = np.random.randn(2, 100)
fig, ((ax1, ax3, ax5, ax7, ax9), (ax2, ax4, ax6, ax8, ax10)) = plt.subplots(2, 5)
fig.suptitle('Random Number Generators')

ax1.scatter(data[0],data[1], s=2)
ax1.set(title='N=100')
ax1.set_ylabel('Pseudo-Random')
ax1.set_yticklabels([])
ax1.set_xticklabels([])

np.random.seed(931682)
data2_1 = sobol_seq.i4_sobol_generate(1, 100)
data2_2 = data2_1[99:100]
data2_3 = data2_1[0:99]
data2_4 = np.concatenate((data2_2, data2_3))
ax2.scatter(data2_1, data2_4, s=1)
ax2.set_ylabel('Quasi-Random')
ax2.set_yticklabels([])
ax2.set_xticklabels([])

np.random.seed(19)
data = np.random.randn(2, 500)
ax3.scatter(data[0], data[1], s=2)
ax3.set(title='N=500')
ax3.set_yticklabels([])
ax3.set_xticklabels([])

np.random.seed(414219)
data = np.random.randn(2, 500)
data4_1 = sobol_seq.i4_sobol_generate(1, 500)
data4_2 = data4_1[99:500]
data4_3 = data4_1[0:99]
data4_4 = np.concatenate((data4_2, data4_3))
ax4.scatter(data4_1, data4_4, s=1)
ax4.set_yticklabels([])
ax4.set_xticklabels([])

np.random.seed(1241)
data = np.random.randn(2, 1000)
ax5.scatter(data[0], data[1], s=2)
ax5.set(title='N=1000')
ax5.set_yticklabels([])
ax5.set_xticklabels([])

np.random.seed(419821)
data = np.random.randn(2, 1000)
data6_1 = sobol_seq.i4_sobol_generate(1, 1000)
data6_2 = data6_1[99:1000]
data6_3 = data6_1[0:99]
data6_4 = np.concatenate((data6_2, data6_3))
ax6.scatter(data6_1, data6_4, s=1)
ax6.set_yticklabels([])
ax6.set_xticklabels([])

np.random.seed(11454)
data = np.random.randn(2, 2000)
ax7.scatter(data[0], data[1], s=2)
ax7.set(title='N=2000')
ax7.set_yticklabels([])
ax7.set_xticklabels([])

np.random.seed(154143)
data = np.random.randn(2, 2000)
data8_1 = sobol_seq.i4_sobol_generate(1, 2000)
data8_2 = data8_1[99:2000]
data8_3 = data8_1[0:99]
data8_4 = np.concatenate((data8_2, data8_3))
ax8.scatter(data8_1, data8_4, s=1)
ax8.set_yticklabels([])
ax8.set_xticklabels([])

np.random.seed(11454)
data = np.random.randn(2, 5000)
ax9.scatter(data[0], data[1], s=2)
ax9.set(title='N=5000')
ax9.set_yticklabels([])
ax9.set_xticklabels([])

np.random.seed(154143)
data = np.random.randn(2, 5000)
data10_1 = sobol_seq.i4_sobol_generate(1, 5000)
data10_2 = data10_1[99:5000]
data10_3 = data10_1[0:99]
data10_4 = np.concatenate((data10_2, data10_3))
ax10.scatter(data10_1, data10_4, s=1)
ax10.set_yticklabels([])
ax10.set_xticklabels([])


plt.show()
