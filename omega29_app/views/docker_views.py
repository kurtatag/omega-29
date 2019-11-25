from flask import Blueprint
from omega29_app.utils.web_utils import get_list

bp = Blueprint('docker', __name__, url_prefix='/docker')


@bp.route('/')
def home():
    return get_list(node_name='Home/Docker')
