import pygame
import Screen
import consts

game_state = {
    "soldier_is_moving": False,
    "is_window_open": True,
    "state": consts.RUNNING_STATE,
    "choice_of_difficulty_level_is_made": False
}

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
CELL_HEIGHT = 124
CELL_WIDTH = 124
CELL_MARGIN = 1


def main():
    pygame.init()
    pygame.display.set_caption("The Flag")


    # показываем окно, пока пользователь не нажмет кнопку "Закрыть"
    while game_state["is_window_open"]:
        handle_user_events()
        pygame.display.flip()
        Screen.draw_game()




def handle_user_events():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return True
        if event.type == pygame.QUIT:
            game_state["is_window_open"] = False

        if event.type == pygame.MOUSEMOTION:
            pass

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pass



if __name__ == "__main__":
    main()