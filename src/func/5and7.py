#! /usr/bin/python3

# 5and7.py -- This script takes a single argument and divides it with 5 and 7 and if it is divisible returns true but when it is not returns false.

# Author: Prince Oppong Boamah<regioths@gmail.com>

# Date -- 8th September, 2015

def five_and_seven(x, y):
        if x % y  == 0:
            return True
        else:
            return False

g = five_and_seven(9, 7)
print(g)
g = five_and_seven(10, 5)
print(g)
g = five_and_seven(35, 5)
print(g)
g = five_and_seven(65, 7)
print(g)
g = five_and_seven(70, 7)
print(g)
g = five_and_seven(100, 5)
print(g)
g = five_and_seven(105, 5)
print(g)
