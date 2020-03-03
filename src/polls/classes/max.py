# A simple use of user modules in python
from utils import find_max


numbers = [0, 2, 8, 10, 280, 8, 90, 800, 7000, 29, 5]
max_number = find_max(numbers)
print(max_number)
