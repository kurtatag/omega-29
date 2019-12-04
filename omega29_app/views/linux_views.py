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


@bp.route('/lfcs/03_user_and_group_management')
def lfcs_03_user_and_group_management():
    node_name = 'Home/Linux/LFCS/03 User and Group Management'
    return get_page(node_name=node_name)


@bp.route('/lfcs/04_networking')
def lfcs_04_networking():
    return get_page(node_name='Home/Linux/LFCS/04 Networking')


@bp.route('/lfcs/05_service_configuration')
def lfcs_05_service_configuration():
    return get_page(node_name='Home/Linux/LFCS/05 Service Configuration')


@bp.route('/lfcs/06_storage_management')
def lfcs_06_storage_management():
    return get_page(node_name='Home/Linux/LFCS/06 Storage Management')
