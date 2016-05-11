import os
from controlers import *
import cherrypy
from mako.lookup import TemplateLookup
from mako.template import Template

path = os.path.abspath(os.path.dirname(__file__))
lookup = TemplateLookup(directories=[os.path.join(path, 'views')])


class WebAppli:

    def __init__(self):
        self.typeOcarina_orm = TypeOcarinaORM()
        self.typeMedia_orm = TypeMediaORM()
        self.performer_orm = PerformerORM()
        self.media_orm = MediaORM()
        self.occurrence_orm = OccurrenceORM()

    def index(self):
        print("machin")
        typeOcarinaArray = self.typeOcarina_orm.findAll()
        template = lookup.get_template('index.html')
        return template.render(typeOcarinaArray=typeOcarinaArray)

    def ocarina(self, choice=None):
        if(choice == None):
            return self.index()
        else :
            ocarina = self.typeOcarina_orm.findById(choice)
            if(ocarina == None):
                return self.index()
            template = lookup.get_template('ocarina.html')
            return template.render(ocarina=ocarina)

    index.exposed = True
    ocarina.exposed = True


class WebServer:

    def __init__(self):
        cherrypy.quickstart(WebAppli(
        ), "/", {"/static": {"tools.staticdir.on": True, "tools.staticdir.dir": os.path.join(path, 'static')}})
