#! /usr/bin/python3

# report.py -- This script prints out a report

# Author -- Prince Oppong Boamah<regioths@gmail.com>

# Date -- 10th September, 2015

class Report:
    def __init__(self, name):
        self.name = name

# The program starts running here.
r = Report("La General Hospital")
print("r is a %s" % (r.__class__))
r.year = "2014"
print("The %s report states that in %s Maternal death was reduced." % (r.name, r.year))

