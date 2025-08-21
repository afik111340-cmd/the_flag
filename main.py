import pygame
import Screen
import Soldier
import consts

game_state = {
    "soldier_is_moving": False,
    "is_window_open": True,
    "state": consts.RUNNING_STATE,
    "choice_of_difficulty_level_is_made": False,
    "solder_move_left": False,
    "solder_move_right": False,
    "solder_move_up": False,
    "solder_move_down": False
}

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
CELL_HEIGHT = 124
CELL_WIDTH = 124
CELL_MARGIN = 1


def main():
    pygame.init()
    pygame.display.set_caption("The Flag")

    Soldier.solder_position = [50, 50]

    # показываем окно, пока пользователь не нажмет кнопку "Закрыть"
    while game_state["is_window_open"]:
        handle_user_events()

        if game_state["solder_move_left"] or game_state["solder_move_right"] \
            or game_state["solder_move_up"] or game_state["solder_move_down"]:
            Soldier.solder_move(game_state)

        Screen.draw_game()




def handle_user_events():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game_state["solder_move_left"] = True
            else:
                game_state["solder_move_left"] = False
            if event.key == pygame.K_RIGHT:
                game_state["solder_move_right"] = True
            else:
                game_state["solder_move_right"] = False
            if event.key == pygame.K_UP:
                game_state["solder_move_up"] = True
            else:
                game_state["solder_move_up"] = False
            if event.key == pygame.K_DOWN:
                game_state["solder_move_down"] = True
            else:
                game_state["solder_move_down"] = False
            # if event.key == pygame.K_RETURN:
            #     return True
        if event.type == pygame.QUIT:
            game_state["is_window_open"] = False

        if event.type == pygame.MOUSEMOTION:
            pass

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pass



if __name__ == "__main__":
    main()