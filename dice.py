from random import randint, choice
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


'''This function makes possible to choose the number of faces'''
def free_dice(number):

    if number % 2 == 0 and number <= 20 and number >= 4:
        dice_roll = randint(1, number)
        print(f'Rolling the \033[1;32mD{number}\033[m dice')

        sleeping()

        print(f'>>> {dice_roll} <<<')
    
    else:
        print('\033[1;31mERROR\033[m')
        print('You can only choose D4, D6, D8, D10, D12, D14, D16, D18 or D20.')


'''This function makes it's a percentage dice'''
def percent():
    print('Rooling the \033[1;32mPercent\033[m dice...')
    number_list = [00, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    sleeping()

    print(f'>>> {choice(number_list)}% <<<')
    