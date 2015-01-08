#coding:utf-8
import tornado.web
import json
import random
import re
from mysql import *
from base import *


class BoardHandler(BaseHandler):
    def get(self,id="1"):
        id = int(id)
        ret = query_for_list("SELECT * FROM `board` ORDER BY `id` DESC")
        self.render(
            "board.html",
            title="心愿说 - 留言板",
            msglist=ret,
            user=self.get_current_user(),
            id = id
            )
    def post(self):
        try:
            msg = self.get_argument("content", default="")
            name = self.get_argument("name", default="unknowuser")
            time = self.get_argument("time", default="")
            querysql = "SELECT * FROM `board` WHERE `content` = '%s'" % msg
            assert len(query_for_list(querysql)) == 0
            sql = "INSERT INTO `board` VALUES (NULL, '%s', '%s', '%s')" % (name, time, msg)
            execute_sql(sql)
            self.write("成功提交!!")
        except Exception:
            self.write("提交失败:(")