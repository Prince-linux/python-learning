#! /usr/bin/python3

# report.py -- This script prints out a report

# Author -- Prince Oppong Boamah<regioths@gmail.com>

# Date -- 9th September, 2015

class Report:
    pass
# The program starts running here.
r = Report()
print("r is a %s" % (r.__class__))
r.name = "La General Hospital"
r.year = "2014"
print("The %s report states that in %s Maternal death was reduced" % (r.name, r.year))

