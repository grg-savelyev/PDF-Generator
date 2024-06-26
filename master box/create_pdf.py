import jinja2
import pdfkit
import images_base64
import os
import xml.dom.minidom


def create_pdf(barcodes_path, key, value):
    image_hb = images_base64.image_hb
    image_eac = images_base64.image_eac

    svg_path = fr'{barcodes_path}\{key}.svg'

    # читаем содержимое SVG файла
    with open(svg_path, "r") as file:
        svg_content = file.read()

    # Преобразуем SVG в XML
    dom = xml.dom.minidom.parseString(svg_content)
    xml_content = dom.toprettyxml()

    size = value[9]
    color_ru = value[3].upper()
    color_en = value[4].upper()
    item_number = value[0]
    item_ru = value[1].upper()
    item_en = value[2].upper()
    materials_ru = value[5].upper()
    materials_en = value[6].upper()
    manufacturer = value[7].upper()
    date_of_manufacture = value[8]
    name_pdf = f'{item_number}, {size}, {color_en}'

    context, name_pdf = {'item_en': item_en, 'item_ru': item_ru, 'materials_en': materials_en,
                         'materials_ru': materials_ru,
                         'manufacturer': manufacturer, 'date_of_manufacture': date_of_manufacture,
                         'item_number': item_number,
                         'size': size, 'color_en': color_en, 'color_ru': color_ru, 'url_image_hb': image_hb,
                         'url_image_eac': image_eac, 'svg_image': xml_content}, name_pdf

    return context, name_pdf


def generation(start_folder_path, barcodes_path, master_box_dict: dict):
    template_loader = jinja2.FileSystemLoader('./')
    template_env = jinja2.Environment(loader=template_loader)

    html_template = 'master box.html'
    template = template_env.get_template(html_template)

    master_box_folder_path = os.path.join(start_folder_path, 'PDF master box')
    os.makedirs(master_box_folder_path)

    for key, value in master_box_dict.items():
        context, name_pdf = create_pdf(barcodes_path, key, value)
        print(name_pdf)
        output_text = template.render(context)
        config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')

        output_pdf = fr'{master_box_folder_path}\{name_pdf}.pdf'
        pdfkit.from_string(output_text, output_pdf, configuration=config, css='master box.css')
        print(f'{name_pdf} сгенерирован')
