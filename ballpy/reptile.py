from flask import ( Blueprint, request, redirect ) 
import json


#reptiles = json.load(open('reptiles.json'))


bp = Blueprint('pet', __name__, url_prefix='/reptiles')

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method =='POST':
        print(request.form)
        return redirect('/reptiles')
    return 'This is the reptile index'

@bp.route('/new')
def new():
    return 'This is your form page to add a new reptile'

@bp.route('/<int:id>')
def show(id):
    return 'This is for viewing a single reptile'
    #I've tried everything I can think of. I just do not know how to get this code to work.
    
    # reptile = models.Reptile.query.filter_by(id=id).first()
    # reptile_dict = {
    #     'id' : reptile.id,
    #     'common_name' : reptile.common_name, 
    #     'scientific_name' : reptile.scientific_name,
    #     'native_habitat' : reptile.native_habitat,
    #     'fun_fact' : reptile.fun_fact
    #     }
    # return reptile_dict

