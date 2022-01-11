from random import choice
# This function holds the different stages of user guesses
# and displays the graphic for a hangman.
def create_chance_for_man():
    empty = """
    """
    head = """
        0
    """
    body = """
        0
        |
    """
    left_arm = """
        0
    /|
    """
    right_arm = """
        0
    /|\\
    """
    left_leg = """
        0
    /|\\
    /
    """
    right_leg = """
        0
    /|\\
    / \\
    """
    return [empty, head, body, left_arm, right_arm, left_leg, right_leg]

def print_initial_message():
    # Displays the welcome prompt and introduces user to the quiz and rules,
    # and takes an input from customer to start the quiz.
    print('*********************************')
    print("Let's Play Hangman!")
    print('*********************************')
def get_username():
    name = input("Enter your name -> ")
    print('Welcome', name, '!')
def print_rules():
    print(" ----------------------------------------- ")
    print("The objective of the Hangman is to guess the secret word.")
    print("You will need to try you letter at a time,")
    print("but If the word does not contain the suggested letter")
    print("the computer will draws one element of a hangman’s gallows")
    print("Just a reminder, you only have 6 attempts, good luck!")

# Gets a random word from my list_of_words and return the word
# with the word in uppercase.
def create_newords():
    with open('newords.txt') as file:
        lines = file.read()
        list_of_words = lines.split('\n')

    return choice(list_of_words).upper()