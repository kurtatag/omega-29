from flask import render_template, request
from omega29_app.models import TreeNode, TreeNodeType, PageComponent
from omega29_app.utils.text_utils import (
    unescape_text, get_id_for_header
)


def get_child_nodes(parent_id):
    nodes = []

    for node in TreeNode.query.filter_by(parent_id=parent_id).all():
        node_name = node.name[node.name.rfind('/') + 1 :]
        node_type = TreeNodeType.query.filter_by(id=node.type_id).first().name

        nodes.append(
            {
                "name": node_name,
                "type": node_type,
                "endpoint": node.endpoint,
                "children": len(node.child_nodes)
            }
        )

    return nodes


def get_breadcrumb_items(node_name, breadcrumb_items):

    if '/' not in node_name:
        endpoint = TreeNode.query.filter_by(name=node_name).first().endpoint

        breadcrumb_items.append(
            {
                "name": node_name,
                "endpoint": endpoint
            }
        )

        return

    else:
        endpoint = TreeNode.query.filter_by(name=node_name).first().endpoint
        parent_name = node_name[:node_name.rfind('/')]

        breadcrumb_items.append(
            {
                "name": node_name[node_name.rfind('/') + 1 :],
                "endpoint": endpoint
            }
        )

        get_breadcrumb_items(parent_name, breadcrumb_items)


def get_list(node_name):
    current_node = TreeNode.query.filter_by(name=node_name).first()

    nodes = get_child_nodes(parent_id=current_node.id)

    breadcrumb_items = []
    get_breadcrumb_items(current_node.name, breadcrumb_items)

    context = {
        "nodes": sorted(nodes, reverse=True, key=lambda x: x["children"]),
        "breadcrumb_items": breadcrumb_items[::-1]
    }

    return render_template('nodes_list.html', **context)


def get_page(node_name):

    breadcrumb_items = []
    toc_items = []  # toc = table of contents
    data = {}  # the actual content of the page

    get_breadcrumb_items(node_name, breadcrumb_items)

    page = TreeNode.query.filter_by(name=node_name).first()
    components = PageComponent.query.filter_by(page_id=page.id).all()

    for c in components:
        section = c.page_section_number
        order = c.order_number
        type = c.page_component_type.name
        content = unescape_text(c.content)

        if section not in data:
            data[section] = {}

        data[section][order] = {
            'type': type,
            'content': content
        }

        if type == 'code':
            data[section][order]['lang'] = c.language.name

        if type == 'h3' or type == 'h5':
            header_id = get_id_for_header(content)
            data[section][order]['id'] = header_id

            if type == 'h3':
                toc_items.append(
                    {
                        'link_href': f'#{header_id}',
                        'link_text': content,
                        'children': []
                    }
                )
            elif type == 'h5':
                toc_items[-1]['children'].append(
                    {
                        'link_href': f'#{header_id}',
                        'link_text': content
                    }
                )

    context = {
        'data': data,
        'toc_items': toc_items,
        "breadcrumb_items": breadcrumb_items[::-1]
    }

    return render_template('page.html', **context)


def get_search():

    breadcrumb_items = []
    get_breadcrumb_items('Home', breadcrumb_items)

    q = request.args.get('q')

    search = f"%{q.lower()}%"
    search_filter = PageComponent.content.like(search)
    components = PageComponent.query.filter(search_filter).all()

    intermediate_data = {}
    for c in components:
        n = c.content.lower().count(q.lower())
        if c.page.name in intermediate_data:
            intermediate_data[c.page.name]['occurrences'] += n
        else:
            intermediate_data[c.page.name] = {
                'endpoint': c.page.endpoint,
                'occurrences': n
            }

    data = []
    for k, v in intermediate_data.items():
        data.append(
            {
                'page_name': k[5:],
                'endpoint': v['endpoint'],
                'occurrences': v['occurrences']
            }
        )

    context = {
        "breadcrumb_items": breadcrumb_items[::-1],
        "q": q,
        "data": sorted(data, reverse=True, key=lambda x: x["occurrences"])
    }

    return render_template('search.html', **context)
