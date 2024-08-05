# Assignment:

# 1. Write a Python program to sum all the items in a list.
numbers = [1, 2, 3, 4, 5]
sum_of_numbers = sum(numbers)
print("The sum of the numbers is:", sum_of_numbers)





# 2. Write a Python program to get the largest and smallest number from a list without builtin functions.
numbers = [12, 45, 7, 23, 56, 89, 34]
largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Largest number is:", largest)
print("Smallest number is:", smallest)





# 3. Write a Python program to find duplicate values from a list and display those.
numbers = [1, 2, 3, 4, 2, 7, 8, 8, 9]

duplicates = []
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j] and numbers[i] not in duplicates:
            duplicates.append(numbers[i])

if duplicates:
    print("Duplicate values are:", duplicates)
else:
    print("No duplicate values found.")





# 4. Write a Python program to split a given list into two parts where the length of the first
# part of the list is given.
# Original list:
# [1, 1, 2, 3, 4, 4, 5, 1]
# Length of the first part of the list: 
# Splitted the said list into two parts:
# ([1, 1, 2], [3, 4, 4, 5, 1])
original_list = [1, 1, 2, 3, 4, 4, 5, 1]
first_part_length = 3

first_part = original_list[:first_part_length]
second_part = original_list[first_part_length:]

print("Original list:", original_list)
print("Splitted list:", (first_part, second_part))








# 5. Write a Python program to traverse a given list in reverse order, and print the elements with the original index.
# Original list:
# ['red', 'green', 'white', 'black']
# Traverse the said list in reverse order:
# black
# white
# green
# red
original_list = ['red', 'green', 'white', 'black']

print("Original list:", original_list)

for i in range(len(original_list) - 1, -1, -1):
    print(original_list[i])







# Assignment:

# 1. Write a Python program and calculate the mean of the below dictionary.
# test_dict = {"A" : 6, "B" : 9, "C" : 5, "D" : 7, "E" : 4}
# Output: 6.2

test_dict = {"A": 6, "B": 9, "C": 5, "D": 7, "E": 4}

# Calculate the mean
mean = sum(test_dict.values()) / len(test_dict)

print("Mean:", mean)








# 2.Write a Python script to concatenate the following dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
new_dict = {**dic1, **dic2, **dic3}
print("Concatenated Dictionary:", new_dict)





# 3.Write a Python program to get the key, value and item in a dictionary.
# input:dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# Output:
# Key 	Value
# 1	10
# 2	20
# 3	30
# 4	40
# 5	50
# 6	60

dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print("Key\tValue")
for key, value in dict_num.items():
    print(f"{key}\t{value}")






# 4.Write a Python program to get the key, value and item in a dictionary.
# Input: input_dict = {1: 10, 2: 20, 3:None, 4: 40, 5: None, 6: 60}
# Output:
# dict with empty items Dropped :
# {1:10,2:40,4:40,6:60}
input_dict = {1: 10, 2: 20, 3: None, 4: 40, 5: None, 6: 60}
output_dict = {key: value for key, value in input_dict.items() if value is not None}
print("dict with empty items Dropped :")
print(output_dict)





# 1. Write a Python program to find the number of times 4 appears in the tuple.
# Input:
# tuplex = (2, 4, 5, 6, 2, 3, 4, 4, 7 )
# Output: 3

tuplex = (2, 4, 5, 6, 2, 3, 4, 4, 7)
count = tuplex.count(4)
print("The number 4 appears", count, "times in the tuple.")




# 2.Write a Python program to convert a list to a tuple.
# Input: listx = [5, 10, 7, 4, 15, 3]
# Output: (5, 10, 7, 4, 15, 3)
listx = [5, 10, 7, 4, 15, 3]
tuplex = tuple(listx)
print(tuplex)





# 3. Write a Python program to calculate the sum of the numbers in a given tuple.
# Input: tuples_list = [(1, 2), (3, 4), (5, 6)]
# Output:
# sum of tuple is : 21
# Define the employee tuples
tuples_list = [(1, 2), (3, 4), (5, 6)]
total_sum = sum(num for tup in tuples_list for num in tup)
print("sum of tuple is :", total_sum)







# 4.Write a python program and iterate the given tuples
# Input:
# employee1 = ("John Doe", 101, "Human Resources", 60000)
# employee2 = ("Alice Smith", 102, "Marketing", 55000)
# employee3 = ("Bob Johnson", 103, "Engineering", 75000)
# Output:
# Employee Records :
# Name : John Doe
# Employee ID : 101
# Department : Human Resources
# Salary	:  60000
# Name : Alice Smith
# Employee ID : 102
# Department :Marketing
# Salary	:  55000
# Name : Bob Johnson
# Employee ID : 103
# Department : Engineering
# Salary	:  75000
employee1 = ("John Doe", 101, "Human Resources", 60000)
employee2 = ("Alice Smith", 102, "Marketing", 55000)
employee3 = ("Bob Johnson", 103, "Engineering", 75000)
employees = [employee1, employee2, employee3]
print("Employee Records :")

for employee in employees:
    name, employee_id, department, salary = employee
    print("\nName : ", name)
    print("Employee ID : ", employee_id)
    print("Department : ", department)
    print("Salary : ", salary)



# Assignment:
# 1. Write a Python program to Get Only unique items from two sets.
# Input:
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# Output:{70, 40, 10, 50, 20, 60, 30}
# Define the input sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
unique_items = set1.union(set2)
print(unique_items)





# 2. Write a Python program to Return a set of elements present in Set A or B, but not both.
# Input:
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# Output:{20, 70, 10, 60}
# Define the input sets

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
result = set1.symmetric_difference(set2)
print(result)



# 3. Write a Python program to Check if two sets have any elements in common. If yes, display the common elements.
# Input:
# set1 = {10, 20, 30, 40, 50}
# set2 = {60, 70, 80, 90, 10}
# Output: {10}
# Define the input sets
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
if set1.intersection(set2):
    print("The sets have common elements:")
    print(set1.intersection(set2))
else:
    print("The sets have no common elements.")






# 3. Write a Python program to Remove items from set1 that are not common to both set1 and set2.
# Input:
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# Output: {40, 50, 30}
# Define the input sets

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set1.intersection_update(set2)
print(set1)

