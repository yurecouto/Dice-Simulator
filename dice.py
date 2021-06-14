from random import randint, choice
from time import sleep

class Dice:
    def __init__(self, type=4):
        self.type = type

    def rolling(type):
        roll = randint(1, type)
        
        print(roll)