import consts

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


def dino_move(game_state, game_field):
    global dino_forward_back
    if dino_position[1][1] == len(game_field[0]) - 1:
        game_state["is_dino_move_forward"] = False

    if dino_position[0][1] == 0:
        game_state["is_dino_move_forward"] = True

    if game_state["is_dino_move_forward"]:
        game_field[dino_position[0][0]][dino_position[0][1]]['dino'] = False
        game_field[dino_position[1][0]][dino_position[1][1]]['dino'] = False

        dino_position[0][1] += 1
        dino_position[1][1] += 1

    if not game_state["is_dino_move_forward"]:
        game_field[dino_position[0][0]][dino_position[0][1]]['dino'] = False
        game_field[dino_position[1][0]][dino_position[1][1]]['dino'] = False

        dino_position[0][1] -= 1
        dino_position[1][1] -= 1
