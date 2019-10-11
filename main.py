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

        # ready?
        ready()

        # print board
        # while(game not over)
        # receive positional input
        # add to board
        # check if winner
        # print board
        game_over = False
        board_state = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        current_player = "Player 1"
        while not game_over:
            draw_board(board_state)
            board_state = receive_play(current_player, marks, board_state)


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
        return {"Player 1": "X", "Player 2": "O"}
    else:
        return {"Player 1": "O", "Player 2": "X"}


def ready():
    rdy = False
    valid_answer = False
    while not rdy:
        while not valid_answer:
            response = input("Are you ready to play? ")
            valid_answer = check_inputs(["Y", "N"], response[0].capitalize())
        rdy = response[0].capitalize() == "Y"
        valid_answer = False


def draw_board(board_state):
    print(" {} | {} | {} ".format(board_state[6], board_state[7], board_state[8]))
    print("-----------")
    print(" {} | {} | {} ".format(board_state[3], board_state[4], board_state[5]))
    print("-----------")
    print(" {} | {} | {} ".format(board_state[0], board_state[1], board_state[2]))


def receive_play(current_player, marks, board_state):
    valid_answer = False
    while not valid_answer:
        current_play = input(
            "{}, choose a square (1-9) to place your {}. ".format(current_player, marks[current_player]))
        valid_answer = check_inputs(["1", "2", "3", "4", "5", "6", "7", "8", "9"], current_play)
    current_play = int(current_play)
    if board_state[current_play - 1] != " ":
        print("Position {} is already occupied. Choose again.".format(current_play))
        return receive_play(current_player, marks, board_state)
    else:
        board_state[current_play - 1] = marks[current_player]
        return board_state


def check_inputs(acceptable, my_s):
    if my_s not in acceptable:
        print("Invalid response. Please enter {}".format(acceptable))
    return my_s in acceptable


main()
