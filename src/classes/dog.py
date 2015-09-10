#! /usr/bin/python3

# dog.py -- This script prints the name of a dog and it's race.

# Author -- Prince Oppong Boamah<regioths@gmail.com>

# Date -- 9th September, 2015

class Dog:
    pass

# The program starts running here.
s = Dog()
s.name = "Leslie"
s.race = "Local"
print("s is a %s" % (s.__class__))
print("The dog is called %s and it is a %s breed" % (s.name, s.race))
