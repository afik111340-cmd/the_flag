import pygame

import Screen
import Soldier
import Game_field
import consts

game_state = {
    "is_window_open": True,
    "state": consts.RUNNING_STATE,
    "choice_of_difficulty_level_is_made": False,
    "is_scan_mode_activated": False,
    "is_last_time_scan_mode_activated": False,
    "game_running": True,
    "is_lose": False,
    "is_win": False,
    "is_it_finish": False,
    "is_explosion": False,
    "solder_move_left": False,
    "solder_move_right": False,
    "solder_move_up": False,
    "solder_move_down": False
}



def main():
    pygame.init()
    pygame.display.set_caption("The Flag")

    Soldier.solder_position = consts.SOLDIER_START_PLACEMENT
    game_field = Game_field.game_field
    Soldier.set_solder_position(game_field)
    # показываем окно, пока пользователь не нажмет кнопку "Закрыть"
    while game_state["is_window_open"]:
        game_state["solder_move_left"] = False
        game_state["solder_move_right"] = False
        game_state["solder_move_up"] = False
        game_state["solder_move_down"] = False

        solder_position = Soldier.solder_position
        handle_user_events()

        if not game_state["is_explosion"] and not game_state["is_win"]:

            if game_state["solder_move_left"] or game_state["solder_move_right"] \
                    or game_state["solder_move_up"] or game_state["solder_move_down"]:

                Soldier.solder_move(game_state, game_field)

            if Game_field.check_if_got_exploded(solder_position):
                game_state["is_explosion"] = True
                game_state["is_lose"] = True
                print(Game_field.what_mine_exploded)

            Screen.draw_game(game_state, game_field, Game_field.bush_in_field, Game_field.mine_in_field, Game_field.what_mine_exploded)

            if game_state["is_scan_mode_activated"]:
                game_state["is_last_time_scan_mode_activated"] = True
            if Game_field.check_if_got_to_flag(solder_position):
                game_state["is_win"] = True

        else:
            Screen.draw_game(game_state, game_field, Game_field.bush_in_field, Game_field.mine_in_field,
                             Game_field.what_mine_exploded)
            game_state["is_it_finish"] = True


def handle_user_events():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and not game_state["is_last_time_scan_mode_activated"]:
                game_state["is_scan_mode_activated"] = True

            if not game_state["is_scan_mode_activated"]:

                if event.key == pygame.K_LEFT:
                    game_state["solder_move_left"] = True

                if event.key == pygame.K_RIGHT:
                    game_state["solder_move_right"] = True

                if event.key == pygame.K_UP:
                    game_state["solder_move_up"] = True

                if event.key == pygame.K_DOWN:
                    game_state["solder_move_down"] = True

        if event.type == pygame.USEREVENT:
            game_state["is_scan_mode_activated"] = False

        if event.type == pygame.QUIT or event.type == 999:
            game_state["is_window_open"] = False

        if event.type == pygame.MOUSEMOTION:
            pass

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pass



if __name__ == "__main__":
    main()