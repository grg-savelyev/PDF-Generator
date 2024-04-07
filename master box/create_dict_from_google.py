import gspread
import pandas as pd


def master_box_dict(df) -> dict:
    new_dict = dict(zip(df['ean_13'],
                        zip(df['size'], df['color_ru'], df['color_en'], df['item_number'], df['item_ru'],
                            df['item_en'], df['materials_ru'], df['materials_en'], df['manufacturer'],
                            df['date_of_manufacture'], df['name_folders'].str.replace(':', '_'))))
    return field_checking(new_dict)


def field_checking(new_dict):
    all_filled = all(all(value) for value in new_dict.values())
    if not all_filled:
        print(f'Словарь не заполнен или содержит пустые строки. Операция прервана.')

    return new_dict


gc = gspread.service_account(filename='creds.json')
wks = gc.open('МАТРИЦА ЛЕГПРОМ').worksheet('Master_box')
df = pd.DataFrame(wks.get_all_records())
master_box_dict = master_box_dict(df)
# print(master_box_dict)
