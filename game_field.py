import random
import consts
from consts import FLAG_PLACEMENT, Soldier_PLACEMENT

game_field = []


def create_game_field():
    global game_field
    game_field = [create_field_row(consts.COLS_FIELD) for row in range(consts.ROWS_FIELD)]


def create_field_row(row_length):
    return [create_field_dict() for col in range(row_length)]


def create_field_dict():
    return {'soldier': False, 'bush': False, 'mine': False, 'center_x': '', 'center_y': ''}


def distribute_bush():
    for i in range(consts.BUSH_NUMBER):
        manage_to_place_bush = False
        random_col = random.randrange(1, 49)
        random_row = random.randrange(1, 24)
        while [random_row, random_col] in FLAG_PLACEMENT or [random_row, random_col] in Soldier_PLACEMENT:
            random_col = random.randrange(1, 49)
            random_row = random.randrange(1, 24)

        while manage_to_place_bush == False:
            if game_field[random_row][random_col]['bush'] != True \
                    and game_field[random_row + 1][random_col]['bush'] != True \
                    and game_field[random_row][random_col + 1]['bush'] != True \
                    and game_field[random_row + 1][random_col + 1]['bush'] != True:
                manage_to_place_bush = True

        if manage_to_place_bush == True:
            game_field[random_row][random_col]['bush'] = True
            game_field[random_row + 1][random_col]['bush'] = True
            game_field[random_row][random_col + 1]['bush'] = True
            game_field[random_row + 1][random_col + 1]['bush'] = True


create_game_field()
# print(game_field)
distribute_bush()
print(game_field)





    # "center_x": center_x,
    # "center_y": center_y}
    # def calc_center_x(col, row, row_start):
    #     bubble_x = row_start + col * (
    #             consts.BUBBLE_RADIUS * 2 + consts.SPACE_BETWEEN_COLS) + consts.BUBBLE_RADIUS
    #
    #  def calc_center_y(row):
    #         return row * (consts.BUBBLE_RADIUS * 2 - consts.ROWS_OVERLAP) + \
    #             consts.BUBBLE_RADIUS
