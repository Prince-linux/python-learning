#! /usr/bin/python3

# planet.py -- this script prints the name of a planet and it's habitation

# Author -- Prince Oppong Boamah<regioths@gmail.com>

# Date -- 10th September, 2015

class Planet:
    def __init__(self, name):
        self.name = name

# The program starts running here.
d = Planet("Mars")
d.people = "None"
d.name1 = "Earth"
d.people1 = " A lot"
print("d is a %s" % (d.__class__))
print("Hmmm %s is a planet that has %s living things but %s has %s of living things on it" % (d.name, d.people, d.name1, d.people1))

