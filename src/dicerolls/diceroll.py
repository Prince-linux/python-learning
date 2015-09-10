#! /usr/bin/python3

# diceroll.py --  This program simulates a 1000 dice rolls randomly.

# Author -- Prince Oppong Boamah<regioths@gmail.com>

# Date -- 9th September, 2015.

import random

diceroll = (0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6,)*1000
for roll in diceroll:
    print("This is what you got %s." % random.randrange(0, 7))
