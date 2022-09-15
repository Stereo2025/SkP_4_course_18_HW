from app.dao.models.movie import Movie
from app.dao.models.director import Director
from app.dao.models.genre import Genre


class MovieDAO:

    def __init__(self, session):
        self.session = session

    def get_movie_by_director_id(self, director_id):
        """Возвращает все фильмы выбранного по id 'director'"""

        return self.session.query(Movie).filter(Director.id == director_id).all()

    def get_movie_by_genre_id(self, genre_id):
        """Возвращает все фильмы выбранного по id 'genre'"""

        return self.session.query(Movie).filter(Genre.id == genre_id).all()

    def get_movie_by_year(self, year_id):
        """Возвращает все фильмы выбранные по year_id """

        return self.session.query(Movie).filter(Movie.year == year_id).all()

    def get_all(self):
        """Возвращает список всех фильмов"""

        return self.session.query(Movie).all()

    def create(self, data):
        """Добавляет фильм в БД"""

        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()
        return movie

    def get_one(self, mid: int):
        """Возвращает фильм по выбранному id"""

        return self.session.query(Movie).get(mid)

    def update(self, movie):
        """Обновляет данные о фильме"""

        self.session.add(movie)
        self.session.commit()
        return movie

    def delete(self, mid: int):
        """Удаляет выбранный по id фильм"""

        movie = self.get_one(mid)
        self.session.delete(movie)
        self.session.commit()
#######################################################################################################################
