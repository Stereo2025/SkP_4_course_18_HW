from app.dao.models.movie import Movie


class MovieDAO:

    def __init__(self, session):
        self.session = session

    def get_all(self):
        """Возвращает список всех фильмов"""

        return self.session.query(Movie).all()

    def get_one_movie(self, mid: int):
        """ Возвращает подробную информацию о фильме. """

        return self.session.query(Movie).get(mid)

    def get_movie_by_director(self, director_id):
        """ Возвращает все фильмы режиссера """

        return self.session.query(Movie).filter(Movie.director_id == director_id).all()

    def get_movie_by_genre(self, genre_id):
        """ Возвращает все фильмы жанра """

        return self.session.query(Movie).filter(Movie.genre_id == genre_id).all()

    def get_movie_by_year(self, year):
        """ Возвращает все фильмы за год """

        return self.session.query(Movie).filter_by(Movie.year == year).all()

    def create(self, movie):
        """ Добавляет фильм методом POST """

        new_movies = Movie(**movie)
        self.session.add(new_movies)
        self.session.commit()
        return new_movies

    def update(self, movie):
        """ Обновляет данные о фильме методом PUT """

        self.session.add(movie)
        self.session.commit()
        return movie

    def delete(self, movie):
        """ Удаляет данные о фильме """

        self.session.delete(movie)
        self.session.commit()
#######################################################################################################################
