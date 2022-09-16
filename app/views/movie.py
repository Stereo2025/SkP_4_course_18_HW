from flask import jsonify
from flask import request
from flask_restx import Resource, Namespace
from app.dao.models.movie import movie_schema, movies_schema
from app.container import movie_service
from app.dao.models.movie import Movie

movie_ns = Namespace('movie')


@movie_ns.route('/')
class MoviesView(Resource):

    def get(self):
        director_id = request.args.get("director_id")
        genre_id = request.args.get("genre_id")
        year = request.args.get("year")

        movies = Movie.query

        if director_id:
            movies = Movie.query.filter(Movie.director_id == director_id)
        if genre_id:
            movies = Movie.query.filter(Movie.genre_id == genre_id)
        if year:
            movies = Movie.query.filter(Movie.year == year)

        all_movies = movie_service.get_all(movies)
        result = movies_schema.dump(all_movies)
        return result, 200

    def post(self):

        query = request.json
        movie = movie_service.create_movie(query)
        return jsonify({'Attention!': f'Movie {movie.id} is created'}), 201


@movie_ns.route('/<int:uid>')
class MovieView(Resource):

    def get(self, uid: int):

        movie = movie_service.get_one(uid)
        if movie:
            return movie_schema.dump(movie), 200
        return jsonify({'Attention!': f'Movie №{uid} not found'})

    def put(self, uid):

        movie_service.update_movie(uid)
        return jsonify({'Attention!': f'Movie №{uid} is update'})

    def delete(self, uid):
        movie_service.delete_movie(uid)
        return jsonify({'Attention!': f'Movie №{uid} deleted'})
#######################################################################################################################
