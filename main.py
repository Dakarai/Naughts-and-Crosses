# rules
# two players
# ask Player 1 if X or O
# ask if Ready
# board is to be printed out after each move
# accept input of player position and place symbol on board
# after game is over, ask to play again


def main():
    play_game = True

    while play_game:
        marks = determine_marks()

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
        current_player = "Player 2"
        while not game_over:
            current_player = next_player(current_player)
            draw_board(board_state)
            board_state = receive_play(current_player, marks, board_state)
            game_over = check_winner(board_state)
            # if we filter board_state to []
            if not filter_occupied(board_state):
                print("The game is a draw.")
                break
        # only if the game has actually been won.
        draw_board(board_state)
        if game_over:
            print("{} has won the game!".format(current_player))
        # play again?
        play_game = play_again()


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


def next_player(current_player):
    if current_player == "Player 1":
        return "Player 2"
    else:
        return "Player 1"


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
        valid_answer = check_inputs(filter_occupied(board_state), current_play)
        if valid_answer:
            current_play = int(current_play)
            board_state[current_play - 1] = marks[current_player]
    return board_state


def filter_occupied(board_state):
    my_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i in range(0, 9):
        if board_state[i] != " ":
            my_list.remove(str(i+1))
    return my_list


def check_winner(board_state):
    if board_state[0] == board_state[1] == board_state[2] and board_state[0] != " ":
        return True
    elif board_state[0] == board_state[4] == board_state[8] and board_state[0] != " ":
        return True
    elif board_state[0] == board_state[3] == board_state[6] and board_state[0] != " ":
        return True
    elif board_state[3] == board_state[4] == board_state[5] and board_state[3] != " ":
        return True
    elif board_state[6] == board_state[7] == board_state[8] and board_state[6] != " ":
        return True
    elif board_state[6] == board_state[4] == board_state[2] and board_state[6] != " ":
        return True
    elif board_state[7] == board_state[4] == board_state[1] and board_state[7] != " ":
        return True
    elif board_state[8] == board_state[5] == board_state[2] and board_state[8] != " ":
        return True
    else:
        return False


def play_again():
    valid_answer = False
    while not valid_answer:
        response = input("Would you like to play again? ")
        valid_answer = check_inputs(["Y", "N"], response[0].capitalize())
    return response[0].capitalize() == "Y"


def check_inputs(acceptable, my_s):
    if my_s not in acceptable:
        print("Invalid response. Please enter {}".format(acceptable))
    return my_s in acceptable


main()
