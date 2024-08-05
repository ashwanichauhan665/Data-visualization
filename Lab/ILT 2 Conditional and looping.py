#Question 1: Python program to check leap year
# Get the year from the user
year = int(input("Enter a year: "))

# Check if the year is a leap year
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")





# Question 2. Python Program to Find the Largest Among Three Numbers
# Get the three numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# Find the largest number
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

# Print the largest number
print(f"The largest number is: {largest}")




# Question 3. Python Program to Check if a Number is Positive, Negative or 0
# Get the number from the user
num = int(input("Enter a number: "))

# Check if the number is positive, negative, or 0
if num > 0:
    print(f"{num} is a positive number.")
elif num < 0:
    print(f"{num} is a negative number.")
else:
    print(f"{num} is zero.")





# Question 4. A toy vendor supplies three types of toys: Battery Based Toys, Key-based Toys, and Electrical Charging Based Toys. The vendor gives a discount of 10% on orders for battery-based toys if the order is for more than Rs. 1000. On orders of more than Rs. 100 for key-based toys, a discount of 5% is given, and a discount of 10% is given on orders for electrical charging based toys of value more than Rs. 500. Assume that the numeric codes 1,2 and 3 are used for battery based toys, key-based toys, and electrical charging based toys respectively. Write a program that reads the product code and the order amount and prints out the net amount that the customer is required to pay after the discount.
# Define the discount rules
discount_rules = {
    1: {"min_amount": 1000, "discount": 0.10},  # Battery Based Toys
    2: {"min_amount": 100, "discount": 0.05},   # Key-based Toys
    3: {"min_amount": 500, "discount": 0.10}    # Electrical Charging Based Toys
}

# Get the product code and order amount from the user
product_code = int(input("Enter the product code (1/2/3): "))
order_amount = float(input("Enter the order amount: "))

# Check if the product code is valid
if product_code not in discount_rules:
    print("Invalid product code. Please try again.")
else:
    # Calculate the discount
    discount_rule = discount_rules[product_code]
    if order_amount > discount_rule["min_amount"]:
        discount = order_amount * discount_rule["discount"]
    else:
        discount = 0

    # Calculate the net amount
    net_amount = order_amount - discount

    # Print the result
    print(f"Net amount to pay: Rs. {net_amount:.2f}")
    print(f"Discount: Rs. {discount:.2f}")





# Question 5. A transport company charges the fare according to following table: Distance Charges 1-50 8 Rs./Km 51-100 10 Rs./Km> 100 12 Rs/Km
# Define the fare rules
fare_rules = [
    {"min_distance": 0, "max_distance": 50, "fare_per_km": 8},
    {"min_distance": 51, "max_distance": 100, "fare_per_km": 10},
    {"min_distance": 101, "max_distance": float("inf"), "fare_per_km": 12}
]

# Get the distance from the user
distance = float(input("Enter the distance traveled (in km): "))

# Calculate the fare
fare = 0
for rule in fare_rules:
    if rule["min_distance"] <= distance <= rule["max_distance"]:
        fare = distance * rule["fare_per_km"]
        break

# Print the result
print(f"Fare: Rs. {fare:.2f}")







# Question 6. Write a python program to reverse a number using a while loop.
# Get the number from the user
num = int(input("Enter a number: "))

# Initialize the reversed number
reversed_num = 0

# Use a while loop to reverse the number
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

# Print the reversed number
print("Reversed number:", reversed_num)





# Question 7. Write a python program to check whether a number is palindrome or not?
# Get the number from the user
num = int(input("Enter a number: "))

# Convert the number to a string to easily reverse it
num_str = str(num)

# Check if the number is a palindrome
if num_str == num_str[::-1]:
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
    






# Question 8. Write a python program finding the factorial of a given number usinga while loop.
# Get the number from the user
num = int(input("Enter a number: "))

# Initialize the factorial
factorial = 1

# Use a while loop to calculate the factorial
i = 1
while i <= num:
    factorial *= i
    i += 1

# Print the factorial
print(f"The factorial of {num} is {factorial}.")







# Question 9. Accept numbers using input() function until the user enters 0. If user
# input 0 then break the while loop and display the sum of all the number

# Initialize the sum to 0
total_sum = 0

# Use a while loop to accept numbers until the user enters 0
while True:
    num = int(input("Enter a number (0 to quit): "))
    if num == 0:
        break
    total_sum += num

# Display the sum of all the numbers
print(f"The sum of all the numbers is: {total_sum}")







# Question 10. Print the first 10 natural numbers using for loop
# Use a for loop to print the first 10 natural numbers
for i in range(1, 11):
    print(i)




# Question 11. Python program to check if the given string is a palindrome
input_str = input("Enter a string: ")
input_str = input_str.lower()  # Convert to lowercase for case-insensitive comparison

if input_str == input_str[::-1]:  # Compare the string with its reverse
    print(f"'{input_str}' is a palindrome.")
else:
    print(f"'{input_str}' is not a palindrome.")






# Question 12. Python program to check if a given number is an Armstrong number
num = int(input("Enter a number: "))
num_str = str(num)
num_digits = len(num_str)
sum_of_digits = sum(int(digit) ** num_digits for digit in num_str)

if sum_of_digits == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")






# Question 13. Python program to get the Fibonacci series between 0 to 50
a, b = 0, 1
print("Fibonacci series between 0 to 50:")
while a <= 50:
    print(a, end=" ")
    a, b = b, a + b




# Question 14. Python program to check the validity of password input by users
password = input("Enter a password: ")

if len(password) < 8:
    print("Password is not valid. It should be at least 8 characters long.")
elif not any(char.isupper() for char in password):
    print("Password is not valid. It should have at least one uppercase letter.")
elif not any(char.islower() for char in password):
    print("Password is not valid. It should have at least one lowercase letter.")
elif not any(char.isdigit() for char in password):
    print("Password is not valid. It should have at least one digit.")
elif not any(not char.isalnum() for char in password):
    print("Password is not valid. It should have at least one special character.")
else:
    print("Password is valid.")
