#coding:utf-8
import tornado.web
from mysql import *
from base import *

class NotfoundHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("404.htm")

class WelcomeHandler(BaseHandler):
    def get(self):
        self.render(
            "index.html",
            title="心愿说 - 首页",
            user=self.get_current_user()
            )
