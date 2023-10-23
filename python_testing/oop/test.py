#!/usr/bin/python3
"""
my_tuple = ("apple", "orange", "banana", "pear")
new_tuple = ("watermelon",) + my_tuple[1:]
print(my_tuple)
print(new_tuple)
print(my_tuple is new_tuple)

"""
"""
my_tuple = (["apple", "orange", "banana", "pear"], ["apple", "blackberry", "lululemon", "orange"])
print("ID: {} {}".format(id(my_tuple), my_tuple))
my_tuple[0][0] = "watermelon"
my_tuple[1][0] = "banana republic"
print("ID: {} {}".format(id(my_tuple), my_tuple))
"""
"""
my_set = frozenset(["apple", "orange", "banana", "pear"])
new_set = frozenset(["watermelon",]) | my_set
print("my_set: {}".format(my_set))
print("new_set: {}".format(new_set))
print(new_set is my_set)
"""



