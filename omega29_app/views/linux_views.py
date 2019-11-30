from flask import Blueprint
from omega29_app.utils.web_utils import get_list, get_page

bp = Blueprint('linux', __name__, url_prefix='/linux')


@bp.route('/')
def home():
    return get_list(node_name='Home/Linux')


### lfcs ######################################################################

@bp.route('/lfcs/')
def lfcs():
    return get_list(node_name='Home/Linux/LFCS')


@bp.route('/lfcs/01_essential_commands')
def lfcs_01_essential_commands():
    return get_page(node_name='Home/Linux/LFCS/01 Essential Commands')


@bp.route('/lfcs/02_operation_of_running_systems')
def lfcs_02_operation_of_running_systems():
    node_name = 'Home/Linux/LFCS/02 Operation of Running Systems'
    return get_page(node_name=node_name)
