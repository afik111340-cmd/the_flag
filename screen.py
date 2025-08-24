import pygame
import consts
import Soldier
# import Game_field


screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
solder_image = pygame.image.load(consts.SOLDIER_IMAGE)
solder_image = pygame.transform.scale(solder_image, consts.SOLDER_SIZE)

night_solder_image = pygame.image.load(consts.SOLDER_NIGHT_IMAGE)
night_solder_image = pygame.transform.scale(night_solder_image, consts.SOLDER_SIZE)

bush_image = pygame.image.load(consts.BUSH_IMAGE)
bush_image = pygame.transform.scale(bush_image, consts.BUSH_SIZE)

mine_image = pygame.image.load(consts.MINE_IMAGE)
mine_image = pygame.transform.scale(mine_image, consts.MINE_SIZE)


def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)


def draw_field(field):
    pass


def draw_bush_and_solder(game_field, bush_list):
    """
    this function in feautures have to get list of bushes
    here we will draw all bushes
    we will use cicle for and write coordinate
    """
    left_leg, right_leg = Soldier.solder_position
    left_leg_row, left_leg_col = left_leg

    screen.blit(solder_image, (game_field[left_leg_row][left_leg_col]['center_x'],
                               game_field[left_leg_row][left_leg_col]['center_y'] - consts.CELL*consts.SOLDER_SIZE_BY_HEIGHT_IN_CELLS))
    screen.blit(bush_image, (80, 80))


def scan_vision(game_state, game_field, mine_list):
    """
    this function in feautures have to get list of mines
    here we will draw all bushes
    we will use cicle 'for' and write coordinate
    """
    left_leg, right_leg = Soldier.solder_position
    left_leg_row, left_leg_col = left_leg

    screen.blit(night_solder_image, (game_field[left_leg_row][left_leg_col]['center_x'],
                               game_field[left_leg_row][left_leg_col][
                                   'center_y'] - consts.CELL * consts.SOLDER_SIZE_BY_HEIGHT_IN_CELLS))

    screen.blit(mine_image, (70, 150))
    screen.blit(mine_image, (270, 350))
    if not game_state["is_last_time_scan_mode_activated"]:
        pygame.time.set_timer(pygame.USEREVENT, 1000)


def draw_game(game_state, game_field, bush_list, mine_list):
    if not game_state["is_scan_mode_activated"]:
        screen.fill(consts.BACKGROUND_COLOR)
        draw_bush_and_solder(game_field, bush_list)
    else:
        screen.fill(consts.BLACK)
        scan_vision(game_state, mine_list)

    pygame.display.flip()



"""
A module for managing the Pygame main screen.
This module will contain a variable for the Pygame main screen and all the methods for drawing
objects on the screen.
"""
