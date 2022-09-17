from app.dao.movie import MovieDAO


class MovieService:

    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all(self, choice):

        if choice.get("director_id"):
            movies = self.dao.get_movie_by_director(int(choice.get("director_id")))

        elif choice.get("genre_id"):
            movies = self.dao.get_movie_by_genre(int(choice.get("genre_id")))

        elif choice.get("year"):
            movies = self.dao.get_movie_by_year(int(choice.get("year")))

        else:
            movies = self.dao.get_all()

        return movies

    def get_one(self, pk):

        return self.dao.get_one_movie(pk)

    def create(self, movie):

        return self.dao.create(movie)

    def update(self, pk):

        mid = pk.get('id')
        movie = self.get_one(mid)
        movie.title = pk.get('title')
        movie.description = pk.get('description')
        movie.trailer = pk.get('trailer')
        movie.year = pk.get('year')
        movie.rating = pk.get('rating')
        self.dao.update(movie)
        return movie

    def update_partial(self, data):
        mid = data.get('id')
        movie = self.dao.get_one_movie(mid)

        if "title" in data:
            movie.title = data.get('title')
        if "description" in data:
            movie.title = data.get('description')
        if "trailer" in data:
            movie.title = data.get('trailer')
        if "year" in data:
            movie.title = data.get('year')
        if "rating" in data:
            movie.title = data.get('rating')
        self.dao.update(movie)
        return movie

    def delete(self, mid):

        movie = self.dao.get_one_movie(mid)
        if movie:
            self.dao.delete(movie)
            return movie
        return None
#######################################################################################################################
