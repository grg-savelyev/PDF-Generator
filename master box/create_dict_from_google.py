import gspread
import pandas as pd
from pprint import pprint


def master_box_dict(df) -> dict:
    new_dict = dict(zip(df['barcode'],
                        zip(df['item'], df['item_name_ru'], df['item_name_en'],
                            df['color_ru'], df['color_en'], df['material_ru'], df['material_en'],
                            df['manufacturer'], df['date'], df['size'],
                            df['name_folder'].str.replace(':', '_'))))
    return field_checking(new_dict)


def field_checking(new_dict):
    all_filled = all(all(value) for value in new_dict.values())
    if not all_filled:
        print(f'Словарь не заполнен или содержит пустые строки. Операция прервана.')

    return new_dict


gc = gspread.service_account(filename='creds.json')
wks = gc.open('InDesign').worksheet('label')
df = pd.DataFrame(wks.get_all_records())
master_box_dict = master_box_dict(df)

# pprint(master_box_dict)
