#!/usr/bin/python3
import cherrypy
config = {
    'global' : {
        #'server.socket_host' : '192.168.0.109',
        'server.socket_port' : 8080
    }
}


class Servidor(object):
    @cherrypy.expose
    def index(self):
        return 'Hello World!'

    @cherrypy.expose
    def greet(self, name):
        return 'Hello {}!'.format(name)

cherrypy.quickstart(Servidor(),'/',config)
