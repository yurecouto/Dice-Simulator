from dice import *

dice_type = 0

while True:

    tittle('\033[1;31mDICE SIMULATOR\033[m')
    print("Welcome to the best dice simulator you've ever seen!\n")

    again = 'Y'
    print('1 - Press "A" for the \033[1;32mFREE-DICE\033[m game-mode.')
    print('2 - Press "B" for the \033[1;32mDUAL-D6\033[m game-mode.')
    print('3 - Press "C" for the \033[1;32mPERCENTAGE\033[m game-mode.')
    print('4 - Or press "X" for quit')
    game_mode = input(f'Choose your game-mode [A, B, C or X]: ')

    while game_mode.upper() == 'A':
        
        print('\nChoose a dice (D4, D6, D8, D10, D12, D14, D16, D18 or D20.)\n')
        dice_type = int(input('Which kind of dice you want to roll? '))
        free_dice(dice_type)

        again = input('Play again? [Y/N] ')

        if again.upper() == 'N':
            break

        elif again.upper() != 'N' and again.upper() != 'Y':
            print('\033[1;31mERROR\033[m')
            print('You can only type "Y" for yes or "N" for not')

    while game_mode.upper() == 'B':

        dual_d6()

        again = input('Play again? [Y/N] ')

        if again.upper() == 'N':
            break

        elif again.upper() != 'N' and again.upper() != 'Y':
            print('\033[1;31mERROR\033[m')
            print('You can only type "Y" for yes or "N" for not')

    while game_mode.upper() == 'C':

        percent()

        again = input('Play again? [Y/N] ')

        if again.upper() == 'N':
            break
            
        elif again.upper() != 'N' and again.upper() != 'Y':
            print('\033[1;31mERROR\033[m')
            print('You can only type "Y" for yes or "N" for not')

    if game_mode.upper() == 'X':
        break

    elif game_mode.upper() not in 'ABX':
        print('\033[1;31mERROR\033[m')
        print('You can only type "A", "B" or "X"')

sleeping('Closing')
print('\033[1;31mTHE END.\033[m')
