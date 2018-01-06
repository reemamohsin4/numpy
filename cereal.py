import codecademylib
from matplotlib import pyplot as plt
import numpy as np

calorie_stats = np.genfromtxt('cereal.csv',delimiter=',')
average_calorie = np.mean(calorie_stats)
print average_calorie
#the average calorie count for other cereal brands is much higher than CrunchieMunchies, 106.88 vs 70

print np.sort(calorie_stats)

median_calorie = np.median(calorie_stats)
print median_calorie

print np.percentile(calorie_stats,18)
high_calorie = 100-18
print high_calorie

calorie_std = np.std(calorie_stats)
print calorie_std

#Our findings show that, on average, competing cereal brands have a much higher calorie count than CrunchieMunchies. In fact, of all the brands tested, 82% of them have a calorie count of 100 or more calories per serving. CrunchieMunchies is only 70 calories per serving. This cereal brand could appeal to consumers by being marketed as one of the healthiest cereal brands on the market.
