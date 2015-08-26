#! /usr/bin/python3
import sys

# add.py -- This script asks for two inputs from a user, adds them and prints them to the scree.
# Author -- Prince Oppong Boamah<regioths@gmail.com>
# Date -- 24th August 2015

num1 = input("Please enter your first number: ")
num2 = input("Please enter your second number: ")
try:
    a = int(num1)
    b = int(num2)
    print(a+b)
except ValueError:
    print("That is not a valid integer")


