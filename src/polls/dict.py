# A typical use of python dictionary

customer = {
    "name": "Andre",
    "age": 1,
    "is_verified": True
}
customer["name"] = "Andre Boamah"
print(customer.get("birthdate", "November 25, 2018"))
print(customer.get("name"))
print(customer.get("age"))
print(customer.get("is_verified"))
