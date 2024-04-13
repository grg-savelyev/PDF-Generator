import gspread
import pandas as pd


def master_box(df) -> dict:
    data_dict = dict(zip(df['barcode'],
                         zip(df['item'], df['item_name_ru'], df['item_name_en'],
                             df['color_ru'], df['color_en'], df['material_ru'], df['material_en'],
                             df['manufacturer'], df['date'], df['size'],
                             df['name_folder'].str.replace(': ', '_'))))
    return dict_check(data_dict)


def dict_check(data_dict):
    all_filled = all(all(value) for value in data_dict.values())
    if not all_filled:
        print(f'Словарь {data_dict} не заполнен или содержит пустые строки. Операция прервана.')
        return None
    return data_dict


def open_sheet():
    gc = gspread.service_account(filename='creds.json')
    wks = gc.open('InDesign').worksheet('label')
    df = pd.DataFrame(wks.get_all_records())
    master_box_dict = master_box(df)
    return master_box_dict
