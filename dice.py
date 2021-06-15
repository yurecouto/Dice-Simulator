from random import randint, choice
from time import sleep

class Dice:

    def rolling(self, faces):
        self.faces = faces
        roll = randint(1, faces)
        print(roll)
        

d4 = Dice()

d4.rolling(4)