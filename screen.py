import pygame
import consts
import Soldier
# import Game_field


screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

soldier_image = pygame.image.load(consts.SOLDIER_IMAGE)
soldier_image = pygame.transform.scale(soldier_image, consts.SOLDIER_SIZE)

damaged_soldier_image = pygame.image.load(consts.DAMAGED_SOLDIER_IMAGE)
damaged_soldier_image = pygame.transform.scale(damaged_soldier_image, consts.SOLDIER_SIZE)

night_soldier_image = pygame.image.load(consts.SOLDIER_NIGHT_IMAGE)
night_soldier_image = pygame.transform.scale(night_soldier_image, consts.SOLDIER_SIZE)

bush_image = pygame.image.load(consts.BUSH_IMAGE)
bush_image = pygame.transform.scale(bush_image, consts.BUSH_SIZE)

mine_image = pygame.image.load(consts.MINE_IMAGE)
mine_image = pygame.transform.scale(mine_image, consts.MINE_SIZE)

explosion_image = pygame.image.load(consts.EXPLOSION_IMAGE)
explosion_image = pygame.transform.scale(explosion_image, consts.EXPLOSION_SIZE)

flag_image = pygame.image.load(consts.FLAG_IMAGE)
flag_image = pygame.transform.scale(flag_image, consts.FLAG_SIZE)

dino_image = pygame.image.load(consts.DINO_IMAGE)
dino_image = pygame.transform.scale(dino_image, consts.DINO_SIZE)


activate_starting_message = True
starting_message_was_activated = False


def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)


def draw_start_message():
    global starting_message_was_activated, activate_starting_message

    draw_message(consts.WELCOME_FIRST_MESSAGE, consts.WELCOME_FONT_SIZE, consts.WELCOME_COLOR, consts.WELCOME_FIRST_LOCATION)
    draw_message(consts.WELCOME_SECOND_MESSAGE, consts.WELCOME_FONT_SIZE, consts.WELCOME_COLOR, consts.WELCOME_SECOND_LOCATION)

    if activate_starting_message and not starting_message_was_activated:
        pygame.time.set_timer(998, 3000)
        starting_message_was_activated = True


def draw_lose_message(game_state):
    draw_message(consts.LOSE_MESSAGE, consts.LOSE_FONT_SIZE,
                 consts.LOSE_COLOR, consts.LOSE_LOCATION)

    if game_state["is_lose"] and not game_state["is_it_finish"]:
        pygame.time.set_timer(999, 3000)


def draw_win_message(game_state):
    draw_message(consts.WIN_MESSAGE, consts.WIN_FONT_SIZE,
                 consts.WIN_COLOR, consts.WIN_LOCATION)

    if game_state["is_win"] and not game_state["is_it_finish"]:
        pygame.time.set_timer(999, 3000)


def draw_bush_and_solder(game_field, bush_list, image_soldier):
    """
    this function in feautures have to get list of bushes
    here we will draw all bushes
    we will use cicle for and write coordinate
    """
    left_leg, right_leg = Soldier.soldier_position
    left_leg_row, left_leg_col = left_leg

    screen.blit(image_soldier, (game_field[left_leg_row][left_leg_col]['center_x'],
                                game_field[left_leg_row][left_leg_col]['center_y'] - consts.CELL*consts.SOLDIER_SIZE_BY_HEIGHT_IN_CELLS))

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
    left_leg, right_leg = Soldier.soldier_position
    left_leg_row, left_leg_col = left_leg

    screen.blit(night_soldier_image, (game_field[left_leg_row][left_leg_col]['center_x'],
                                      game_field[left_leg_row][left_leg_col]['center_y'] -
                                      cell_size * consts.SOLDIER_SIZE_BY_HEIGHT_IN_CELLS))


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




def draw_explosion(game_field, exploding_mine, mine_list):
    row_explosion, col_explosion = exploding_mine[0], exploding_mine[1]

    # print((game_field[row_explosion-1][col_explosion-1]["center_x"],
    #        game_field[row_explosion][col_explosion]["center_y"]))
    # for mine in mine_list:
    #     bush_row, bush_col = mine[0], mine[1]
    #     screen.blit(mine_image, (game_field[bush_row][bush_col]["center_x"], game_field[bush_row][bush_col]["center_y"]))

    screen.blit(explosion_image, (game_field[row_explosion-2][col_explosion-1]["center_x"],
                                  game_field[row_explosion-2][col_explosion-1]["center_y"]))


def draw_dino(game_field, dino_position):
    left_leg, right_leg = dino_position
    left_leg_row, left_leg_col = left_leg

    screen.blit(dino_image, (game_field[left_leg_row][left_leg_col]['center_x'],
                             game_field[left_leg_row][left_leg_col]['center_y']
                             - consts.CELL*consts.DINO_SIZE_BY_HEIGHT_IN_CELLS))



def draw_game(game_state, game_field, bush_list, mine_list, mine_position):
    if not game_state["is_scan_mode_activated"]:
        screen.fill(consts.BACKGROUND_COLOR)

        if game_state["is_explosion"]:
            draw_bush_and_solder(game_field, bush_list, damaged_soldier_image)
            draw_explosion(game_field, mine_position, mine_list)
            draw_lose_message(game_state)
        else:
            draw_bush_and_solder(game_field, bush_list, soldier_image)
            if game_state["is_win"]:
                draw_win_message(game_state)

        if game_state["need_print_starting_message"]:
            draw_start_message()
        draw_dino()
        draw_flag(game_field)



    else:
        screen.fill(consts.BLACK)
        scan_vision(game_state, game_field, mine_list)

    pygame.display.flip()



"""
A module for managing the Pygame main screen.
This module will contain a variable for the Pygame main screen and all the methods for drawing
objects on the screen.
"""
