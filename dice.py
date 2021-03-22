from random import randint
from time import sleep


def tittle(msg):
    print('-=' * 30)
    print(f'{msg:^70}')
    print('-=' * 30)


def dual_d6():
    d1 = randint(1, 6)
    d2 = randint(1, 6)
    print(f'Rolling two \033[1;32mD6\033[m dice')
    sleep(0.5)
    print('...')
    sleep(0.5)
    print('..')
    sleep(0.5)
    print('.')
    sleep(0.5)

    print(f'>> {d1} <<')
    sleep(0.5)
    print(f'>> {d2} <<')
    sleep(0.5)
    print(f'The result is {d1 + d2}')


def free_dice(number):
    dice_roll = randint(1, number)
    print(f'Rolling the \033[1;32mD{number}\033[m dice')
    sleep(0.5)
    print('...')
    sleep(0.5)
    print('..')
    sleep(0.5)
    print('.')
    sleep(0.5)

    print(f'>>> {dice_roll} <<<')
