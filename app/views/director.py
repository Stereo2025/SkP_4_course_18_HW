from flask import jsonify
from flask_restx import Resource, Namespace
from app.dao.models.director import director_schema, directors_schema
from app.container import director_service

director_ns = Namespace('director')


@director_ns.route('/')
class DirectorsView(Resource):

    def get(self):
        """Показывает всех 'director'"""

        all_directors = director_service.get_all()
        return directors_schema.dump(all_directors), 200


@director_ns.route('/<int:uid>/')
class DirectorView(Resource):

    def get(self, uid: int):
        """Показывает 'director' по его pk"""

        director = director_service.get_one(uid)
        if director:
            return director_schema.dump(director), 200
        return jsonify({'Attention!': f'Director №{uid} not found'})
#######################################################################################################################
