from Repositories.ABCrepository import ABCRepository


class SQLAlchemyRepository(ABCRepository):
    def __init__(self, session):
        self.session = session

    def save(self, data):
        self.session.add(data)
        self.session.commit()

    def find(self, model, **kwargs):
        return self.session.query(model).filter_by(**kwargs).all()

    def delete(self, data):
        self.session.delete(data)
        self.session.commit()
