import numpy as np
customer_ids = np.array([101, 102, 103, 104, 105, 106, 107, 108, 109, 110])
last_purchase_days_ago = np.array([5, 15, 20, 25, 30, 35, 40, 45, 50, 55])

less_30 = last_purchase_days_ago <= 30
greater_30 = last_purchase_days_ago > 30

costomer_less30 = customer_ids[less_30]
costomer_greater30 = customer_ids[greater_30]


print("Active customers (Last purchase <= 30 days ago)")
print(costomer_less30)
print("Active customers (Last purchase > 30 days ago)")
print(costomer_greater30)