from app.dao.movie import MovieDAO
from app.services.movie import MovieService
from app.dao.genre import GenreDAO
from app.services.genre import GenreService
from app.dao.director import DirectorDAO
from app.services.director import DirectorService
from database import db


movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)
#######################################################################################################################
