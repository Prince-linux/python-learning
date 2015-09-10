#! /usr/bin/python3

# country.py -- This script prints out a country and it's population.

# Author -- Prince Oppong Boamah<regioths@gmail.com>

# Date -- 9th September,2015

class Country:
    pass

# The program starts running here.
j = Country()
print("j is a %s" % (j.__class__))
j.name = "Ghana"
j.name1 = "Nigeria"
j.population = "25million"
j.population1 = "500million"
print("The country %s has a lot of population thus %s than %s which has %s and this inluences the citizen to take serious change of mind and heart." % (j.name1, j.population1, j.name, j.population)) 
