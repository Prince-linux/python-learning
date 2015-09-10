#! /usr/bin/python3

# currency.py -- This script prints two currencies and it's stock exchange in Ghana.

# Author -- Prince Oppong Boamah<regioths@gmail.com>

# Date -- 10th September, 2015

class Currency:
    def __init__(self, name):
        self.name = name

# The program starts running here.
c = Currency("Dollar")
print("c is a %s" % (c.__class__))
c.value = "3gh cedis"
c.name1 = "Pounds Sterling"
c.value1 = "5gh cedis"
print("The %s is of %s value whiles the %s is also valued %s in Ghana." % (c.name, c.value, c.name1, c.value1))

