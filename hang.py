# This function holds the different stages of user guesses
# and displays the graphic for a hangman.
def create_chance_for_man():
    hang = """
    ____
        |
        |
        -"""
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
    return [hang, empty, head, body, left_arm, right_arm, left_leg, right_leg]