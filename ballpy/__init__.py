from flask import Flask
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:34Shutthed**r@localhost:5432/ballpy'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    @app.route('/')
    def hello():
        return "Hello ball"
    from . import models
    models.db.init_app(app)
    migrate = Migrate(app, models.db)
    
    #register reptile blueprint
    from . import reptile
    app.register_blueprint(reptile.bp)
    
    return app