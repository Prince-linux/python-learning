#! /usr/bin/python3

# product.py -- This script prints out a product and it's price. 

# Author -- Prince Oppong Boamah<regioths@gmail.com>

# Date -- 10th September, 2015

class Product:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


# The program starts running here.
p = Product("Lenovo")
p.price = "2000gh cedis or 400 pounds or 600 dollars to be precise."
print("p is a %s" % (p.__class__))
print("This is a Laptop called %s and the price is %s" % (p.name, p.price))

