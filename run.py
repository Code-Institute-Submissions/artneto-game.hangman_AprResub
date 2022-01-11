from hang import create_chance_for_man
from hang import print_initial_message
from hang import get_username
from hang import print_rules
from hang import create_newords

chance_for_man = create_chance_for_man()

win = 0
wrong = 0
letters_rg = ''
letters_wrg = ''
print_initial_message()
get_username()
print_rules()
hang = """
    ____
        |
        |
        -"""
# Checking if user input matches the letter in the "secret word".
word = create_newords()
while win != len(word) and wrong != 6:
    message = ''
    for letter in word:
        if letter in letters_rg:
            message += f'{letter} '
        else:
            message += '_ '
    print(hang+chance_for_man[wrong])
    print(message)

    letter = input('please input a letter').upper()

    if letter in letters_rg+letters_wrg:
        print('Wrong guess')
        continue
    # Player guessed a right letter.
    if letter in word:
        print('Good job')
        letters_rg += letter
        win += word.count(letter)
    else:
        print('Is not the right guess')
# Player guessed wrong letter.
        letters_wrg += letter
        wrong += 1


# This code is the end game, will show the secret word even if the user
# win or loose.
if wrong < 6:
    print("Great job, you are the winner!")
    print("The secret word was {}".format(word))
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

else:

    print("Game over, you are hanged!")
    print("The secret word was {}".format(word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/            ")
    print("Thanks for playing!")


