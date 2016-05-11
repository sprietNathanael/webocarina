"""
Tutorial - Hello World

The most basic (working) CherryPy application possible.
"""

# Import CherryPy global namespace
import os
import cherrypy
from mako.lookup import TemplateLookup
from mako.template import Template

path = os.path.abspath(os.path.dirname(__file__))
lookup = TemplateLookup(directories=[os.path.join(path, 'views')])


class HelloWorld:

    """ Sample request handler class. """

    def index(self):
        # CherryPy will call this method for the root URI ("/") and send
        # its return value to the client. Because this is tutorial
        # lesson number 01, we'll just send something really simple.
        # How about...
        template = lookup.get_template('index.html')
        return template.render(foo='bar')

    # Expose the index method through the web. CherryPy will never
    # publish methods that don't have the exposed attribute set to True.
    index.exposed = True

if __name__ == '__main__':
    cherrypy.quickstart(HelloWorld())
