import os
import csv
import json

from flask import current_app

from omega29_app import db
from omega29_app.models import (
    TreeNodeType, TreeNode, PageComponentType, PageComponent, Language
)


def create_tables():
    db.drop_all()
    db.create_all()


def insert_tree_node_types():
    db.session.add(TreeNodeType(name='folder'))
    db.session.add(TreeNodeType(name='page'))
    db.session.commit()


def insert_tree_nodes(node_type):

    if node_type == 'folder':
        json_file = 'folders.json'
    elif node_type == 'page':
        json_file = 'pages.json'

    file_name = os.path.join(
        current_app.root_path,
        'data',
        json_file
    )

    with open(file_name) as f:
        nodes = json.load(f)

    node_type = TreeNodeType.query.filter_by(name=node_type).first()

    for node in nodes:
        name = node['name']
        if '/' in name:
            parent_name = name[:name.rfind('/')]
            parent_id = TreeNode.query.filter_by(name=parent_name).first().id
        else:
            parent_id = None

        db.session.add(
            TreeNode(
                name=name,
                parent_id=parent_id,
                type_id=node_type.id,
                endpoint=node['endpoint']
            )
        )

    db.session.commit()


def insert_page_component_types():
    db.session.add(PageComponentType(name='h3'))
    db.session.add(PageComponentType(name='h5'))
    db.session.add(PageComponentType(name='code'))
    db.session.add(PageComponentType(name='paragraph'))
    db.session.commit()


def insert_languages():
    db.session.add(Language(name='python'))
    db.session.add(Language(name='bash'))
    db.session.commit()


def insert_page_components():

    source_csv_file = os.path.join(
        current_app.instance_path,
        'data.csv'
    )

    with open(source_csv_file) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')

        for line in csv_reader:
            page_name = line["page_name"]
            page_component_type = line["page_component_type"]
            page_section_number = line["page_section_number"]
            order_number = line["order_number"]
            content = line["content"]
            language = line['language']

            page_id = TreeNode.query.filter_by(name=page_name).first().id
            page_component_type_id = PageComponentType.query.filter_by(
                name=page_component_type
            ).first().id
            lang_id = None

            if language:
                lang_id = Language.query.filter_by(name=language).first().id

            db.session.add(
                PageComponent(
                    page_section_number=page_section_number,
                    order_number=order_number,
                    content=content,
                    page_id=page_id,
                    page_component_type_id=page_component_type_id,
                    language_id=lang_id
                )
            )

    db.session.commit()
