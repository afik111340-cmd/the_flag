import random
import consts
from consts import FLAG_PLACEMENT, SOLDIER_START_PLACEMENT, BUSH_SIZE_BY_WIDTH_IN_CELLS, MINE_SIZE_BY_WIDTH_IN_CELLS

game_field = []
bush_in_field = []
mine_in_field = []
what_mine_exploded = []


def create_game_field():
    global game_field
    game_field = [create_field_row(consts.COLS_FIELD) for row in range(consts.ROWS_FIELD)]


def create_field_row(row_length):
    return [create_field_dict() for col in range(row_length)]


def create_field_dict():
    return {'dino': False, 'teleport': False, 'soldier': False, 'bush': False, 'mine': False, 'flag': False, 'center_x': '', 'center_y': ''}


def insert_flag_to_matrix():
    for i in range(len(FLAG_PLACEMENT)):
        game_field[FLAG_PLACEMENT[i][0]][FLAG_PLACEMENT[i][1]]['flag'] = True


def distribute_bush():
    num_of_bush_placed = 0

    while num_of_bush_placed != consts.BUSH_NUMBER:
        manage_to_place_bush = False
        random_col = random.randrange(1, 49)
        random_row = random.randrange(1, 24)

        while game_field[random_row][random_col+1]['flag'] or [random_row, random_col] in SOLDIER_START_PLACEMENT:
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
        while game_field[random_row][random_col]['flag'] or game_field[random_row][random_col+1]['flag'] or game_field[random_row][random_col+2]['flag'] or [random_row, random_col] in SOLDIER_START_PLACEMENT:
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
            mine_in_field.append([random_row, random_col, random_row, random_col + 1, random_row, random_col + 2])


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


def check_if_got_to_flag(soldier):
    got_flag = False
    for side in range(len(soldier)):
        for highet in range(1, 3):
            if [soldier[side][0] - highet, soldier[side][1]] in FLAG_PLACEMENT:
                got_flag = True

    return got_flag


def check_if_got_exploded(soldier):
    got_exploded = False
    for row in range(len(game_field)):
        for col in range(len(game_field[row])):
            if game_field[row][col]['mine'] and [row, col] in soldier:
                got_exploded = True
                for i in range(len(mine_in_field)):
                    for j in range(0, len(mine_in_field[i]), 2):
                        if row == mine_in_field[i][j] and col == mine_in_field[i][j + 1]:
                            what_mine_exploded.append(mine_in_field[i][2])
                            what_mine_exploded.append(mine_in_field[i][3])

    return got_exploded



def init_game_field():
    create_game_field()
    insert_flag_to_matrix()
    distribute_bush()
    distribute_mine()
    calc_center_x_y(game_field)




