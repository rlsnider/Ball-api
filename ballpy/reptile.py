from flask import Blueprint

bp = Blueprint('pet', __name__, url_prefix='/reptiles')

@bp.route('/') 
def index():
    return "this is the reptile index"