from random import randint

def tittle(msg):
    print('-=' * 30)
    print(f'{msg:^70}')
    print('-=' * 30)


def dice(type):
    return randint(0, type)