import pygame
import consts

screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))



def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)



def draw_game():
    screen.fill(consts.BACKGROUND_COLOR)

    pygame.display.flip()



"""
A module for managing the Pygame main screen.
This module will contain a variable for the Pygame main screen and all the methods for drawing
objects on the screen.
"""
