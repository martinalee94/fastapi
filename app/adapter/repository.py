import abc

from sqlalchemy.orm import Session


# Port -> Interface
class AbstractRepository(abc.ABC):
    def add(self):
        "Abstract Method for add entity to persistent layer"

    def add_all(self):
        "Abstract Method for add list of entity to persistent layer"

    @abc.abstractmethod
    def get(self, is_update=False):
        raise NotImplementedError

    @abc.abstractmethod
    def list(self, is_update=False):
        raise NotImplementedError


# Adapter
class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session: Session, model):
        self.session: Session = session
        self.model = model

    def add(self):
        self.session.add(self.model)

    def get(self):
        return self.session.query(self.model).first()

    def list(self):
        return self.session.query(self.model).all()


# Test
class FakeSqlAlchemyRepository(AbstractRepository):
    def __init__(self, session: Session, model):
        self.session: Session = session
        self.model = model

    def add(self):
        self.session.add(self.model)

    def get(self):
        return self.session.query(self.model).first()

    def list(self):
        return self.session.query(self.model).all()


class FakeSession:
    committed = False

    def commit(self):
        self.committed = True
