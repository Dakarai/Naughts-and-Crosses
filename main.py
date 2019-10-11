# rules
# two players
# board is to be printed out after each move
# accept input of player position and place symbol on board


def main():
    play_game = True

    while play_game:
        determine_marks()

    # player 1 will go first.

    # ready?
    # print board
    # while(game not over)
    # receive positional input
    # add to board
    # check if winner
    # print board

    # player X has won
    # play again?


def determine_marks():
    # ask player 1 if X or O
    valid_answer = False
    while not valid_answer:
        p1_s = input("Player 1: Would you like X or O? ")