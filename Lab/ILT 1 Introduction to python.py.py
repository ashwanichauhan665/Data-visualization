#Question 1 : Using input() function take one number from the user and using ternary operators check whether the number is even or odd

# Get user input
num = int(input("Enter a number: "))

# Use ternary operator to determine if the number is even or odd
result = "Even" if num % 2 == 0 else "Odd"

# Print the result
print(f"The number {num} is {result}.")








#Question 2: Using input function take two number and then swap the number
# Get two numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Print the original numbers
print(f"Original numbers: num1 = {num1}, num2 = {num2}")
# Swap the numbers using a temporary variable
temp = num1
num1 = num2
num2 = temp

# Print the swapped numbers
print(f"Swapped numbers: num1 = {num1}, num2 = {num2}")





#Question 3. Write a Program to Convert Kilometers to Miles

# Define a function to convert kilometers to miles
def km_to_miles(km):
    miles = km * 0.621371  # 1 kilometer is approximately 0.621371 miles
    return miles

# Get the distance in kilometers from the user
km = float(input("Enter a distance in kilometers: "))

# Convert the distance to miles
miles = km_to_miles(km)

# Print the result
print(f"{km} kilometers is approximately {miles:.2f} miles.")







# Question 4. Find the Simple Interest on Rs. 200 for 5 years at 5% per year
# Define the principal amount, interest rate, and time period
principal = 200
interest_rate = 5 / 100  # 5% as a decimal
time_period = 5  # in years

# Calculate the simple interest
simple_interest = (principal * interest_rate * time_period)

# Calculate the total amount
total_amount = principal + simple_interest

# Print the results
print("Simple Interest Calculator")
print(f"Principal Amount: Rs. {principal}")
print(f"Interest Rate: {interest_rate*100}% per year")
print(f"Time Period: {time_period} years")
print(f"Simple Interest: Rs. {simple_interest:.2f}")
print(f"Total Amount: Rs. {total_amount:.2f}")