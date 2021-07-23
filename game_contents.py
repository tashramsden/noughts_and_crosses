"""Constants/starting grids"""

instruction_grid = "  1  |  2  |  3  \n" \
                   "----- ----- -----\n" \
                   "  4  |  5  |  6  \n" \
                   "----- ----- -----\n" \
                   "  7  |  8  |  9  \n"

winning_combos = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]

row_divide = "----- ----- -----"

board_contents = {
    1: "     ",
    2: "     ",
    3: "     ",
    4: "     ",
    5: "     ",
    6: "     ",
    7: "     ",
    8: "     ",
    9: "     ",
}

game_board = f"{board_contents[1]}|{board_contents[2]}|{board_contents[3]}\n" \
             f"{row_divide}\n" \
             f"{board_contents[4]}|{board_contents[5]}|{board_contents[6]}\n" \
             f"{row_divide}\n" \
             f"{board_contents[7]}|{board_contents[8]}|{board_contents[9]}\n"
