import barcode
from barcode import EAN13_GUARD
from barcode.writer import SVGWriter, ImageWriter
import os


def generate_ean13_svg(start_folder_path, master_box_dict: dict):
    """генерирует svg изображение ШК, возвращает на папку"""

    barcodes_path = os.path.join(start_folder_path, 'Barcodes')
    os.makedirs(barcodes_path)

    for ean_num in master_box_dict.keys():
        fullname = fr'{barcodes_path}\{ean_num}.svg'
        with open(fullname, 'wb') as f:
            EAN13_GUARD(str(ean_num), writer=SVGWriter()).write(f)

    return barcodes_path


# def generate_ean13_png(ean_num) -> str:
#     """генерирует png изображение ШК, возвращает ссылку на него"""
#     ean13 = barcode.get_barcode_class('ean13-guard')
#     my_ean = ean13(str(ean_num), writer=ImageWriter())
#     fullname = my_ean.save(f'images_EAN13_GUARD/{ean_num}')
#     return fullname
