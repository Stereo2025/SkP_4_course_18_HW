from app.dao.movie import MovieDAO


class MovieService:

    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, mid: int):

        return self.dao.get_one(mid)

    def get_all(self, choice):

        if choice.get('director_id') is not None:
            movies = self.dao.get_movie_by_director_id(choice.get('director_id'))

        elif choice.get('genre_id') is not None:
            movies = self.dao.get_movie_by_genre_id(choice.get('genre_id'))

        elif choice.get('year') is not None:
            movies = self.dao.get_movie_by_year(choice.get('year'))

        else:
            movies = self.dao.get_all()

        return movies

    def create_movie(self, data):

        return self.dao.create(data)

    def update_movie(self, data):

        mid = data.get('id')
        movie = self.get_one(mid)
        movie.title = data.get('title')
        movie.description = data.get('description')
        movie.trailer = data.get('trailer')
        movie.year = data.get('year')
        movie.rating = data.get('rating')
        movie.genre_id = data.get('genre_id')
        movie.director_id = data.get('director_id')
        self.dao.update(movie)

    def update_partial(self, data):

        mid = data.get('id')
        movie = self.get_one(mid)

        if 'title' in data:
            movie.title = data.get('title')
        if 'description' in data:
            movie.description = data.get('description')
        if 'trailer' in data:
            movie.trailer = data.get('trailer')
        if 'year' in data:
            movie.year = data.get('year')
        if 'rating' in data:
            movie.rating = data.get('rating')
        if 'genre_id' in data:
            movie.genre_id = data.get('genre_id')
        if 'director_id' in data:
            movie.director_id = data.get('director_id')

        self.dao.update(movie)

    def delete_movie(self, mid: int):

        self.dao.delete(mid)
#######################################################################################################################
