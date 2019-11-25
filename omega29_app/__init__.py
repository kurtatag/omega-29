from flask import Flask, render_template, current_app, request

from omega29_app.models import TreeNode
from .extensions import db
from .views import (
    python_views, linux_views, git_views, docker_views, ansible_views
)

from .utils.text_utils import unescape_text
from .utils.web_utils import get_list, get_search

def create_app(config_file='settings.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)

    db.init_app(app)


    @app.route('/')
    def index():
        return get_list(node_name='Home')


    @app.route('/search')
    def search():
        return get_search()


    app.register_blueprint(python_views.bp)
    app.register_blueprint(linux_views.bp)
    app.register_blueprint(git_views.bp)
    app.register_blueprint(docker_views.bp)
    app.register_blueprint(ansible_views.bp)

    return app
