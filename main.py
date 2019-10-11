# rules
# two players
# board is to be printed out after each move
# accept input of player position and place symbol on board


def main():
    play_game = True

    while play_game:
        marks = determine_marks()
        print(marks)

        # player 1 will go first.
        print("Player 1 will go first.")
        ready()

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
        p1_string = input("Player 1: Would you like X or O? ")
        p1_mark = p1_string[0].capitalize()
        valid_answer = check_inputs(["X", "O"], p1_mark)
    if p1_mark == 'X':
        return {"p1": "X", "p2": "O"}
    else:
        return {"p1": "O", "p2": "X"}


def ready():
    rdy = False
    valid_answer = False
    while not rdy:
        while not valid_answer:
            response = input("Are you ready to play? ")
            valid_answer = check_inputs(["Y", "N"], response[0].capitalize())
        rdy = response[0].capitalize() == "Y"
        valid_answer = False


def check_inputs(acceptable, my_s):
    if my_s not in acceptable:
        print("Invalid response. Please enter {}".format(acceptable))
    return my_s in acceptable


main()
