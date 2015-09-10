#! /usr/bin/python3

# switch.py -- This script prints out the switch from Mtn to Tigo

# Author -- Prince Oppong Boamah<regioths@gmail.com>

# Date -- 10th September, 2015

class Switch:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

# The program starts running here.
q = Switch("Mtn")
print("q is a %s" % (q.__class__))
q.new_name = "Tigo"
q.number = "0547616821"
q.number1 = "0572723240"
print("The number %s which was on the %s Network later switched to the %s Network and has %s as the new number" % (q.number, q.name, q.new_name, q.number1))

