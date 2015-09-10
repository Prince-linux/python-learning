#! /usr/bin/python3

# student.py -- This script prints out the name of a student and the school he attends.

# Author -- Prince Oppong Boamah<regioths@gmail.com>

# Date -- 9th September 2015.

class Student:
    pass
# The program starts running here.
s = Student()
print("s is a %s" % (s.__class__))
s.name = "Doris"
s.school = "University of Chana"
print("%s is a student of %s" % (s.name, s.school))

