#! /usr/bin/python3

# point.py -- prints the points kofi got. 

# Author -- Prince Oppong Boamah<regioths@gmail.com>

# Date -- 10th September, 2015

class Point:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

# The program starts running here.
x = Point("90 points")
print("x is a %s" % (x.__class__))
print("The marathon resulted in kofi getting %s" % (x.name))

