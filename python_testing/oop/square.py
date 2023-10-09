#!/usr/bin/python3
class Sqaure:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    @property
    def height(self):
        print("Retrieving the height")

        return self.__height

    @height.setter
    def height(self, value):
        if value.isdigit():
            self.__height = value
        else:
            print("Please only enter numbers for height")

    @property
    def height(self):
        print("Retrieving the height")

        return self.__height

    @width.setter
    def width(self, value):
        if value.isdigit():
            self.width = value
        else:
            print("Please only enter numbers for width")

    

    def main():
        aSquare = Sqaure
        height = input("Enter hieght : ")
        width = input()
