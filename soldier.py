import consts

solder_position = []


def solder_move(game_state):
    if game_state["solder_move_left"]:
        solder_position[0] -= consts.CELL

    if game_state["solder_move_right"]:
        solder_position[0] += consts.CELL

    if game_state["solder_move_up"]:
        solder_position[1] -= consts.CELL

    if game_state["solder_move_down"]:
        solder_position[1] += consts.CELL



"""
Player character detection module.
Will contain (among other things):
.1. Player image.
.2. Player position relative to its upper left corner.
.3. Methods for calculating the position of the character's legs and body (to check for contact with a mine/flag).
.4. Checking that the character does not go beyond the boundaries of the game window.
"""
