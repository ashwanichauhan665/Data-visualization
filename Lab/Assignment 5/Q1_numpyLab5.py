import numpy as np

temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2])

hot_days_mask = temperatures > 35
cold_days_mask = temperatures < 5

hot_days = np.where(hot_days_mask)[0]+1
cold_days = np.where(cold_days_mask)[0]+1


extreme_temperatures = temperatures[hot_days-1]
cold_temp = temperatures[cold_days-1]

print("days:", *hot_days)
print("Temperatures on  temperature days:", *extreme_temperatures)

print("days:", *cold_days)
print("Temperatures on Low temperature days:", *cold_temp)


