import numpy as np
monthly_sales = np.array([120, 135, 148, 165, 180, 155, 168, 190, 205, 198, 210, 225])
arr = np.split(monthly_sales,4)
j=0
for i in arr:
    print(f"Quarter {j} sales (in terms of thousands)")
    print(*i)
    j+=1
