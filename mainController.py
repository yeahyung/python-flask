from flask import Blueprint

blueprint = Blueprint('index', __name__)


@blueprint.route('/qwe')
def hello_world():
    return 'Hqwer'
