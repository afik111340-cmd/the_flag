import pandas as pd
import ast


def save_progress(name_file, game_state, game_field, solder_position, bush_list, mine_list, flag_position):

    df = pd.Series([game_state, game_field, solder_position, bush_list, mine_list, flag_position],
                   index=["game_state", "game_field", "solder_position", "bush_list", "mine_list", "flag_position"])

    df.to_csv(f'{name_file}.csv')


def load_save(name_file):
    print("="*200)

    df = pd.read_csv(f'{name_file}.csv')
    data_dict = df.to_dict(orient='index')
    list_of_game_progress = []
    for key in data_dict.keys():
        list_of_game_progress.append((ast.literal_eval(data_dict[key]['0'])))

    for i in list_of_game_progress:
        print(i)

    return list_of_game_progress



# list of name, degree, score
# nme = ["aparna", "pankaj", "sudhir", "Geeku"]
# deg = ["MBA", "BCA", "M.Tech", "MBA"]
# scr = [90, 40, 80, 99]
#
# # dictionary of lists
# dict = {'name': nme, 'degree': deg, 'score': scr}
#
# df = pd.DataFrame(dict)
#
# df.to_csv('file1.csv')

# df.to_csv('file2.csv', header=False, index=False)