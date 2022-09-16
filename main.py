from flask import Flask
from flask_restx import Api
from app.config import Config
from app.database import db
from app.views.movie import movie_ns
from app.views.genre import genre_ns
from app.views.director import director_ns


def create_app(config: Config) -> Flask:

    application = Flask(__name__)
    application.config.from_object(config)
    register_extensions(application)
    return application


def register_extensions(application: Flask):

    db.init_app(application)
    api = Api(application)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)


def create_data():

    with app.app_context():
        db.create_all()


if __name__ == '__main__':
    app = create_app(Config())
    create_data()
    app.run(debug=True)
