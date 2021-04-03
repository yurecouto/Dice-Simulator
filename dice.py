from random import randint
from time import sleep


def sleeping(action=''):
    print(action)
    sleep(0.5)
    print('...')
    sleep(0.5)
    print('..')
    sleep(0.5)
    print('.')
    sleep(0.5)
    print()


'''This function makes a simple banner'''


def tittle(msg):
    print('-=' * 30)
    print(f'{msg:^70}')
    print('-=' * 30)
    print("Welcome to the best dice simulator you've ever seen!\n")


'''This function makes the game-mode of the two D6'''


def dual_d6():
    d1 = randint(1, 6)
    d2 = randint(1, 6)
    print(f'Rolling two \033[1;32mD6\033[m dice')

    sleeping()

    print(f'>> {d1} <<')
    sleep(0.5)
    print(f'>> {d2} <<')
    sleep(0.5)
    print(f'The result is {d1 + d2}')


'''This one makes possible to choose the number of faces'''
# I'm gonna make an dice tyope limiter to let only possible dices available, like d4, d6, d8, d10, d12, and d20


def free_dice(number):
    dice_roll = randint(1, number)
    print(f'Rolling the \033[1;32mD{number}\033[m dice')

    sleeping()

    print(f'>>> {dice_roll} <<<')

