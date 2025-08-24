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

explosion_image = pygame.image.load(consts.EXPLOSION_IMAGE)
explosion_image = pygame.transform.scale(explosion_image, consts.EXPLOSION_SIZE)

flag_image = pygame.image.load(consts.FLAG_IMAGE)
flag_image = pygame.transform.scale(flag_image, consts.FLAG_SIZE)


def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)



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

    for bush in bush_list:
        bush_row, bush_col = bush
        screen.blit(bush_image, (game_field[bush_row][bush_col]["center_x"], game_field[bush_row][bush_col]["center_y"]))



def scan_vision(game_state, game_field, mine_list):
    cell_size = consts.CELL
    """
    this function in feautures have to get list of mines
    here we will draw all bushes
    we will use cicle 'for' and write coordinate
    """
    left_leg, right_leg = Soldier.solder_position
    left_leg_row, left_leg_col = left_leg

    screen.blit(night_solder_image, (game_field[left_leg_row][left_leg_col]['center_x'],
                                     game_field[left_leg_row][left_leg_col]['center_y'] -
                                     cell_size * consts.SOLDER_SIZE_BY_HEIGHT_IN_CELLS))


    for mine in mine_list:
        bush_row, bush_col = mine[0], mine[1]
        screen.blit(mine_image, (game_field[bush_row][bush_col]["center_x"], game_field[bush_row][bush_col]["center_y"]))


    for row in game_field:
        for col in row:
            x = col["center_x"]
            y = col["center_y"]
            pygame.draw.rect(screen, (255, 255, 255), (x, y, cell_size, cell_size), 1)


    if not game_state["is_last_time_scan_mode_activated"]:
        pygame.time.set_timer(pygame.USEREVENT, 1000)


def draw_flag(game_field):
    flag_row_start_point, flag_col_start_point = consts.FLAG_PLACEMENT[0]
    screen.blit(flag_image, (game_field[flag_row_start_point][flag_col_start_point]["center_x"],
                             game_field[flag_row_start_point][flag_col_start_point]["center_y"]))


def draw_explosion(game_field, exploding_mine):
    row_explosion, col_explosion = exploding_mine[2:4]
    print("blyaaaa 91 errroooors")
    screen.blit(explosion_image, (game_field[row_explosion][col_explosion]))


def draw_game(game_state, game_field, bush_list, mine_list, solder_position):
    if not game_state["is_scan_mode_activated"]:
        screen.fill(consts.BACKGROUND_COLOR)
        draw_flag(game_field)
        draw_bush_and_solder(game_field, bush_list)

        if game_state["is_explosion"]:
            draw_explosion(game_field, solder_position)

    else:
        screen.fill(consts.BLACK)
        scan_vision(game_state, game_field, mine_list)

    pygame.display.flip()



"""
A module for managing the Pygame main screen.
This module will contain a variable for the Pygame main screen and all the methods for drawing
objects on the screen.
"""
