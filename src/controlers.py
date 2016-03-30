import os.path
from sqlalchemy import create_engine
from sqlalchemy import and_
from sqlalchemy.orm import sessionmaker
from models import *


class BDEError(Exception):

    def __init__(self, mess):
        self.mess = mess

    def __str__(self):
        return self.mess


class BaseORM:

    def __init__(self, dbName="database.sqlite3"):
        self.dbName = dbName
        self.session = None
        if not os.path.isfile(dbName):
            raise BDEError(
                "Connexion avec la base de données a échoué :\nErreur détectée : {} n'existe pas\n".format(dbName))
        try:
            engine = create_engine('sqlite:///' + dbName, echo=False)
            Session = sessionmaker(bind=engine)
            self.session = Session()
        except Exception as err:
            raise BDEError(
                'Connexion avec la base de données a échoué :\nErreur détectée :\n%s' % err)


class TypeOcarinaORM(BaseORM):

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


class PerformerORM(BaseORM):

    def reset(self):
        # TODO
        pass

    def __str__(self):
        s = ''
        for performer in self.session.query(Performer):
            s = s + str(performer) + "\n"
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


class TypeMediaORM(BaseORM):

    def reset(self):
        # TODO
        pass

    def __str__(self):
        s = ''
        for typeMedia in self.session.query(TypeMedia):
            s = s + str(typeMedia) + "\n"
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


class MediaORM(BaseORM):

    def reset(self):
        # TODO
        pass

    def __str__(self):
        s = ''
        for media in self.session.query(Media):
            s = s + str(media) + "\n"
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


class OccurrenceORM(BaseORM):

    def reset(self):
        # TODO
        pass

    def __str__(self):
        s = ''
        for occurrence in self.session.query(Occurrence):
            s = s + str(occurrence) + "\n"
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