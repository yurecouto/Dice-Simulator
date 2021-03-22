from random import randint
from time import sleep

def tittle(msg):
    print('-=' * 30)
    print(f'{msg:^70}')
    print('-=' * 30)


def dice(number):
    dice_roll = randint(0, number)
    print(f'Rollind the \033[1;32mD{number}\033[mdice')
    sleep(0.5)
    print('...')
    sleep(0.5)
    print('..')
    sleep(0.5)
    print('.')

    print(f'>>> {dice_roll} <<<')
