#! /usr/bin/python3

# country.py -- This script prints a country.

# Author -- Prince Oppong Boamah<regioths@gmail.com>

# Date -- 10th September,2015

class Country:
    def __init__(self, name):
        self.name = name

# The program starts running here.
j = Country("Ghana")
print("j is a %s" % (j.__class__))
print("The country %s is my native land" % (j.name))
