from app.dao.models.genre import Genre


class GenreDAO:

    def __init__(self, session):
        self.session = session

    def get_all(self):
        """Возвращает все 'genres'"""

        return self.session.query(Genre).all()

    def get_one(self, gid: int):
        """Возвращает 'genres' по id"""

        return self.session.query(Genre).get(gid)
#######################################################################################################################
