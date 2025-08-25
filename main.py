import pygame
import time
import Screen
import Soldier
import Game_field
import Database
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
    "need_print_starting_message": True,
    "save_progress": 0,
    "load_progress": 0,
    "solder_move_left": False,
    "solder_move_right": False,
    "solder_move_up": False,
    "solder_move_down": False
}

time_list = []
save_num_list = {pygame.K_1: 1,
                 pygame.K_2: 2,
                 pygame.K_3: 3,
                 pygame.K_4: 4,
                 pygame.K_5: 5,
                 pygame.K_6: 6,
                 pygame.K_7: 7,
                 pygame.K_8: 8,
                 pygame.K_9: 9
                 }




def main():
    global game_state
    pygame.init()
    pygame.display.set_caption("The Flag")

    Game_field.init_game_field()
    game_field = Game_field.game_field

    Soldier.solder_position = consts.SOLDIER_START_PLACEMENT
    Soldier.set_solder_starting_position(game_field)

    # Game_field.print_mateix(game_field)
    # показываем окно, пока пользователь не нажмет кнопку "Закрыть"
    while game_state["is_window_open"]:
        game_state["solder_move_left"] = False
        game_state["solder_move_right"] = False
        game_state["solder_move_up"] = False
        game_state["solder_move_down"] = False

        if game_state["load_progress"]:
            game_state["load_progress"] = 0
        if game_state["save_progress"]:
            game_state["save_progress"] = 0

        game_field = Game_field.game_field
        soldier_position = Soldier.soldier_position

        handle_user_events()

        if game_state["save_progress"]:
            print("save_progress")
            Database.save_progress(game_state["save_progress"], game_state, game_field, soldier_position,
                                   Game_field.bush_in_field, Game_field.mine_in_field, consts.FLAG_PLACEMENT)
            continue
        if game_state["load_progress"]:
            print("load_progress")
            data_from_save = Database.load_save(game_state["load_progress"])
            (game_state, Game_field.game_field, Soldier.soldier_position, Game_field.bush_in_field, Game_field.mine_in_field,
             consts.FLAG_PLACEMENT) = data_from_save
            continue

        if not game_state["is_explosion"] and not game_state["is_win"]:

            if game_state["solder_move_left"] or game_state["solder_move_right"] \
                    or game_state["solder_move_up"] or game_state["solder_move_down"]:
                Soldier.solder_move(game_state, game_field)

            if Game_field.check_if_got_exploded(soldier_position):
                game_state["is_explosion"] = True
                game_state["is_lose"] = True

            Screen.draw_game(game_state, game_field, Game_field.bush_in_field, Game_field.mine_in_field,
                             Game_field.what_mine_exploded)

            if game_state["is_scan_mode_activated"]:
                game_state["is_last_time_scan_mode_activated"] = True
            if Game_field.check_if_got_to_flag(soldier_position):
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

            if event.key in save_num_list:
                how_long_press(event.key, 'start')

        if event.type == pygame.KEYUP:
            if event.key in save_num_list:
                tt = how_long_press(event.key, 'stop')
                if save_or_load_file(tt) == "load":
                    game_state["load_progress"] = save_num_list[event.key]
                else:
                    game_state["save_progress"] = save_num_list[event.key]



        if event.type == pygame.USEREVENT:
            game_state["is_scan_mode_activated"] = False

        if event.type == 998:
            game_state["need_print_starting_message"] = False

        if event.type == pygame.QUIT or event.type == 999:
            game_state["is_window_open"] = False

        if event.type == pygame.MOUSEMOTION:
            pass

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pass


def how_long_press(file_key, to_do):
    if to_do == 'start':
        time_list.append(time.time())

    if to_do == 'stop':
        t = time_list[0]
        t = time.time() - t
        t = str(t)
        t = t[:5]
        print("You pressed key for", t, 'seconds')
        time_list.clear()
        return t


def save_or_load_file(t):
    save_or_load = ''
    if float(t) > 1:
        save_or_load = 'save'
    if float(t) < 1:
        save_or_load = 'load'

    return save_or_load


if __name__ == "__main__":
    main()
