import os
from omega29_app import create_app
from omega29_app.utils import db_utils, csv_utils

app = create_app()

with app.app_context():

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    csv_utils.page_components_to_csv()

    db_utils.create_tables()
    db_utils.insert_tree_node_types()
    db_utils.insert_page_component_types()
    db_utils.insert_tree_nodes(node_type='folder')
    db_utils.insert_tree_nodes(node_type='page')
    db_utils.insert_languages()
    db_utils.insert_page_components()
