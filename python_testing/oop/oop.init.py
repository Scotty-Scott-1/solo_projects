#!/usr/bin/python3
class person:
    def __init__(self, name):
        self.name = name

    def say_hi(self, message):
        print("Hello, my name is {}. {}".format(self.name, message))

#p = person("Scott")
#p.say_hi()

person("Scotty Scott").say_hi("I'm a cat")


# The previous two line can also be writted as
# person("Scott").say_hi()
