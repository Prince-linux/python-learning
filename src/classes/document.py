#! /usr/bin/python3

# document.py -- This program prints out a document type and it's size.

# Author -- Prince Oppong Boamah<regioths@gmail.com>

# Date -- 9th September, 2015

class Document:
    def __init__(self, name):
        self.name = name

# The program starts running here.
f = Document("snap.pdf")
print("f is a %s" % (f.__class__))
f.size = "98.9mb"
print("The document %s has a size of %s" % (f.name, f.size))

