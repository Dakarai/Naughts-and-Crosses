# rules
# two players
# ask Player 1 if X or O
# ask if Ready
# board is to be printed out after each move
# accept input of player position and place symbol on board
# after game is over, ask to play again
import random


def main():
    play_game = True

    while play_game:
        marks = determine_marks()

        current_player = next_player()
        print("{} will go first.".format(current_player))

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
    """
    Determines X and O for each player.

    Returns:
         dict: {"Player 1": mark, "Player 2": mark}
    """
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
    """
    Keeps player in routine until they confirm they are ready.
    No output.
    """
    rdy = False
    valid_answer = False
    while not rdy:
        while not valid_answer:
            response = input("Are you ready to play? ")
            valid_answer = check_inputs(["Y", "N"], response[0].capitalize())
        rdy = response[0].capitalize() == "Y"
        valid_answer = False


def next_player(current_player="None"):
    """
    Determines the next player. Chooses a random player if current_player is not passed.
    :param current_player: "Player 1" or "Player 2". Null to return random previous string.
    :return: "Player 1" or "Player 2"
    """
    if current_player == "None":
        return random.choice(["Player 1", "Player 2"])
    elif current_player == "Player 1":
        return "Player 2"
    else:
        return "Player 1"


def draw_board(board_state):
    """
    Draws the current board through the board_state list
    :param board_state: 9-length list with current marks.
    :return: no output
    """
    print(" {} | {} | {} ".format(board_state[6], board_state[7], board_state[8]))
    print("-----------")
    print(" {} | {} | {} ".format(board_state[3], board_state[4], board_state[5]))
    print("-----------")
    print(" {} | {} | {} ".format(board_state[0], board_state[1], board_state[2]))


def receive_play(current_player, marks, board_state):
    """
    Receives an input from the current player and places it on the board after checking input validity.
    :param current_player: "Player 1" or "Player 2"
    :param marks: "X" or "X"
    :param board_state: list item with indices 0-8 corresponding to their board position
    :return: board_state after placing turn's mark.
    """
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
    """
    Given a board_state, return which positions are empty
    :param board_state: list item with indices 0-8 corresponding to their board position
    :return: list item containing open positions. [] if no open positions
    """
    my_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i in range(0, 9):
        if board_state[i] != " ":
            my_list.remove(str(i+1))
    return my_list


def check_winner(board_state):
    """
    Given a board state, determine if someone has won with three identical marks in a row
    :param board_state: list item with indices 0-8 corresponding to their board position
    :return: True if game has been won, False otherwise
    """
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
    """
    Prompts the player to play another game.
    :return: True for another game, False to end.
    """
    valid_answer = False
    while not valid_answer:
        response = input("Would you like to play again? ")
        valid_answer = check_inputs(["Y", "N"], response[0].capitalize())
    return response[0].capitalize() == "Y"


def check_inputs(acceptable, my_s):
    """
    Does the input provided by a user match the acceptable options they can choose from?
    :param acceptable: list item containing valid responses
    :param my_s: string item containing player input
    :return: True if user input a valid response, False otherwise.
    """
    if my_s not in acceptable:
        print("Invalid response. Please enter {}".format(acceptable))
    return my_s in acceptable


main()
