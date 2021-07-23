"""A class to handle all current game data and carry out game functions"""

from game_contents import instruction_grid, row_divide, winning_combos, board_contents, game_board


class GameManager:

    def __init__(self):
        self.current_player = "X"
        self.board_contents = board_contents
        self.game_board = game_board
        self.moves = {
            "X": [],
            "O": [],
        }
        self.available_spaces = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def clear_game_board(self):
        self.board_contents = {1: "     ", 2: "     ", 3: "     ", 4: "     ", 5: "     ", 6: "     ", 7: "     ", 8: "     ", 9: "     ", }
        self.game_board = game_board

    def switch_players(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    def update_game_board(self):
        self.game_board = f"{self.board_contents[1]}|{self.board_contents[2]}|{self.board_contents[3]}\n" \
                          f"{row_divide}\n" \
                          f"{self.board_contents[4]}|{self.board_contents[5]}|{self.board_contents[6]}\n" \
                          f"{row_divide}\n" \
                          f"{self.board_contents[7]}|{self.board_contents[8]}|{self.board_contents[9]}\n"

    def register_move(self, selection):
        self.moves[self.current_player].append(selection)
        self.available_spaces.remove(selection)

    def check_winning(self):
        win = False
        for combo in winning_combos:
            full_combo = 0
            for number in combo:
                if number in self.moves[self.current_player]:
                    full_combo += 1
            if full_combo == 3:
                win = True
        return win

    def check_spaces(self):
        if not self.available_spaces:
            return False
        else:
            return True

    def new_move(self):
        print(instruction_grid)
        print(f"It's player {self.current_player}'s move.")
        selection = input(f"Please pick an available space by selecting a number between 1 and 9:\n{self.game_board}")
        try:
            selection = int(selection)
            if 1 <= selection <= 9:
                pass
            else:
                print("Sorry, that's not a valid number. Try again!")
                return "TRY_AGAIN"
        except ValueError:
            print("Sorry, that's not a valid option. Try again!")
            return "TRY_AGAIN"

        if selection not in self.available_spaces:
            print("Sorry, that's not an available space. Try again!")
            return "TRY AGAIN"

        self.board_contents[selection] = f"  {self.current_player}  "
        self.update_game_board()
        self.register_move(selection)
        has_won = self.check_winning()
        moves_left = self.check_spaces()

        if has_won:
            return "WINNER"
        elif not moves_left:
            return "DRAW"
        else:
            return "KEEP PLAYING"

    def winner(self):
        print(self.game_board)
        print(f"Congratulations! Player {self.current_player} has won!")

    def draw(self):
        print(self.game_board)
        print("It's a draw. Better luck next time!")

