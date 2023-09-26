#!/usr/bin/python3

# 0. Ask the user for num1, operator and num2
num1, operator, num2 = input('Enter calculation: ').split()

# 1. Convert numbers to int
num1 = int(num1)
num2 = int(num2)

# 3. Use if statements to choose correct operation
if operator == "+":
    print("{} + {} = {}".format(num1, num2, num1 + num2))
elif operator == "-":
    print("{} - {} = {}".format(num1, num2, num1 - num2))
elif operator == "*":
        print("{} * {} = {}".format(num1, num2, num1 * num2))
elif operator == "/":
        print("{} / {} = {}".format(num1, num2, num1 / num2))
elif operator == "%":
        print("{} % {} = {}".format(num1, num2, num1 % num2))

