import pygame

import consts
import Soldier

screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))



def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)


image = pygame.image.load(consts.SOLDIER_IMAGE)
image = pygame.transform.scale(image, consts.SOLDER_SIZE)


def draw_game():
    screen.fill(consts.BACKGROUND_COLOR)
    screen.blit(image, Soldier.solder_position)
    pygame.display.flip()



"""
A module for managing the Pygame main screen.
This module will contain a variable for the Pygame main screen and all the methods for drawing
objects on the screen.
"""
