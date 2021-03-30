from dice import *

again = 'Y'
dice_type = 0 

tittle('\033[1;31mDICE SIMULATOR\033[m')
print("Welcome to the best dice simulator you've ever seen!\n")

# There's a bug in the following while, you can't play another mode when you've already played one mode

while True:
    print('1 - Press "A" for the free dice game-mode.')
    print('2 - or "B" for the dual D6 game-mode.')
    print('3 - you can press "X" for quit.')
    game_mode = input(f'Choose your game-mode [A, B or X]: ')

    if game_mode.upper() == 'A':
        
        while again.upper() == 'Y':

            if again.upper() == 'Y':
                dice_type = int(input('Which kind of dice you want to roll? '))
                free_dice(dice_type)

            else:
                print('\033[1;31mERROR\033[m')
                print('You can only type "Y" for yes or "N" for not')

            again = input('Play again? [y/n] ')

    elif game_mode.upper() == 'B':

        while again.upper == 'Y':
            
            if again.upper() == 'Y':
                dual_d6()

            else:
                print('\033[1;31mERROR\033[m')
                print('You can only type "Y" for yes or "N" for not')

            again = input('Play again? [y/n] ')

    elif game_mode.upper() == 'X':
        break

    else:
        print('\033[1;31mERROR\033[m')
        print('You can only type "A", "B" or "X"')

print('Closing')
sleep(0.5)
print('...')
sleep(0.5)
print('..')
sleep(0.5)
print('.')
sleep(0.5)
print('\033[1;31mTHE END.\033[m')
