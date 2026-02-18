"""
6.101 Lab:
Snekoban Game
"""

# import json # optional import for loading test_levels
# import typing # optional import
# import pprint # optional import

# NO ADDITIONAL IMPORTS!


DIRECTION_VECTOR = {
    "up": (-1, 0),
    "down": (+1, 0),
    "left": (0, -1),
    "right": (0, +1),
}


def make_new_game(level_description):
    """
    Given a description of a game state, create and return a game
    representation of your choice.

    The given description is a list of lists of lists of strs, representing the
    locations of the objects on the board (as described in the lab writeup).

    For example, a valid level_description is:

    [
        [[], ['wall'], ['computer']],
        [['target', 'player'], ['computer'], ['target']],
    ]

    The exact choice of representation is up to you; but note that what you
    return will be used as input to the other functions. This function should not
    mutate the level_description.
    """
    #make a tuple of tuples of tuple containing strings?
    #for item in level_description:
        #print(item)
    
    res = ()
    for row in level_description:
        tmp = ()
        for items in row:
            i = ()
            for item in items:
                print(item)
                i += tuple(item)
            tmp += i
        res += tmp
    return res

            




def victory_check(game):
    """
    Given a game representation (of the form returned from make_new_game), where
    there are the same number of computers and targets, return a Boolean:
    True if all the computers are placed on targets, and False otherwise.

    A game with no computers or targets is unwinnable. This function should not mutate
    the input game.
    """
    raise NotImplementedError


def step_game(game, direction):
    """
    Given a game representation (of the form returned from make_new_game),
    return a game representation (of that same form), representing the
    updated game after running one step of the game.  The user's input is given
    by direction, which is one of the following:
        {'up', 'down', 'left', 'right'}.

    This function should not mutate its input.
    Hint: you may want to use the DIRECTION_VECTOR
    """
    raise NotImplementedError


def dump_game(game):
    """
    Given a game representation (of the form returned from make_new_game),
    convert it back into a level description that would be a suitable input to
    make_new_game (a list of lists of lists of strings).

    This function is used by the GUI and the tests to see what your game
    implementation has done, and it can also serve as a rudimentary way to
    print out the current state of your game for testing and debugging on your
    own. This function should not mutate the game.
    """
    raise NotImplementedError


def solve_puzzle(game):
    """
    Given a game representation (of the form returned from make_new_game), find
    a solution.

    Return a list of strings representing the shortest sequence of moves ("up",
    "down", "left", and "right") needed to reach the victory condition.

    If the given level cannot be solved, return None. This function should not mutate
    the input game.
    """
    raise NotImplementedError


if __name__ == "__main__":
    level = [
        [[], ['wall'], ['computer']],
        [['target', 'player'], ['computer'], ['target']],
    ]
    print(make_new_game(level))