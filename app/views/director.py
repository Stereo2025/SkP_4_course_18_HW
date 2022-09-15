from flask import request
from flask_restx import Resource, Namespace
from app.dao.models.director import director_schema, directors_schema


director_ns = Namespace('director')
