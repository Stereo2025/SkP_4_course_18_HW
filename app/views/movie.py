from flask import request, abort
from flask_restx import Resource, Namespace
from app.dao.models.movie import movie_schema, movies_schema
from app.container import movie_service


movie_ns = Namespace('movie')


@movie_ns.route("/")
class MoviesView(Resource):
    def get(self):

        query = request.args
        return movies_schema.dump(movie_service.get_all(query)), 200

    def post(self):

        upload_data = request.get_json()
        add_movie = movie_service.create(upload_data)
        return f"Фильм {add_movie.title} добавлен ", 201


@movie_ns.route("/<int:mid>")
class MoviesView(Resource):

    def get(self, mid):

        movie = movie_service.get_one(mid)
        if not movie:
            abort(404)
        return movie_schema.dump(movie_service.get_one(mid)), 200

    def put(self, mid):

        query = request.get_json()
        query['id'] = mid
        if movie_service.update(query):
            return f'Movie №{mid} is updated', 201
        return f'Movie №{mid} is not found', 404

    def patch(self, mid):

        query = request.get_json()
        query['id'] = mid
        if movie_service.update_partial(query):
            return f'Movie №{mid} is updated', 201
        return f'Movie №{mid} is not found', 404

    def delete(self, mid):

        movie = movie_service.delete(mid)
        if not movie:
            abort(404)
        return '', 204
#######################################################################################################################
