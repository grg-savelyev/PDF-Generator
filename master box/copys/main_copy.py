import jinja2
import pdfkit
# from datetime import datetime
import images_base64
from images_base64 import image_to_base64
import generate_barcode


image_hb = images_base64.image_hb
image_eac = images_base64.image_eac

ean_13 = image_to_base64(generate_barcode.generate_ean13(4690624062827))

size = "86-92"
color_ru = "ЧЁРНЫЙ"
color_en = "BLACK"
item_number = "88501"
item_ru = "ФУТБОЛКА ДЕТСКАЯ"
item_en = "CHILDREN'S T-SHIRT"
materials_ru = "ХЛОПОК"
materials_en = "COTTON"
manufacturer = "SUNTEX IMPORT & EXPORT TRADING CO., LTD. («САНТЕКС ИМПОРТ ЭНД ЭКСПОРТ ТРЕЙДИНГ КО, ЛТД»). RM NO. " \
               "1106-1108, ZHONGYUAN BUILDING NO.368 NORTH YOUYI STREET, SHIJIAZHUANG HEBEI PROVINCE, CHINA (ОФ. " \
               "1106-1108, ЧЖУНЮАНЬ БИЛДИНГ №368 НОРФ ЮИ СТРИТ, ШИЦЗЯЧЖУАН ХЭБЕЙ ПРОВИНС, КИТАЙ)."
date_of_manufacture = "06.2022"

# today_date = datetime.today().strftime("%d %b, %Y")

context = {'item_en': item_en, 'item_ru': item_ru, 'materials_en': materials_en, 'materials_ru': materials_ru,
           'manufacturer': manufacturer, 'date_of_manufacture': date_of_manufacture, 'item_number': item_number,
           'size': size, 'color_en': color_en, 'color_ru': color_ru, 'url_image_hb': image_hb,
           'url_image_eac': image_eac, 'url_image_ean13': ean_13}

template_loader = jinja2.FileSystemLoader('./')
template_env = jinja2.Environment(loader=template_loader)

html_template = 'master box.html'
template = template_env.get_template(html_template)
output_text = template.render(context)

config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
output_pdf = 'master box.pdf'
pdfkit.from_string(output_text, output_pdf, configuration=config, css='master box.css')
