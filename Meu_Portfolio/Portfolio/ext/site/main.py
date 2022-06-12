from flask import Blueprint, render_template
bp = Blueprint('main', __name__)


def init_app(app):
    app.register_blueprint(bp)
    

