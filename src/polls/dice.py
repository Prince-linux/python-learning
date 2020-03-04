# Generating random values in a diceroll

import random


class Dice:

    def roll():
        first_num = random.randint(1, 6)
        second_num = random.randint(1, 6)
        return first_num, second_num


dice = Dice
print(dice.roll())
