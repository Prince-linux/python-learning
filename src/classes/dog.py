#! /usr/bin/python3

# dog.py -- This script prints the name of a dog and it's race.

# Author -- Prince Oppong Boamah<regioths@gmail.com>

# Date -- 9th September, 2015

class Dog:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

# The program starts running here.
s = Dog("Leslie")
s.race = "Local"
print("s is a %s" % (s.__class__))
print("The dog is called %s and it is a %s breed" % (s.name, s.race))
