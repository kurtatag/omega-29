from flask import Blueprint
from omega29_app.utils.web_utils import get_list, get_page

bp = Blueprint('python', __name__, url_prefix='/python')


@bp.route('/')
def home():
    return get_list(node_name='Home/Python')


### core ######################################################################

@bp.route('/core/')
def core():
    return get_list(node_name='Home/Python/Python Core')


@bp.route('/core/file-io')
def core_file_io():
    return get_page(node_name='Home/Python/Python Core/File IO')


@bp.route('/core/comprehensions')
def core_comprehensions():
    return get_page(node_name='Home/Python/Python Core/Comprehensions')


@bp.route('/core/decorators')
def core_decorators():
    return get_page(node_name='Home/Python/Python Core/Decorators')


@bp.route('/core/truth-value-testing')
def core_truth_value_testing():
    return get_page(node_name='Home/Python/Python Core/Truth Value Testing')


@bp.route('/core/variable-scopes')
def core_variable_scopes():
    return get_page(node_name='Home/Python/Python Core/Variable Scopes')


### std-lib ###################################################################

@bp.route('/std-lib/')
def std_lib():
    return get_list(node_name='Home/Python/Python Standard Library')


@bp.route('/std-lib/csv')
def std_lib_csv():
    return get_page(node_name='Home/Python/Python Standard Library/CSV Module')


### algorithms ################################################################

@bp.route('/algorithms/')
def algorithms():
    return get_list(node_name='Home/Python/Data Structures & Algorithms')


### patterns ##################################################################

@bp.route('/patterns/')
def patterns():
    return get_list(node_name='Home/Python/Design Patterns')


### tricks ####################################################################

@bp.route('/tricks/')
def tricks():
    return get_list(node_name='Home/Python/Python Tricks')
