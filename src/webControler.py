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
        typeOcarinaArray = typeOcarina_orm.findAll()
        performerArray = performer_orm.findAll()
        template = lookup.get_template('index.html')
        return template.render(typeOcarinaArray=typeOcarinaArray, performerArray=performerArray)

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

    index.exposed = True
    ocarina.exposed = True
    allOcarinas.exposed = True
    performer.exposed = True
    allPerformers.exposed = True


class WebServer:

    def __init__(self):
        cherrypy.quickstart(WebAppli(
        ), "/", {"/static": {"tools.staticdir.on": True, "tools.staticdir.dir": os.path.join(path, 'static')}})
