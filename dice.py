from random import randint

def tittle(msg):
    print('-=' * 30)
    print(f'{msg:^70}')
    print('-=' * 30)


def dice(number):
    print(f'The dice you choose rolled {randint(0, number)}')