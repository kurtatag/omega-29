from flask import Blueprint
from omega29_app.utils.web_utils import get_list, get_page

bp = Blueprint('git', __name__, url_prefix='/git')


@bp.route('/')
def home():
    return get_list(node_name='Home/Git')


@bp.route('/essentials')
def essentials():
    return get_page(node_name='Home/Git/Git Essentials')
