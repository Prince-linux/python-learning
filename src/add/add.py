#! /usr/bin/python3

# add.py -- This script asks for two inputs from a user, adds them and prints them to the screen.

# Author -- Prince Oppong Boamah<regioths@gmail.com>

# Date -- 10th september, 2015

while True:
    a = input("Please enter any integer: ")
    try:
        n1 = int(a)
        print(n1)
        break
    except ValueError:
        print("Not a valid integer:  Try again.")

             
while True:
    b = input("Please enter another integer: ")
    try:
        n2 = int(b)
        print(n1 + n2)
        break
    except ValueError:
        print("Not a valid integer: Try again.")
    
