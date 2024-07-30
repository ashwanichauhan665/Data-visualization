import numpy as np

full_time_employees = np.array([
    [101, 'John Doe', 'Full-Time', 55000],
    [102, 'Jane Smith', 'Full-Time', 60000],
    [103, 'Mike Johnson', 'Full-Time', 52000]
])

part_time_employees = np.array([
    [201, 'Alice Brown', 'Part-Time', 25000],
    [202, 'Bob Wilson', 'Part-Time', 28000],
    [203, 'Emily Davis', 'Part-Time', 22000]
])

all_employees = np.vstack((full_time_employees, part_time_employees))

print("Combined Employee Data:")

# Print each employee's data
for employee in all_employees:
    print(f"Employee ID: {employee[0]} Name: {employee[1]} Type: {employee[2]} Salary: {employee[3]}")
