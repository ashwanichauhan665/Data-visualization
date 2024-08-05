# 1. Write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen.
file = open("ABC.txt", 'w')
file.write("Clouds drifted lazily across the sky, obscuring the moon's glow.\n")
file.write("The sun set over the horizon, painting the sky with hues of orange and pink.\n")
file.write("Beneath the stars, a quiet serenity embraced the night.\n")
file.write("Tiny droplets of rain began to fall, tapping softly on the windowpane.\n")
file.write("Time seemed to stand still as the world was enveloped in the tranquility of twilight.\n")
file.write("Thunder rumbled in the distance, heralding the arrival of a summer storm.\n")
file.close()





# 2. Write a function in Python to count and display the total number of words in a textfile “ABC.txt”
def reading (fil):
    file=open(fil, 'r')
    for line in file:
        print(line.strip())
    file.close()
reading('ABC.txt')




# 3. Write a function in Python to count uppercase character in a text file “ABC.txt”
def count_uppercase(fil):
    file=open(fil, 'r')
    text = file.read()
    uppercase_count = sum(1 for char in text if char.isupper())
    print("Total uppercase characters in file ",uppercase_count)
count_uppercase('ABC.txt')






# 4. Write a function display_words() in python to read lines from a text file "story.txt",and display those words, which are less than 4 characters.
file = open("story.txt", 'w')
file.write("Clouds drifted lazily across the sky, obscuring the moon's glow.\n")
file.write("The sun set over the horizon, painting the sky with hues of orange and pink.\n")
file.write("Beneath the stars, a quiet serenity embraced the night.\n")
file.write("Tiny droplets of rain began to fall, tapping softly on the windowpane.\n")
file.write("Time seemed to stand still as the world was enveloped in the tranquility of twilight.\n")
file.write("Thunder rumbled in the distance, heralding the arrival of a summer storm.\n")
file.close()

def display_words(file_name):
    file=open(file_name, 'r')
    for line in file:
        words = line.split()
        for word in words:
            if len(word) < 4:
                print(word)


# Example usage:
display_words('story.txt')





# Assignment:

# 1. Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
def div(a,b):
    result=a/b
    print(result)
try:
    div(10,0)
except ZeroDivisionError as e :
    print("ZERO DIVISION ERROR ENCOUNTERED")




# 2. Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
try:
    num=int(input("ENTER A NUMBER: "))
except ValueError as v:
    print("VALUE ERROR ENCOUNTERED")




# 3. Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.
try:
    open("anudip.txt")
except FileNotFoundError as f:
    print("FILE NOT FOUND ERROR ENCOUNTERED")



# 4. Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical
try:
    num1 = float(input("Enter the first number: "))
except ValueError:
    raise TypeError("Invalid input. Please enter a numerical value.")
try:
    num2 = float(input("Enter the second number: "))
except ValueError:
    raise TypeError("Invalid input. Please enter a numerical value.")




