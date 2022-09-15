from flask import request
from flask_restx import Resource, Namespace
from app.dao.models.movie import movie_schema, movies_schema


movie_ns = Namespace('movie')
