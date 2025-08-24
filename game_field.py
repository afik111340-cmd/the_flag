import random
import consts
from consts import FLAG_PLACEMENT, SOLDIER_START_PLACEMENT

game_field = []
bush_in_field = []
mine_in_field = []


def create_game_field():
    global game_field
    game_field = [create_field_row(consts.COLS_FIELD) for row in range(consts.ROWS_FIELD)]


def create_field_row(row_length):
    return [create_field_dict() for col in range(row_length)]


def create_field_dict():
    return {'soldier': False, 'bush': False, 'mine': False, 'center_x': '', 'center_y': ''}


def distribute_bush():
    num_of_bush_placed = 0

    while num_of_bush_placed != consts.BUSH_NUMBER:
        manage_to_place_bush = False
        random_col = random.randrange(1, 49)
        random_row = random.randrange(1, 24)

        while [random_row, random_col] in FLAG_PLACEMENT or [random_row, random_col] in SOLDIER_START_PLACEMENT:
            random_col = random.randrange(1, 49)
            random_row = random.randrange(1, 24)

        if game_field[random_row][random_col]['bush'] != True \
                and game_field[random_row + 1][random_col]['bush'] != True \
                and game_field[random_row][random_col + 1]['bush'] != True \
                and game_field[random_row + 1][random_col + 1]['bush'] != True:
            manage_to_place_bush = True

        if manage_to_place_bush:
            game_field[random_row][random_col]['bush'] = True
            game_field[random_row + 1][random_col]['bush'] = True
            game_field[random_row][random_col + 1]['bush'] = True
            game_field[random_row + 1][random_col + 1]['bush'] = True
            num_of_bush_placed += 1
            bush_in_field.append([random_row, random_col])



def distribute_mine():
    num_of_mine_placed = 0

    while num_of_mine_placed != consts.MINE_NUMBER:
        manage_to_place_mine = False
        random_col = random.randrange(1, 48)
        random_row = random.randrange(1, 25)

        while [random_row, random_col] in FLAG_PLACEMENT or [random_row, random_col] in SOLDIER_START_PLACEMENT:
            random_col = random.randrange(1, 48)
            random_row = random.randrange(1, 25)

        if game_field[random_row][random_col]['mine'] != True \
                and game_field[random_row][random_col + 1]['mine'] != True \
                and game_field[random_row][random_col + 2]['mine'] != True:
            manage_to_place_mine = True

        if manage_to_place_mine:
            game_field[random_row][random_col]['mine'] = True
            game_field[random_row][random_col + 1]['mine'] = True
            game_field[random_row][random_col + 2]['mine'] = True

            num_of_mine_placed += 1
            mine_in_field.append([random_row, random_col])


def print_mateix(matrix):
    for row in matrix:
        for col in row:
            print(col, end=" ")

        print()


def calc_center_x_y(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            matrix[row][col]['center_x'] = col * consts.CELL
            matrix[row][col]['center_y'] = row * consts.CELL



create_game_field()
distribute_bush()
distribute_mine()
calc_center_x_y(game_field)
# print_mateix(game_field)
# print(bush_in_field)
# print(mine_in_field)
