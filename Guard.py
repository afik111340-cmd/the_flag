import consts
from Game_field import game_field

dino_position = []
dino_forward_back = 'forward'


def set_dino_starting_position(game_field):
    global dino_position
    left_leg, right_leg = consts.DINO_START_PLACEMENT
    left_leg_row, left_leg_col = left_leg
    right_leg_row, right_leg_col = right_leg

    dino_position = [[left_leg_row, left_leg_col], [right_leg_row, right_leg_col]]
    game_field[left_leg_row][left_leg_col]['dino'] = True
    game_field[right_leg_row][right_leg_col]['dino'] = True


def dino_move(game_field):
    global dino_forward_back
    if dino_position[1][1] == len(game_field[0]) - 1:
        dino_forward_back = 'back'

    if dino_position[0][1] == 0:
        dino_forward_back = 'forward'

    if dino_forward_back == 'forward':
        game_field[dino_position[0][0]][dino_position[0][1]]['dino'] = False
        game_field[dino_position[1][0]][dino_position[1][1]]['dino'] = False

        dino_position[0][1] += 1
        dino_position[1][1] += 1

    if dino_forward_back == 'back':
        game_field[dino_position[0][0]][dino_position[0][1]]['dino'] = False
        game_field[dino_position[1][0]][dino_position[1][1]]['dino'] = False

        dino_position[0][1] -= 1
        dino_position[1][1] -= 1


def check_if_got_eaten(soldier):
    got_eaten = False
    for side in range(soldier):
        for hight in range(3):
            if game_field[soldier[0][hight]][soldier[1][hight]]['dino']:
                got_eaten = True

    return got_eaten





