import os.path
from sqlalchemy import create_engine
from sqlalchemy import and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class TypeOcarina(Base):
    __tablename__ = 'typeOcarina'
    id_type_ocarina = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    hole_nb = Column(Integer, nullable=False)

    def __init__(self, name, hole_nb):
        self.id_type_ocarina = None
        self.name = name
        self.hole_nb = hole_nb

    def __str__(self):
        return ("n° {} : {} : {} trous".format(self.id_type_ocarina, self.name, self.hole_nb))


class BDEError(Exception):

    def __init__(self, mess):
        self.mess = mess

    def __str__(self):
        return self.mess


class TypeOcarinaORM:

    def __init__(self, dbName="database.sqlite3"):
        self.dbName = dbName
        self.session = None
        if not os.path.isfile(dbName):
            raise BDEError(
                "Connexion avec la base de données a échoué :\nErreur détectée : {} n'existe pas\n".format(dbName))
        try:
            engine = create_engine('sqlite:///'+dbName, echo=True)
            Session = sessionmaker(bind=engine)
            self.session = Session()
        except Exception as err:
            raise BDEError(
                'Connexion avec la base de données a échoué :\nErreur détectée :\n%s' % err)

    def reset(self):
        # TODO
        pass

    def __str__(self):
        s = ''
        for typeOcarina in self.session.query(TypeOcarina):
            s = s + str(typeOcarina) + "\n"
        return s

    def maj(self):
        # TODO
        pass

    def insert(self):
        # TODO
        pass

    def delete(self):
        # TODO
        pass
