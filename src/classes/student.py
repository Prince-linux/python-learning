#! /usr/bin/python3

# student.py -- This script prints out the name of a student and the school attended

# Author -- Prince Oppong Boamah<regioths@gmail.com>

# Date -- 10th September 2015.

class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

# The program starts running here.
s = Student("Doris")
print("s is a %s" % (s.__class__))
s.school = "University of Chana"
print("%s is a student of %s" % (s.name, s.school))

