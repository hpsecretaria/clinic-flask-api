from app.routes import register_routes
from flask import Blueprint, Flask
from flask_restplus import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.engine import url

db = SQLAlchemy()


conn_url = url.URL(
    drivername='postgres',
    username='admin',
    password='1234',
    host='172.17.0.2',
    port=5432,
    database='clinic_flask_db',
    query=None
)


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = conn_url.__to_string__(
        hide_password=False)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    blueprint = Blueprint('clinic_appointment_api', __name__)
    api = Api(
        blueprint,
        version='1.0',
        prefix='/api/v1',
        title='Clinic Appointment',
        description='Clinic Appointment API'
    )
    register_routes(api, app)
    app.register_blueprint(blueprint)
    db.init_app(app)

    return app
