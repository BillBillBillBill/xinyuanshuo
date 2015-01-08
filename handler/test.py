#coding:utf-8
import tornado.web, json, os.path, MySQLdb
from mysql import *
from handler.board import BoardHandler
from tornado.httpclient import AsyncHTTPClient
from sae.ext.storage import monkey
from sae.storage import Bucket
from sae.storage import Connection
import sae.const

class TestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
            "test.html",
            title="测试页面"
            )
    def post(self):
        try:
            code = self.get_argument("content", default="SELECT * FROM db WHERE ID = 1")
            # ret = execute_sql(code)
            ret = query_for_list(code)
            self.write("succeed"+str(ret))
        except Exception,e:
            self.write(str(e))
