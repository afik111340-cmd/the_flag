import pygame

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
    window_size = (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT)
    pygame.display.set_caption("The Flag")

    screen = pygame.display.set_mode(window_size)
    background_color = consts.BACKGROUND_COLOR

    screen.fill(background_color)



    # показываем окно, пока пользователь не нажмет кнопку "Закрыть"
    while game_state["is_window_open"]:
        handle_user_events()
        pygame.display.flip()




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