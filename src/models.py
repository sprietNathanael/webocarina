
from sqlalchemy import Integer, ForeignKey, String, Column, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class TypeOcarina(Base):
    __tablename__ = 'typeOcarina'
    id_type_ocarina = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    hole_nb = Column(Integer, nullable=False)
    occurrences = relationship("Occurrence")

    def __init__(self, name, hole_nb):
        self.id_type_ocarina = None
        self.name = name
        self.hole_nb = hole_nb

    def __str__(self):
        return ("n° {} ; nom : {} ; nombres Trous : {}".format(self.id_type_ocarina, self.name, self.hole_nb))


class TypeMedia(Base):
    __tablename__ = 'typeMedia'
    id_type_media = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    medias = relationship("Media")

    def __init__(self, name):
        self.id_type_media = None
        self.name = name

    def __str__(self):
        return ("n° {} ; name : {}".format(self.id_type_media, self.name))


class Performer(Base):
    __tablename__ = 'performer'
    id_performer = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    occurrences = relationship("Occurrence")

    def __init__(self, name):
        self.id_performer = None
        self.name = name

    def __str__(self):
        return ("n° {} ; nom : {}".format(self.id_performer, self.name))


class Media(Base):
    __tablename__ = 'media'
    id_media = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    length = Column(Integer, nullable=False)
    fk_id_type_media = Column(Integer, ForeignKey("typeMedia.id_type_media"), nullable=False, )
    typeMedia = relationship("TypeMedia")
    occurrences = relationship("Occurrence")

    def __init__(self, name, length, fk_id_type_media):
        self.id_media = None
        self.name = name
        self.length = length
        fk_id_type_media = fk_id_type_media

    def __str__(self):
        return ("n° {} ; nom : {} ; durée : {} ; type :  ( {} )".format(self.id_media, self.name, self.length, self.typeMedia))


class Occurrence(Base):
    __tablename__ = 'occurrence'
    fk_id_media = Column(Integer, ForeignKey("media.id_media"), primary_key=True)
    fk_id_type_ocarina = Column(Integer, ForeignKey("typeOcarina.id_type_ocarina"), primary_key=True)
    length = Column(Integer, nullable=False)
    comment = Column(String, nullable=True)
    fk_id_performer = Column(Integer, ForeignKey("performer.id_performer"), nullable=False)
    media = relationship("Media")
    typeOcarina = relationship("TypeOcarina")
    performer = relationship("Performer")

    def __init__(self, fk_id_media, fk_id_type_ocarina, length, comment, fk_id_performer):
        self.fk_id_media = fk_id_media
        self.fk_id_type_ocarina = fk_id_type_ocarina
        self.length = length
        self.comment = comment
        self.fk_id_performer = fk_id_performer

    def __str__(self):
        return ("media : ( {} ) ; ocarina : ( {} ) ; durée : {} ; commentaire : {}  ; interprète : ( {} )".format(self.media, self.typeOcarina, self.length, self.comment, self.performer))
