#!/usr/bin/python3
'''
Problem: Reveive miles and convert to km
Km = miles * 1.60934
Input = Enter miles
Output = x miles equals x km
'''

# 0. Ask user for input
user_input = input("Enter miles: ")

# 1. Covert input to float
user_input = int(user_input)

# 2. Convert miles to km
result = user_input * 1.60934

# 3. Print the result
print("{} miles equals {} km".format(user_input, result))
