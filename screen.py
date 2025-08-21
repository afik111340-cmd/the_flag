import pygame
import consts
import Soldier
import Game_field


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


def draw_bush_and_solder():
    """
    this function in feautures have to get list of bushes
    here we will draw all bushes
    we will use cicle for and write coordinate
    """
    screen.blit(solder_image, Soldier.solder_position)
    screen.blit(bush_image, (80, 80))


def scan_vision():
    """
    this function in feautures have to get list of mines
    here we will draw all bushes
    we will use cicle 'for' and write coordinate
    """
    screen.blit(night_solder_image, Soldier.solder_position)
    screen.blit(mine_image, (70, 150))


def draw_game(game_state):
    if not game_state["is_scan_mode_activated"]:
        screen.fill(consts.BACKGROUND_COLOR)
        draw_bush_and_solder()
    else:
        screen.fill(consts.BLACK)
        scan_vision()
        pass

    pygame.display.flip()



"""
A module for managing the Pygame main screen.
This module will contain a variable for the Pygame main screen and all the methods for drawing
objects on the screen.
"""
