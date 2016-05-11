import os
from controlers import *
import cherrypy
from mako.lookup import TemplateLookup
from mako.template import Template

path = os.path.abspath(os.path.dirname(__file__))
lookup = TemplateLookup(directories=[os.path.join(path, 'views')], input_encoding='utf-8')


class WebAppli:

    def index(self):
        typeOcarina_orm = TypeOcarinaORM()
        typeOcarinaArray = typeOcarina_orm.findAll()
        template = lookup.get_template('index.html')
        return template.render(typeOcarinaArray=typeOcarinaArray)

    def ocarina(self, choice=None):
        if(choice == None):
            return self.index()
        else :
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

    index.exposed = True
    ocarina.exposed = True


class WebServer:

    def __init__(self):
        cherrypy.quickstart(WebAppli(
        ), "/", {"/static": {"tools.staticdir.on": True, "tools.staticdir.dir": os.path.join(path, 'static')}})
