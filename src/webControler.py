import os
from controlers import *
import cherrypy
from mako.lookup import TemplateLookup
from mako.template import Template

path = os.path.abspath(os.path.dirname(__file__))
lookup = TemplateLookup(
    directories=[os.path.join(path, 'views')], input_encoding='utf-8')


class WebAppli:

    def index(self):
        typeOcarina_orm = TypeOcarinaORM()
        performer_orm = PerformerORM()
        media_orm = MediaORM()
        typeMedia_orm = TypeMediaORM()
        occurrence_orm = OccurrenceORM()
        typeOcarinaArray = typeOcarina_orm.findAll()
        performerArray = performer_orm.findAll()
        mediaArray = media_orm.findAll()
        typeMediaArray = typeMedia_orm.findAll()
        occurrenceArray = occurrence_orm.findAll()
        template = lookup.get_template('index.html')
        return template.render(typeOcarinaArray=typeOcarinaArray, performerArray=performerArray,  mediaArray=mediaArray, typeMediaArray=typeMediaArray, occurrenceArray=occurrenceArray)

    def ocarina(self, choice=None):
        if(choice == None):
            return self.index()
        else:
            typeOcarina_orm = TypeOcarinaORM()
            ocarina = typeOcarina_orm.findById(choice)
            if(ocarina == None):
                return self.index()
            try:
                performer = typeOcarina_orm.getMaxPerformer(choice)
                typeMedia = typeOcarina_orm.getMaxTypeMedia(choice)
            except TypeError:
                performer = None
                typeMedia = None
            avg = typeOcarina_orm.getAverageLength(choice)
            min = typeOcarina_orm.getMinLength(choice)
            max = typeOcarina_orm.getMaxLength(choice)
            total = typeOcarina_orm.getTotalLength(choice)
            template = lookup.get_template('ocarina.html')
            return template.render(ocarina=ocarina, performer=performer, typeMedia=typeMedia, avg=avg, min=min, max=max, total=total)

    def allOcarinas(self):
        typeOcarina_orm = TypeOcarinaORM()
        ocarinaArray = typeOcarina_orm.findAll()
        ocarinaInfos = {}
        for ocarina in ocarinaArray:
            ocarinaInfos[ocarina.id_type_ocarina] = {}
            try:
                ocarinaInfos[ocarina.id_type_ocarina][
                    "performer"] = typeOcarina_orm.getMaxPerformer(ocarina.id_type_ocarina)
                ocarinaInfos[ocarina.id_type_ocarina][
                    "typeMedia"] = typeOcarina_orm.getMaxTypeMedia(ocarina.id_type_ocarina)
            except TypeError:
                ocarinaInfos[ocarina.id_type_ocarina]["performer"] = None
                ocarinaInfos[ocarina.id_type_ocarina]["typeMedia"] = None
            ocarinaInfos[ocarina.id_type_ocarina][
                "avg"] = typeOcarina_orm.getAverageLength(ocarina.id_type_ocarina)
            ocarinaInfos[ocarina.id_type_ocarina][
                "min"] = typeOcarina_orm.getMinLength(ocarina.id_type_ocarina)
            ocarinaInfos[ocarina.id_type_ocarina][
                "max"] = typeOcarina_orm.getMaxLength(ocarina.id_type_ocarina)
            ocarinaInfos[ocarina.id_type_ocarina][
                "total"] = typeOcarina_orm.getTotalLength(ocarina.id_type_ocarina)
        template = lookup.get_template('allOcarinas.html')
        return template.render(ocarinaArray=ocarinaArray, ocarinaInfos=ocarinaInfos)

    def performer(self, choice=None):
        if(choice == None):
            return self.index()
        else:
            performer_orm = PerformerORM()
            performer = performer_orm.findById(choice)
            if(performer == None):
                return self.index()
            try:
                ocarina = performer_orm.getFavouriteTypeOcarina(choice)
            except TypeError:
                ocarina = None
            avg = performer_orm.getAverageLength(choice)
            min = performer_orm.getMinLength(choice)
            max = performer_orm.getMaxLength(choice)
            total = performer_orm.getTotalLength(choice)
            template = lookup.get_template('performer.html')
            return template.render(performer=performer, ocarina=ocarina, avg=avg, min=min, max=max, total=total)

    def allPerformers(self):
        performer_orm = PerformerORM()
        performerArray = performer_orm.findAll()
        performerInfos = {}
        for performer in performerArray:
            performerInfos[performer.id_performer] = {}
            try:
                performerInfos[performer.id_performer][
                    "ocarina"] = performer_orm.getFavouriteTypeOcarina(performer.id_performer)
            except TypeError:
                performerInfos[performer.id_performer]["ocarina"] = None
            performerInfos[performer.id_performer][
                "avg"] = performer_orm.getAverageLength(performer.id_performer)
            performerInfos[performer.id_performer][
                "min"] = performer_orm.getMinLength(performer.id_performer)
            performerInfos[performer.id_performer][
                "max"] = performer_orm.getMaxLength(performer.id_performer)
            performerInfos[performer.id_performer][
                "total"] = performer_orm.getTotalLength(performer.id_performer)
        template = lookup.get_template('allPerformers.html')
        return template.render(performerArray=performerArray, performerInfos=performerInfos)

    def media(self, choice=None):
        if(choice == None):
            return self.index()
        else:
            media_orm = MediaORM()
            media = media_orm.findById(choice)
            if(media == None):
                return self.index()
            typeMedia = TypeMediaORM().findById(media.fk_id_type_media)
            template = lookup.get_template('media.html')
            return template.render(media=media, typeMedia=typeMedia)

    def allMedias(self):
        media_orm = MediaORM()
        typeMedia_orm = TypeMediaORM()
        mediaArray = media_orm.findAll()
        mediaInfos = {}
        for media in mediaArray:
            mediaInfos[media.id_media] = typeMedia_orm.findById(
                media.fk_id_type_media)
        template = lookup.get_template('allMedias.html')
        return template.render(mediaArray=mediaArray, mediaInfos=mediaInfos)

    def typeMedia(self, choice=None):
        if(choice == None):
            return self.index()
        else:
            typeMedia_orm = TypeMediaORM()
            typeMedia = typeMedia_orm.findById(choice)
            if(typeMedia == None):
                return self.index()
            media_orm = MediaORM()
            mediaArray = media_orm.findByTypeMedia(choice)
            avg = typeMedia_orm.getAverageLength(choice)
            min = typeMedia_orm.getMinLength(choice)
            max = typeMedia_orm.getMaxLength(choice)
            total = typeMedia_orm.getTotalLength(choice)
            template = lookup.get_template('typeMedia.html')
            return template.render(typeMedia=typeMedia, avg=avg, min=min, max=max, total=total, mediaArray=mediaArray)

    def allTypeMedias(self):
        typeMedia_orm = TypeMediaORM()
        typeMediaArray = typeMedia_orm.findAll()
        typeMediaInfos = {}
        for typeMedia in typeMediaArray:
            typeMediaInfos[typeMedia.id_type_media] = {}
            typeMediaInfos[typeMedia.id_type_media][
                "avg"] = typeMedia_orm.getAverageLength(typeMedia.id_type_media)
            typeMediaInfos[typeMedia.id_type_media][
                "min"] = typeMedia_orm.getMinLength(typeMedia.id_type_media)
            typeMediaInfos[typeMedia.id_type_media][
                "max"] = typeMedia_orm.getMaxLength(typeMedia.id_type_media)
            typeMediaInfos[typeMedia.id_type_media][
                "total"] = typeMedia_orm.getTotalLength(typeMedia.id_type_media)
        template = lookup.get_template('allTypeMedias.html')
        return template.render(typeMediaArray=typeMediaArray, typeMediaInfos=typeMediaInfos)

    def allOccurrences(self):
        occurrence_orm = OccurrenceORM()
        media_orm = MediaORM()
        typeOcarina_orm = TypeOcarinaORM()
        performer_orm = PerformerORM()
        occurrenceArray = occurrence_orm.findAll()
        occurrenceInfos = {}
        i = 0
        for occurrence in occurrenceArray:
            occurrenceInfos[i] = {}

            occurrenceInfos[i][
                "media"] = media_orm.findById(occurrence.fk_id_media)
            occurrenceInfos[i][
                "typeOcarina"] = typeOcarina_orm.findById(occurrence.fk_id_type_ocarina)
            occurrenceInfos[i][
                "performer"] = performer_orm.findById(occurrence.fk_id_performer)
            i += 1
        template = lookup.get_template('allOccurrences.html')
        return template.render(occurrenceArray=occurrenceArray, occurrenceInfos=occurrenceInfos)

    def occurrence(self, mediaChoice=None, ocarinaChoice=None):
        if(mediaChoice == None or ocarinaChoice == None):
            return self.index()
        else:
            occurrence_orm = OccurrenceORM()
            media_orm = MediaORM()
            performer_orm = PerformerORM()
            typeOcarina_orm = TypeOcarinaORM()
            occurrence = occurrence_orm.findByMediaOcarina(
                mediaChoice, ocarinaChoice)
            if(occurrence == None):
                return self.index()
            media = media_orm.findById(occurrence.fk_id_media)
            typeOcarina = typeOcarina_orm.findById(
                occurrence.fk_id_type_ocarina)
            performer = performer_orm.findById(occurrence.fk_id_performer)
            template = lookup.get_template('occurrence.html')
            return template.render(occurrence=occurrence, performer=performer, typeOcarina=typeOcarina, media=media)

    def addOcarina(self):
        template = lookup.get_template('addOcarina.html')
        return template.render()

    def addOcarinaSend(self, name, holes):
        typeOcarina_orm = TypeOcarinaORM()
        try:
            typeOcarina_orm.insert(name, holes)
        except AttributeError:
            return(self.addOcarina())
        else:
            return(self.index())

    def addMedia(self):
        typeMedia_orm = TypeMediaORM()
        typeMediaArray = typeMedia_orm.findAll()
        template = lookup.get_template('addMedia.html')
        return template.render(typeMediaArray=typeMediaArray)

    def addMediaSend(self, name, length, typeMedia):
        media_orm = MediaORM()
        try:
            media_orm.insert(name, length, typeMedia)
        except AttributeError:
            return(self.addMedia())
        else:
            return(self.index())

    def addTypeMedia(self):
        template = lookup.get_template('addTypeMedia.html')
        return template.render()

    def addTypeMediaSend(self, name):
        typeMedia_orm = TypeMediaORM()
        try:
            typeMedia_orm.insert(name)
        except AttributeError:
            return(self.addTypeMedia())
        else:
            return(self.index())

    def addPerformer(self):
        template = lookup.get_template('addPerformer.html')
        return template.render()

    def addPerformerSend(self, name):
        performer_orm = PerformerORM()
        try:
            performer_orm.insert(name)
        except AttributeError:
            return(self.addPerformer())
        else:
            return(self.index())

    def addOccurrence(self):
        media_orm = MediaORM()
        performer_orm = PerformerORM()
        typeOcarina_orm = TypeOcarinaORM()
        mediaArray = media_orm.findAll()
        performerArray = performer_orm.findAll()
        typeOcarinaArray = typeOcarina_orm.findAll()
        template = lookup.get_template('addOccurrence.html')
        return template.render(mediaArray=mediaArray, performerArray=performerArray, typeOcarinaArray=typeOcarinaArray)

    def addOccurrenceSend(self, media, ocarina, length, comment, performer):
        occurrence_orm = OccurrenceORM()
        try:
            occurrence_orm.insert(media, ocarina, length, comment, performer)
        except AttributeError:
            return(self.addOccurrence())
        except:
            return(self.addOccurrence())

        else:
            return(self.index())

    index.exposed = True
    ocarina.exposed = True
    allOcarinas.exposed = True
    performer.exposed = True
    allPerformers.exposed = True
    media.exposed = True
    allMedias.exposed = True
    typeMedia.exposed = True
    allTypeMedias.exposed = True
    allOccurrences.exposed = True
    occurrence.exposed = True
    addOcarina.exposed = True
    addOcarinaSend.exposed = True
    addMedia.exposed = True
    addMediaSend.exposed = True
    addTypeMedia.exposed = True
    addTypeMediaSend.exposed = True
    addPerformer.exposed = True
    addPerformerSend.exposed = True
    addOccurrence.exposed = True
    addOccurrenceSend.exposed = True


class WebServer:

    def __init__(self):
        cherrypy.quickstart(WebAppli(
        ), "/", {"/static": {"tools.staticdir.on": True, "tools.staticdir.dir": os.path.join(path, 'static')}})
