from flask import jsonify
from flask_restx import Resource, Namespace
from app.dao.models.genre import genre_schema, genres_schema
from app.container import genre_service

genre_ns = Namespace('genre')


@genre_ns.route('/')
class GenresView(Resource):

    def get(self):
        """"""

        all_genres = genre_service.get_all()
        return genres_schema.dump(all_genres), 200


@genre_ns.route('/<int:uid>/')
class GenreView(Resource):

    def get(self, uid: int):
        """"""

        genre = genre_service.get_one(uid)
        if genre:
            return genre_schema.dump(genre), 200
        return jsonify({'Attention!': f'Genre №{uid} not found'})
#######################################################################################################################
