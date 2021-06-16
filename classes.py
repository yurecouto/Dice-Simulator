from random import randint, choice
from time import sleep

class Dice:
    def __init__(self, number):
        self.number = number


class D4(Dice):
    def rolling(self):
        if self.number == 1:
            roll = randint(1, 4)
            return roll      

class D6(Dice):
    def rolling(self):
        if self.number == 1:
            roll = randint(1, 6)
            return roll 


class D8(Dice):
    def rolling(self):
        if self.number == 1:
            roll = randint(1, 8)
            return roll        

