from flask import request
from flask_restx import Resource, Namespace
from app.dao.models.genre import genre_schema, genres_schema


genre_ns = Namespace('genre')
