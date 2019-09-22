import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import csv
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


d = pd.read_csv('MTA_Stations_Data1.csv')
df_all = pd.DataFrame(d)
df_all
print(df_all)
print(df_all.describe())

print("\n"
      "Top 10 Subway Stations""\n"
      "Means:")
df_1_10 = df_all[0:10]
Average1_10 = df_1_10.mean()
print(Average1_10)
print("Standard Deviations:")
StandardDev1_10 = df_1_10.std()
print(StandardDev1_10)

print("\n"
      "Top 11-20 Subway Stations""\n"
      "Means:")
df_11_20 = df_all[11:20]
Average11_20 = df_11_20.mean()
print(Average11_20)
print("Standard Deviations:")
StandardDev11_20 = df_11_20.std()
print(StandardDev11_20)

print("\n"
      "Top 21-30 Subway Stations""\n"
      "Means:")
df_21_30 = df_all[21:30]
Average21_30 = df_21_30.mean()
print(Average21_30)
print("Standard Deviations:")
StandardDev21_30 = df_21_30.std()
print(StandardDev21_30)

print("\n"
      "Top 31-40 Subway Stations" "\n"
      "Means:")
df_31_40 = df_all[31:40]
Average31_40 = df_31_40.mean()
print(Average31_40)
print("Standard Deviations:")
StandardDev31_40 = df_31_40.std()
print(StandardDev31_40)

print("\n"
      "Top 41-50 Subway Stations" "\n"
      "Means:")
df_41_50 = df_all[41:50]
Average41_50 = df_41_50.mean()
print(Average41_50)
print("Standard Deviations:")
StandardDev41_50 = df_41_50.std()
print(StandardDev41_50)
print("\n")




import numpy as np
import matplotlib.pyplot as plt

# data to plot
n_groups = 5
Average_2017_Weekday = (73529, 31399, 24764, 20418, 16476)
Average_2017_Weekend = (68601, 33994, 25303, 20263, 17630)
Average_2017_Day = (72120, 32140, 24918, 20373, 16805)

# create plot
fig1, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.2
opacity = 0.8

rects1 = plt.bar(index, Average_2017_Weekday, bar_width,
alpha=opacity,
color='b',
label='Average 2017 Weekday')

rects2 = plt.bar(index + bar_width, Average_2017_Weekend, bar_width,
alpha=opacity,
color='g',
label='Average 2017 Weekend')

rects3 = plt.bar(index + bar_width + bar_width, Average_2017_Day, bar_width,
alpha=opacity,
color='r',
label='Average 2017 Day')

plt.xlabel('Station Grouping')
plt.ylabel('Number of Riders')
plt.title('Ridership by Top NY Subway Station Groups')
plt.xticks(index + bar_width, ('Top 1-10', 'Top 11-20', 'Top 21-30', 'Top 31-40', 'Top 41-50'))
plt.legend()

plt.tight_layout()

n_groups = 5
Std_2017_Weekday = (27146, 4601, 1837, 3343, 1199)
Std_2017_Weekend = (40925, 11714, 3895, 5238, 2876)
Std_2017_Day = (29222, 6122, 886, 1709, 730)

# create plot
fig2, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.2
opacity = 0.8

rects1 = plt.bar(index, Std_2017_Weekday, bar_width,
alpha=opacity,
color='b',
label='Std. Dev. of 2017 Weekday')

rects2 = plt.bar(index + bar_width, Std_2017_Weekend, bar_width,
alpha=opacity,
color='g',
label='Std. Dev. of 2017 Weekend')

rects3 = plt.bar(index + bar_width + bar_width, Std_2017_Day, bar_width,
alpha=opacity,
color='r',
label='Std. Dev. of 2017 Day')

plt.xlabel('Station Grouping')
plt.ylabel('Number of Riders')
plt.title('Standard Deviation of Ridership by Top NY Subway Station Groups')
plt.xticks(index + bar_width, ('Top 1-10', 'Top 11-20', 'Top 21-30', 'Top 31-40', 'Top 41-50'))
plt.legend()

plt.tight_layout()
plt.show()