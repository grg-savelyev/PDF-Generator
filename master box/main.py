import os
from datetime import datetime
from create_dict_from_google import open_sheet
import generate_barcode
import create_pdf


def start_time():
    current_time = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    return current_time


def main():
    print('Укажите путь к папке для сохранения файлов:')
    folder_path = 'result_generation'  # input().strip()
    print('Запуск обработки.\n')

    start_folder_path = os.path.join(folder_path, start_time())
    os.makedirs(start_folder_path)

    # создание словаря мастер короб
    master_box_dict = open_sheet()

    # генерация EAN13
    barcodes_path = generate_barcode.generate_ean13_svg(start_folder_path, master_box_dict)
    # генерация PDF
    create_pdf.generation(start_folder_path, barcodes_path, master_box_dict)

    print('Обработка завершена')


if __name__ == "__main__":
    main()
