from tornado.web import RequestHandler
from tornado.web import authenticated
from tornado.escape import url_unescape
import os,json
from html import unescape
from config import mysql_options

class Base(RequestHandler):
    def initialize(self,*args,**wkargs):
        self.settings['template_path'] = os.path.join('templates', 'home')

