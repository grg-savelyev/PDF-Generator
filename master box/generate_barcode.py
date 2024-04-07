import barcode
from barcode.writer import ImageWriter


def generate_ean13(ean_num) -> str:
    """генерирует png изображение ШК, возвращает ссылку на него или имя"""
    ean13 = barcode.get_barcode_class('ean13-guard')
    my_ean = ean13(str(ean_num), writer=ImageWriter())
    fullname = my_ean.save('ean13_barcode')
    return fullname
