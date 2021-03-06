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

    def findById(self, id):
        return self.session.query(TypeOcarina).get(id)

    def toCSV(self):
        s = ''
        for typeOcarina in self.session.query(TypeOcarina):
            s = s + typeOcarina.toCSV() + "\n"
        return s

    def findAll(self):
        return self.session.query(TypeOcarina)

    def maj(self, id, name, hole_nb):
        typeOcarina = self.findById(id)
        typeOcarina.name = name
        typeOcarina.hole_nb = hole_nb
        self.session.commit()

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
        print(self.session.query(Performer).get(
            self.session.query(Occurrence.fk_id_performer).
            group_by(Occurrence.fk_id_performer).
            filter(Occurrence.fk_id_type_ocarina == id).
            order_by(desc(func.
                          count(Occurrence.fk_id_performer))).first()))
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

    def findByMedia(self, media):
        typeOcarina_id_Array = self.session.query(
            Occurrence.fk_id_type_ocarina).filter(Occurrence.fk_id_media == media).all()
        typeOcarinaArray = []
        for i in typeOcarina_id_Array:
            typeOcarinaArray.append(self.session.query(TypeOcarina).get(i))
        return typeOcarinaArray

    def getAverageLength(self, typeOcarina=-1):
        if(typeOcarina == -1):
            average = self.session.query(func.avg(Occurrence.length)).one()[0]
        else:
            average = self.session.query(func.avg(Occurrence.length)).filter(
                Occurrence.fk_id_type_ocarina == typeOcarina).one()[0]
        if(type(average) is int or type(average) is float):
            return(average)
        else:
            return(0)

    def getMinLength(self, typeOcarina=-1):
        if(typeOcarina == -1):
            minimum = self.session.query(func.min(Occurrence.length)).one()[0]
        else:
            minimum = self.session.query(func.min(Occurrence.length)).filter(
                Occurrence.fk_id_type_ocarina == typeOcarina).one()[0]
        if(type(minimum) is int or type(minimum) is float):
            return(minimum)
        else:
            return(0)

    def getMaxLength(self, typeOcarina=-1):
        if(typeOcarina == -1):
            maximum = self.session.query(func.max(Occurrence.length)).one()[0]
        else:
            maximum = self.session.query(func.max(Occurrence.length)).filter(
                Occurrence.fk_id_type_ocarina == typeOcarina).one()[0]
        if(type(maximum) is int or type(maximum) is float):
            return(maximum)
        else:
            return(0)

    def getTotalLength(self, typeOcarina=-1):
        if(typeOcarina == -1):
            total = self.session.query(func.sum(Occurrence.length)).one()[0]
        else:
            total = self.session.query(func.sum(Occurrence.length)).filter(
                Occurrence.fk_id_type_ocarina == typeOcarina).one()[0]
        if(type(total) is int or type(total) is float):
            return(total)
        else:
            return(0)


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

    def findById(self, id):
        return self.session.query(Performer).get(id)

    def findAll(self):
        return self.session.query(Performer)

    def maj(self, id_performer, name):
        performer = self.findById(id_performer)
        performer.name = name
        self.session.commit()

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

    def getAverageLength(self, performer):
        average = self.session.query(func.avg(Occurrence.length)).filter(
            Occurrence.fk_id_performer == performer).one()[0]
        if(type(average) is int or type(average) is float):
            return(average)
        else:
            return(0)

    def getMinLength(self, performer):
        minimum = self.session.query(func.min(Occurrence.length)).filter(
            Occurrence.fk_id_performer == performer).one()[0]
        if(type(minimum) is int or type(minimum) is float):
            return(minimum)
        else:
            return(0)

    def getMaxLength(self, performer):
        maximum = self.session.query(func.max(Occurrence.length)).filter(
            Occurrence.fk_id_performer == performer).one()[0]
        if(type(maximum) is int or type(maximum) is float):
            return(maximum)
        else:
            return(0)

    def getTotalLength(self, performer):
        total = self.session.query(func.sum(Occurrence.length)).filter(
            Occurrence.fk_id_performer == performer).one()[0]
        if(type(total) is int or type(total) is float):
            return(total)
        else:
            return(0)


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

    def findById(self, id):
        return self.session.query(TypeMedia).get(id)

    def getFavouriteTypeOcarina(self, id):
        return(self.session.query(TypeOcarina).
               get(self.session.query(Occurrence.fk_id_type_ocarina).
                   join(Media).
                   group_by(Occurrence.fk_id_type_ocarina).
                   filter(Media.fk_id_type_media == id).
                   order_by(desc(func.
                                 count(Occurrence.fk_id_type_ocarina))).first()))

    def getAverageLength(self, typeMedia):
        average = self.session.query(func.avg(Occurrence.length)).\
            join(Media).\
            filter(Media.fk_id_type_media == typeMedia).one()[0]
        if(type(average) is int or type(average) is float):
            return(average)
        else:
            return(0)

    def getMinLength(self, typeMedia):
        minimum = self.session.query(func.min(Occurrence.length)).\
            join(Media).\
            filter(Media.fk_id_type_media == typeMedia).one()[0]
        if(type(minimum) is int or type(minimum) is float):
            return(minimum)
        else:
            return(0)

    def getMaxLength(self, typeMedia):
        maximum = self.session.query(func.max(Occurrence.length)).\
            join(Media).\
            filter(Media.fk_id_type_media == typeMedia).one()[0]
        if(type(maximum) is int or type(maximum) is float):
            return(maximum)
        else:
            return(0)

    def getTotalLength(self, typeMedia):
        total = self.session.query(func.sum(Occurrence.length)).\
            join(Media).\
            filter(Media.fk_id_type_media == typeMedia).one()[0]
        if(type(total) is int or type(total) is float):
            return(total)
        else:
            return(0)


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

    def findById(self, id):
        return self.session.query(Media).get(id)

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

    def typeOcarinaProportion(self, media, id_ocarina):
        ocarinaLength = self.session.query(Occurrence.length).\
            filter(and_(Occurrence.fk_id_media == media,
                        Occurrence.fk_id_type_ocarina == id_ocarina)).one()[0]
        totalLength = self.session.query(Media).get(media).length
        return((ocarinaLength/totalLength)*100)

    def findByTypeMedia(self, typeMedia):
        media_id_Array = self.session.query(
            Media.id_media).filter(Media.fk_id_type_media == typeMedia).all()
        mediaArray = []
        for i in media_id_Array:
            mediaArray.append(self.session.query(Media).get(i))
        return mediaArray


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

    def findByMediaOcarina(self, media, ocarina):
        return(self.session.query(Occurrence).get((media, ocarina)))

    def insert(self, fk_id_media, fk_id_type_ocarina, length, comment, fk_id_performer):
        occurrence = Occurrence(
            fk_id_media, fk_id_type_ocarina, length, comment, fk_id_performer)
        self.session.add(occurrence)
        self.session.commit()

    def delete(self):
        # TODO
        pass
