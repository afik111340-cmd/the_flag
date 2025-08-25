import consts

soldier_position = []


def set_solder_starting_position(game_field):
    global soldier_position
    left_leg, right_leg = consts.SOLDIER_START_PLACEMENT
    left_leg_row, left_leg_col = left_leg
    right_leg_row, right_leg_col = right_leg

    soldier_position = [[left_leg_row, left_leg_col], [right_leg_row, right_leg_col]]
    game_field[left_leg_row][left_leg_col]['soldier'] = True
    game_field[right_leg_row][right_leg_col]['soldier'] = True


def solder_move(game_state, game_field):
    if game_state["solder_move_left"] and soldier_position[0][1] != 0:
        game_field[soldier_position[0][0]][soldier_position[0][1]]['soldier'] = False
        game_field[soldier_position[1][0]][soldier_position[1][1]]['soldier'] = False

        soldier_position[0][1] -= 1
        soldier_position[1][1] -= 1

    if game_state["solder_move_right"] and soldier_position[0][1] != len(game_field[0]) - 2:
        game_field[soldier_position[0][0]][soldier_position[0][1]]['soldier'] = False
        game_field[soldier_position[1][0]][soldier_position[1][1]]['soldier'] = False

        soldier_position[0][1] += 1
        soldier_position[1][1] += 1

    if game_state["solder_move_up"] and soldier_position[0][0] != consts.SOLDIER_SIZE_BY_HEIGHT_IN_CELLS:
        game_field[soldier_position[0][0]][soldier_position[0][1]]['soldier'] = False
        game_field[soldier_position[1][0]][soldier_position[1][1]]['soldier'] = False

        soldier_position[0][0] -= 1
        soldier_position[1][0] -= 1

    if game_state["solder_move_down"] and soldier_position[0][0] != len(game_field) - 1:
        game_field[soldier_position[0][0]][soldier_position[0][1]]['soldier'] = False
        game_field[soldier_position[1][0]][soldier_position[1][1]]['soldier'] = False

        soldier_position[0][0] += 1
        soldier_position[1][0] += 1

    game_state["solder_move_left"] = False
    game_state["solder_move_right"] = False
    game_state["solder_move_up"] = False
    game_state["solder_move_down"] = False

"""
Player character detection module.
Will contain (among other things):
.1. Player image.
.2. Player position relative to its upper left corner.
.3. Methods for calculating the position of the character's legs and body (to check for contact with a mine/flag).
.4. Checking that the character does not go beyond the boundaries of the game window.
"""
