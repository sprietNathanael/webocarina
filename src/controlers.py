import os.path
from sqlalchemy import create_engine
from sqlalchemy import func
from sqlalchemy import desc
from sqlalchemy import asc
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

    def toCSV(self):
        s = ''
        for typeOcarina in self.session.query(TypeOcarina):
            s = s + typeOcarina.toCSV() + "\n"
        return s

    def findAll(self):
        return self.session.query(TypeOcarina)

    def maj(self):
        # TODO
        pass

    def insert(self, name, hole_nb):
        try:
            typeOcarina = TypeOcarina(name, hole_nb)
        except AttributeError:
            raise
        self.session.add(typeOcarina)
        self.session.commit()

    def delete(self):
        # TODO
        pass

    def getMaxPerformer(self, id):
        return(self.session.query(Performer).get(
            self.session.query(Occurrence.fk_id_performer).
            group_by(Occurrence.fk_id_performer).
            filter(Occurrence.fk_id_type_ocarina == id).
            order_by(desc(func.
                          count(Occurrence.fk_id_performer))).first()))

    def getMaxTypeMedia(self, id):
        return(self.session.query(TypeMedia).
               get(self.session.query(Media.fk_id_type_media).
                   join(Occurrence).
                   group_by(Media.fk_id_type_media).
                   filter(Occurrence.fk_id_type_ocarina == id).
                   order_by(desc(func.
                                 count(Media.fk_id_type_media))).first()))


class PerformerORM(BaseORM):

    def reset(self):
        # TODO
        pass

    def __str__(self):
        s = ''
        for performer in self.session.query(Performer):
            s = s + str(performer) + "\n"
        return s

    def toCSV(self):
        s = ''
        for performer in self.session.query(Performer):
            s = s + performer.toCSV() + "\n"
        return s

    def findAll(self):
        return self.session.query(Performer)

    def maj(self):
        # TODO
        pass

    def insert(self, name):
        performer = Performer(name)
        self.session.add(performer)
        self.session.commit()

    def delete(self):
        # TODO
        pass

    def getFavouriteTypeOcarina(self, id):
        return(self.session.query(TypeOcarina).get(
            self.session.query(Occurrence.fk_id_type_ocarina).
            group_by(Occurrence.fk_id_type_ocarina).
            filter(Occurrence.fk_id_performer == id).
            order_by(desc(func.
                          count(Occurrence.fk_id_type_ocarina))).first()))


class TypeMediaORM(BaseORM):

    def reset(self):
        # TODO
        pass

    def __str__(self):
        s = ''
        for typeMedia in self.session.query(TypeMedia):
            s = s + str(typeMedia) + "\n"
        return s

    def toCSV(self):
        s = ''
        for typeMedia in self.session.query(TypeMedia):
            s = s + typeMedia.toCSV() + "\n"
        return s

    def findAll(self):
        return self.session.query(TypeMedia)

    def insert(self, name):
        typeMedia = TypeMedia(name)
        self.session.add(typeMedia)
        self.session.commit()

    def maj(self):
        # TODO
        pass

    def delete(self):
        # TODO
        pass

    def getFavouriteTypeOcarina(self, id):
        return(self.session.query(TypeOcarina).
               get(self.session.query(Occurrence.fk_id_type_ocarina).
                   join(Media).
                   group_by(Occurrence.fk_id_type_ocarina).
                   filter(Media.fk_id_type_media == id).
                   order_by(desc(func.
                                 count(Occurrence.fk_id_type_ocarina))).first()))


class MediaORM(BaseORM):

    def reset(self):
        # TODO
        pass

    def __str__(self):
        s = ''
        for media in self.session.query(Media):
            s = s + str(media) + "\n"
        return s

    def toCSV(self):
        s = ''
        for media in self.session.query(Media):
            s = s + media.toCSV() + "\n"
        return s

    def findAll(self):
        return self.session.query(Media)

    def maj(self):
        # TODO
        pass

    def insert(self, name, length, fk_id_type_media):
        media = Media(name, length, fk_id_type_media)
        self.session.add(media)
        self.session.commit()

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

    def toCSV(self):
        s = ''
        for occurrence in self.session.query(Occurrence):
            s = s + occurrence.toCSV() + "\n"
        return s

    def findAll(self):
        return self.session.query(Occurrence)

    def maj(self):
        # TODO
        pass

    def insert(self, fk_id_media, fk_id_type_ocarina, length, comment, fk_id_performer):
        occurrence = Occurrence(
            fk_id_media, fk_id_type_ocarina, length, comment, fk_id_performer)
        self.session.add(occurrence)
        self.session.commit()

    def delete(self):
        # TODO
        pass
