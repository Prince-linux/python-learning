#! /usr/bin/python3

# product.py -- This script prints out a product and it's price. 

# Author -- Prince Oppong Boamah<regioths@gmail.com>

# Date -- 9th September, 2015

class Product:
    pass

# The program starts running here.
p = Product()
p.name = "Lenovo"
p.price = "2000gh cedis or 400 pounds or 600 dollars to be precise."
print("p is a %s" % (p.__class__))
print("This is a Laptop called %s and the price is %s" % (p.name, p.price))

