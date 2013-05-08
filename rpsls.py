# The key idea of this program is to match the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors
#
# we can then simply calculate the difference using the following formula
# difference = (player_number - comp_number)%5
# if difference == 1 or difference == 2: player wins
# if difference == 3 or difference == 4: computer wins
# else: draw

# helper functions
import random

def rpsls(name): 
    """ 
    str -> str, str, str
    takes player_choice as input and returns Computer / Player / Tie as well as player and computer choice
    """

    # convert name to player_number using name_to_number
    player_number = name_to_number(name.lower())
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(5)
    # compute difference of player_number and comp_number modulo five
    difference = (player_number - comp_number)%5
    # use if/elif/else to determine winner
    if difference == 1 or difference == 2:
        #player wins
        winner = 'Player'
    elif difference == 3 or difference == 4:
        #computer wins
        winner = 'Computer'
    else:
        #tie
        winner = 'Tie'
    # convert comp_number to name using number_to_name
    comp_name = number_to_name(comp_number)
    
    # return results
    return winner, name, comp_name

def number_to_name(number):
    """ int in range (0, 5) -> str
    convert number to a name"""
    names = ['rock', 'Spock', 'paper', 'lizard', 'scissors'] 
    return names[number]
    
def name_to_number(name):
    """str -> int in range(0, 5)
    convert name to number"""
    if name == 'rock':
        return 0
    elif name == 'spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        raise Exception("Invalid game choice. Must be in [rock, paper, scissors, lizard, spock]")

# ask for user choice and start game if this file is executed
if __name__ == '__main__':
    # ask for choice
    choice = raw_input('Choose rock, paper, scissors, lizard or Spock: ')

    try:
        #get winner
        winner, player, computer = rpsls(choice)

        # print winner info etc
        print 'Player chose ' + player
        print 'Computer chose ' + computer
        if winner == 'Tie':
            print 'It\' a tie!'
        else:
            print  winner + ' wins!'

    except BaseException, e:
        print 'Error: ' + str(e)

    

