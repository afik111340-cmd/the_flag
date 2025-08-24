import consts

solder_position = []


def set_solder_position(game_field):
    global solder_position
    left_leg, right_leg = consts.SOLDIER_START_PLACEMENT
    left_leg_row, left_leg_col = left_leg
    right_leg_row, right_leg_col = right_leg

    solder_position = [[left_leg_row, left_leg_col], [right_leg_row, right_leg_col]]
    game_field[left_leg_row][left_leg_col]['soldier'] = True
    game_field[right_leg_row][right_leg_col]['soldier'] = True




def solder_move(game_state, game_field):

    if game_state["solder_move_left"] and solder_position[0][1] != 0:
        game_field[solder_position[0][0]][solder_position[0][1]]['soldier'] = False
        game_field[solder_position[1][0]][solder_position[1][1]]['soldier'] = False

        solder_position[0][1] -= 1
        solder_position[1][1] -= 1

    if game_state["solder_move_right"] and solder_position[0][1] != len(game_field[0]) - 2:
        game_field[solder_position[0][0]][solder_position[0][1]]['soldier'] = False
        game_field[solder_position[1][0]][solder_position[1][1]]['soldier'] = False

        solder_position[0][1] += 1
        solder_position[1][1] += 1

    if game_state["solder_move_up"] and solder_position[0][0] != consts.SOLDER_SIZE_BY_HEIGHT_IN_CELLS:
        game_field[solder_position[0][0]][solder_position[0][1]]['soldier'] = False
        game_field[solder_position[1][0]][solder_position[1][1]]['soldier'] = False

        solder_position[0][0] -= 1
        solder_position[1][0] -= 1

    if game_state["solder_move_down"] and solder_position[0][0] != len(game_field) - 1:
        game_field[solder_position[0][0]][solder_position[0][1]]['soldier']=False
        game_field[solder_position[1][0]][solder_position[1][1]]['soldier']=False

        solder_position[0][0] += 1
        solder_position[1][0] += 1


"""
Player character detection module.
Will contain (among other things):
.1. Player image.
.2. Player position relative to its upper left corner.
.3. Methods for calculating the position of the character's legs and body (to check for contact with a mine/flag).
.4. Checking that the character does not go beyond the boundaries of the game window.
"""
