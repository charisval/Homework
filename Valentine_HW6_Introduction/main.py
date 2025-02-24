"""
Name: Charis Valentine
Date: 2/24/25
Homework: Python introduction
Description: This program collects two number inputs, runs arithmetic calculations, and prints the answers. 
"""

# numbers are collected using the input function
num1 = input("What is your first number? ")
num2 = input("What is your second number? ")

# all variables are converted to integers using the int function
sum = int(num1) + int(num2)
diff = int(num1) - int(num2)
power = int(num1)**int(num2)
divide = int(num1)//int(num2)
mod = int(num1)%int(num2)

# calculations are printed using the variables
print()
print(f"The sum of {num1} and {num2} is {sum}")
print(f"The difference between {num1} and {num2} is {diff}")
print(f"{num1} to the power of {num2} is {power}")
print(f"{num1} divided by {num2} is {divide}. The remainder is {mod}")