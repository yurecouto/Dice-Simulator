from random import randint]

def tittle(msg):
    print('-=' * 30)
    print(f'{msg:^70}')
    print('-=' * 30)


class Dice:
    def __init__(self, type):
        self.type = type

        return randint(0, type)