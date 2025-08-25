import pandas as pd
import ast


def save_progress(name_file, game_state, game_field, solder_position, bush_list, mine_list, flag_position):

    df = pd.Series([game_state, game_field, solder_position, bush_list, mine_list, flag_position],
                   index=["game_state", "game_field", "solder_position", "bush_list", "mine_list", "flag_position"])

    df.to_csv(f'{name_file}.csv')


def load_save(name_file) -> list:

    df = pd.read_csv(f'{name_file}.csv')
    data_dict = df.to_dict(orient='index')
    list_of_game_progress = []
    for key in data_dict.keys():
        list_of_game_progress.append((ast.literal_eval(data_dict[key]['0'])))

    return list_of_game_progress
