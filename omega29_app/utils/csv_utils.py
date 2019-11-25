import csv
import os
import json
from flask import current_app
from omega29_app.utils.text_utils import escape_text


def page_components_to_csv():

    target_csv_filename = os.path.join(
        current_app.instance_path,
        'data.csv'
    )

    source_json_filename = os.path.join(
        current_app.root_path,
        'data',
        'pages.json'
    )

    with open(source_json_filename) as json_file:
        pages = json.load(json_file)

    with open(target_csv_filename, 'w', newline='') as csv_file:
        fieldnames = [
            'page_name',
            'page_component_type',
            'page_section_number',
            'order_number',
            'content',
            'language'
        ]

        csv_writer = csv.DictWriter(
            csv_file,
            fieldnames=fieldnames,
            delimiter=','
        )

        csv_writer.writeheader()

        for page in pages:

            source_data_dir = os.path.join(
                current_app.root_path,
                *(page['data_dir'].split('/'))
            )

            os.chdir(source_data_dir)

            file_names = os.listdir()

            for file_name in file_names:

                page_conponent_data = file_name.split('-')

                csv_row_data = {
                    'page_section_number': page_conponent_data[0],
                    'order_number': page_conponent_data[1],
                    'page_component_type': page_conponent_data[2],
                    'page_name': page['name']
                }

                if csv_row_data['page_component_type'] == 'code':
                    csv_row_data['language'] = page_conponent_data[-1]

                with open(file_name, 'r', encoding='utf-8') as data_file:
                    content = data_file.read()
                    csv_row_data['content'] = escape_text(content)

                csv_writer.writerow(csv_row_data)
