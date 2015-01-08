#coding:utf-8
import tornado.web
import json
import os.path
from handler import *
from tornado.httpclient import AsyncHTTPClient
from sae.ext.storage import monkey
from sae.storage import Bucket
from sae.storage import Connection

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "templates")
STATIC_PATH = os.path.join(os.path.dirname(__file__), "files")

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', page.WelcomeHandler),
            (r'/login', user.LoginHandler),
            (r'/logout', user.LogoutHandler),
            (r'/signup', user.SignupHandler),
            (r'/me', user.UcHandler),
            (r'/makewish', wish.MakewishHandler),
            (r'/board', board.BoardHandler),
            (r'/board/(\d+)', board.BoardHandler),
            (r'/wish', wish.WishHandler),
            (r'/wish/(\d+)', wish.WishHandler),
            (r'/pickone', wish.PickoneHandler),
            (r'/pool', wish.WishpoolHandler),
            (r".*", page.NotfoundHandler)
        ]
        settings = dict(
            template_path = TEMPLATE_PATH, 
            static_path = STATIC_PATH, 
            login_url = "/login",
            cookie_secret = "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
            debug = True
        )
        tornado.web.Application.__init__(self, handlers, **settings)

application = Application()
