#!/usr/bin/python3
class Cat:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def run(self):
        print("{} runs!".format(self.name))

    def eat(self):
        print("{} eats!".format(self.name))

    def sleep(self):
        print("{} sleeps!".format(self.name))

def main():
    scott = Cat("Scott", 1, 5)
    scott.run()
    skitty = Cat("Skitty", 1, 3)
    skitty.eat()
main()
