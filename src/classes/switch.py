#! /usr/bin/python3

# switch.py -- This script prints out the switch from Mtn to Tigo

# Author -- Prince Oppong Boamah<regioths@gmail.com>

# Date -- 9th September, 2015

class Switch:
    pass

# The program starts running here.
q = Switch()
print("q is a %s" % (q.__class__))
q.name = "Mtn"
q.new_name = "Tigo"
q.number = "0547616821"
q.number1 = "0572723240"
print("The number %s which was on the %s Network later switched to the %s Network and has %s as the new number" % (q.number, q.name, q.new_name, q.number1))

