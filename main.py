"""Command line Noughts and Crosses"""

from game_manager import GameManager

playing = True

while playing:
    play = input("Do you want to play a game of Noughts and Crosses? y or n?\n")

    if play.lower() != "y":
        print("Bye then!")
        playing = False
        break

    else:
        this_game = True
        game_manager = GameManager()
        game_manager.clear_game_board()
        while this_game:
            move_outcome = game_manager.new_move()
            if move_outcome == "WINNER":
                game_manager.winner()
                this_game = False
                break
            elif move_outcome == "DRAW":
                game_manager.draw()
                this_game = False
                break
            elif move_outcome == "KEEP PLAYING":
                game_manager.switch_players()
            elif move_outcome == "TRY AGAIN":
                pass




