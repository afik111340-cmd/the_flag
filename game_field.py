import random
import consts


game_field = []


def create_game_field():
    global game_field
    game_field = [
        create_field_row(row, row_start=0, row_length=consts.ROWS_FIELD)
        for row in
        range(consts.COLS_FIELD)]


def create_field_row(row_index, row_start, row_length):
    return [create_field_dict() for col in range(row_length)]


def create_field_dict():
    return {'soldier': False, 'bush': False, 'mine': False, 'center_x': '', 'center_y': ''}


def distribute_bush():
    for i in range(consts.BUSH_NUMBER):
        manage_to_place_bush = False
        random_col=[random.randrange[1, 50]]
        random_row=[random.randrange[1, 25]]





create_game_field()
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
