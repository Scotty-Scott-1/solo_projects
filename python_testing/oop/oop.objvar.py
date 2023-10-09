#!/usr/bin/python3
class robot:
    population = 0

    def __init__(self, name):
        self.name = name
        print("Initializing {}". format(name))
        robot.population += 1

    def die(self):
        print("{} is being destroyed".format(self.name))
        robot.population -= 1

        if robot.population == 0:
            print("{} was the last one". format(self.name))
        else:
            print("There are still {} robots working".format(robot.population))

    def say_hi(self):
        print("Hello, my name is {}".format(self.name))

    @classmethod
    def how_many(cls):
        print("We have {} robots".format(cls.population))

droid1 = robot("R2-D2")
droid1.say_hi()
robot.how_many()
droid2 = robot("Chopper")
robot.how_many()
droid2.say_hi()
droid1.die()
droid2.die()
robot.how_many()
