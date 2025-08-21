import random

BUSH_NUMBER=20
MINE_NUMBER=20
game_field=[]

def create_game_field():
    game_field=[]
    global game_field
    game_field = [
        create_field_row(row, row_start=0, row_length=50)
        for row in
        range(25)]
    print(game_field)




def create_field_row(row_index, row_start, row_length):
    return [create_field_dict() for col in range(row_length)]



def create_field_dict():
    return {"type": 'empty'}


def distribute_mine_bush():
    for i in range


create_game_field()

            # "center_x": center_x,
            # "center_y": center_y}
# def calc_center_x(col, row, row_start):
#     bubble_x = row_start + col * (
#             consts.BUBBLE_RADIUS * 2 + consts.SPACE_BETWEEN_COLS) + consts.BUBBLE_RADIUS
#
#  def calc_center_y(row):
#         return row * (consts.BUBBLE_RADIUS * 2 - consts.ROWS_OVERLAP) + \
#             consts.BUBBLE_RADIUS
