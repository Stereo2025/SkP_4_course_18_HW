from flask import request
from flask_restx import Resource, Namespace
from app.dao.models.director import director_schema, directors_schema


director_ns = Namespace('director')


@director_ns.route('/')
class DirectorsView(Resource):

    def get(self):
        pass


@director_ns.route('/<int:uid>')
class DirectorView(Resource):

    def get_one(self, pk):
        pass
#######################################################################################################################
