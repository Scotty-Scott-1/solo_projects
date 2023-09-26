#!/usr/bin/python3

# 0. Ask the user to input two values and store them in variables
# num1 & num 2
num1, num2 = input('Enter two numbers: ').split()

# 1. Convert the strings into regular numbers: Integers
num1 = int(num1)
num2 = int(num2)

# 2. Add the numbers and store them in sum
sum = num1 + num2

# 3. Subtract the numbers and store them in difference
difference = num1 - num2

# 4. Multiply the numbers and store them in product
product = num1 * num2

# 5. Divide the numbers and store them in division
division = num1 / num2

# 6. Use modulus on the numbers and store the remainder in remainder
remainder = num1 % num2

# 7. Print the results
print("{} + {} = {}".format(num1, num2, sum))
print("{} - {} = {}".format(num1, num2, difference))
print("{} * {} = {}".format(num1, num2, product))
print("{} / {} = {}".format(num1, num2, division))
print("{} % {} = {}".format(num1, num2, remainder))
