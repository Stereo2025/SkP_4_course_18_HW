from flask import request
from flask_restx import Resource, Namespace
from app.dao.models.movie import movie_schema, movies_schema


movie_ns = Namespace('movie')


@movie_ns.route('/')
class MoviesView(Resource):

    def get(self):
        pass

    def post(self):
        pass


@movie_ns.route('/<int:uid>')
class MovieView(Resource):

    def get_one(self, pk):
        pass

    def put(self, pk):
        pass

    def delete(self, pk):
        pass
#######################################################################################################################
