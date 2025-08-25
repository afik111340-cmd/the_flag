import pandas as pd
import ast
import os


def save_progress(name_file, game_state, game_field, solder_position, bush_list, mine_list, flag_position, dino_position):
    if not os.path.exists(f"saves"):
        os.makedirs('saves', exist_ok=True)

    df = pd.Series([game_state, game_field, solder_position, bush_list, mine_list, flag_position, dino_position],
                   index=["game_state", "game_field", "solder_position", "bush_list", "mine_list", "flag_position", "dino_position"])

    df.to_csv(f'saves/{name_file}.csv')


def load_save(name_file) -> list or bool:

    if not os.path.exists(f"saves"):
        os.makedirs('saves', exist_ok=True)

    if os.path.isfile(f"saves/{name_file}.csv"):
        df = pd.read_csv(f'saves/{name_file}.csv')
        data_dict = df.to_dict(orient='index')
        list_of_game_progress = []
        for key in data_dict.keys():
            list_of_game_progress.append((ast.literal_eval(data_dict[key]['0'])))
        return list_of_game_progress

    else:
        print("Error, the entered does not exist")
        return False

