from app.dao.models.director import Director


class DirectorDAO:

    def __init__(self, session):
        self.session = session

    def get_all(self):
        """Возвращает всех 'directors'"""

        return self.session.query(Director).all()

    def get_one(self, did: int):
        """Возвращает 'director' по id"""

        return self.session.query(Director).get(did)
#######################################################################################################################
