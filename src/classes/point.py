#! /usr/bin/python3

# point.py -- prints the points kofi got. 

# Author -- Prince Oppong Boamah<regioths@gmail.com>

# Date -- 9th September, 2015

class Point:
    pass

# The program starts running here.
x = Point()
print("x is a %s" % (x.__class__))
x.name = "90 points"
print("The marathon resulted in kofi getting %s" % (x.name))

