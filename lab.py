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
    
    res = {}
    row = len(level_description)
    col = len(level_description[0])
    size = (row, col)
    things = {'wall', 'computer', 'target', 'player'}
    for i in range(row):
        for j in range(col):
            cell = level_description[i][j]
            for contents in cell:
                if(contents not in res):
                    res[contents] = set()
                    res[contents].add((i,j))
                else:
                    res[contents].add((i, j))
    for items in things:
        if items not in res.keys():
            res[items] = set()

    return (res, size)

            



def victory_check(game):
    """
    Given a game representation (of the form returned from make_new_game), where
    there are the same number of computers and targets, return a Boolean:
    True if all the computers are placed on targets, and False otherwise.

    A game with no computers or targets is unwinnable. This function should not mutate
    the input game.
    """
    target = game[0]['target']
    computer = game[0]['computer']
    if(len(target) == 0 or len(computer) == 0):
        return False
    return game[0]['computer'] == game[0]['target']

def copy_set(game):
    dic = {}
    for key, value in game[0].items():
        dic[key] = value.copy()
    return dic, game[1]

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
    copy_game = copy_set(game)
    size = game[1]
    pos = copy_game[0]['player'].copy()
    pos = pos.pop()
    walls = copy_game[0]['wall']
    computers = copy_game[0]['computer']
    row,col = DIRECTION_VECTOR[direction]
    newPos = (pos[0] + row, pos[1]+ col)
    t = (newPos[0] + row, newPos[1] + col)
    if(0 <= newPos[0] < size[0] and 0 <= newPos[1] < size[1]):
        if(newPos in walls):
            return copy_game
        if(0 <= t[0] < size[0] and 0 <= t[1] < size[1]):
            if(newPos in computers):
                if(t in walls or t in computers):
                    return copy_game
                copy_game[0]['computer'].remove(newPos)
                copy_game[0]['computer'].add(t)
        if(newPos not in computers):
            copy_game[0]['player'] = set()
            copy_game[0]['player'].add(newPos)
    return copy_game


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
    dic, size = game
    res = []
    walls = set(dic['wall'])
    computer = set(dic['computer'])
    target = set(dic['target'])
    player = set(dic['player'])
    for i in range(size[0]):
        tmp = []
        for j in range(size[1]):
            to_add = []
            if((i,j) in walls):
                to_add.append('wall')
            if((i,j) in computer):
                to_add.append('computer')
            if((i,j) in target):
                to_add.append('target')
            if((i,j) in player):
                to_add.append('player')
            tmp.append(to_add)
        res.append(tmp)
    return res


def generate_hashable(game):
    res = []
    players = []
    computers = []
    for player in game[0]['player']:
        players.append(player)
    for computer in game[0]['computer']:
        computers.append(computer)
    player = tuple(player)
    computers = tuple(computers)
    res.append(player)
    res.append(computers)
    return tuple(res)



def generate_board(game, func):
    if(func(game)):
        return (game,)
    agenda = [(game,)]
    visited = {(generate_hashable(game))}
    while agenda:
        g = agenda.pop(0)
        terminal = g[-1]
        for direction in DIRECTION_VECTOR:
            new = step_game(terminal, direction)
            if generate_hashable(new) not in visited:
                new_path = g + (new,)
                if(func(new)):
                    return new_path
                agenda.append(new_path)
                visited.add(generate_hashable(new))
    return None


def generate_steps(seq):
    if(seq == None):
        return None
    path = []
    for i in range(len(seq) - 1):
        check = seq[i]
        for direction in DIRECTION_VECTOR:
            step = step_game(check, direction)
            if(step == seq[i + 1]):
                path.append(direction)
                break
    return path



def solve_puzzle(game):
    """
    Given a game representation (of the form returned from make_new_game), find
    a solution.
    Return a list of strings representing the shortest sequence of moves ("up",
    "down", "left", and "right") needed to reach the victory condition.

    If the given level cannot be solved, return None. This function should not mutate
    the input game.
    """
    copy_game = copy_set(game)
    seq = generate_board(copy_game, victory_check)
    path = generate_steps(seq)
    return path


if __name__ == "__main__":
    level = [
  [[], [], [], ["wall"], ["wall"], ["wall"], ["wall"]],
  [[], [], [], ["wall"], [], [], ["wall"]],
  [[], [], [], ["wall"], ["player"], [], ["wall"]],
  [["wall"], ["wall"], ["wall"], ["wall"], [], ["target", "computer"], ["wall"]],
  [["wall"], [], [], [], [], ["target", "computer"], ["wall"]],
  [["wall"], [], ["wall"], [], [], ["target", "computer"], ["wall"]],
  [["wall"], [], [], [], [], ["wall"], ["wall"]],
  [["wall"], ["wall"], ["wall"], ["wall"], ["wall"], ["wall"], []]
]



    res = make_new_game(level)
    print(solve_puzzle(res))
   