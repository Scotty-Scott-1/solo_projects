#!/usr/bin/python3
class person:
    def say_hi(self, message, number):
        print("{} {}".format(message, number))


p = person()
p.say_hi("an arg passed to a method")

# The previous two lines can also be written as:
# person().say_hi()

