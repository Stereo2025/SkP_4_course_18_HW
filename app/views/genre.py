from flask import request
from flask_restx import Resource, Namespace
from app.dao.models.genre import genre_schema, genres_schema


genre_ns = Namespace('genre')


@genre_ns.route('/')
class GenresView(Resource):

    def get(self):
        pass


@genre_ns.route('/<int:uid>')
class GenreView(Resource):

    def get_one(self, pk):
        pass
#######################################################################################################################
