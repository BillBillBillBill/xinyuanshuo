#coding:utf-8
import tornado.web
from mysql import *
from base import *

class WishHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self,wishid):
        querysql = "SELECT * FROM `wish` WHERE `ID` = '%s'" % wishid
        wl = query_for_list(querysql)
        self.render(
            "wish.html",
            title="心愿说 - 愿望",
            user=self.get_current_user().decode('UTF-8'),
            wishid=wishid,
            wish=wl[0]
            )

    def post(self):
        try:
            optype = self.get_argument("optype")
            wishid = self.get_argument("wishid")
            user = self.get_current_user().decode('UTF-8')
            querysql = "SELECT * FROM `wish` WHERE `ID` = '%s'" % wishid
            wl = query_for_list(querysql)
            if optype == "delete":
                assert user == wl[0]['user']
                querysql = "DELETE FROM `wish` WHERE `ID` = '%s'" % wishid
                execute_sql(querysql)
                self.write("成功删除")
            elif optype == "complete":
                assert user == wl[0]['user']
                if wl[0]['status'][0] == u'已':
                    self.write("已成功完成!")
                    return
                helpuser = "by"+wl[0]['status'][:-4] if len(wl[0]['status'])!=3 else ""
                querysql = u"UPDATE `wish` SET `status` = '已完成%s' WHERE `ID` = '%s'" % (helpuser,wishid)
                execute_sql(querysql)
                self.write("成功完成!")
            elif optype == "join":
                assert user != wl[0]['user']
                if wl[0]['status'] == u"求实现":
                    querysql = u"UPDATE `wish` SET `status` = '%s' WHERE `ID` = '%s'" % (user+u"正在帮助",wishid)
                    execute_sql(querysql)
                    self.write("成功完成!")
                else:
                    self.write("已经有人帮忙啦!")
        except Exception,e:
            self.write("出错了:"+str(e))

class PickoneHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        user=self.get_current_user().decode("utf-8")
        querysql = u"SELECT * FROM `wish` WHERE `status` = '求实现' AND `user` != '%s' ORDER BY RAND() LIMIT 1" % user
        wl = query_for_list(querysql)
        self.render(
            "wish.html",
            title="心愿说 - 手气不错",
            user=self.get_current_user().decode('UTF-8'),
            wishid=wl[0]['ID'],
            wish=wl[0]
            )


class WishpoolHandler(BaseHandler):
    def get(self):
        querysql = u"SELECT * FROM `wish` WHERE `status` = '求实现' ORDER BY `ID` DESC"
        wl_need = query_for_list(querysql)
        querysql = u"SELECT * FROM `wish` WHERE `status` NOT LIKE '%%已完成%%' AND `status` != '求实现' ORDER BY `ID` DESC"
        wl_ing = query_for_list(querysql)
        querysql = u"SELECT * FROM `wish` WHERE `status` LIKE '%%已完成%%' ORDER BY `ID` DESC"
        wl_finish = query_for_list(querysql)
        self.render(
            "wishpool.html",
            title="心愿说 - 许愿池",
            user=self.get_current_user(),
            wishlist_need=wl_need,
            wishlist_ing=wl_ing,
            wishlist_finish=wl_finish,
            )

class MakewishHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render(
            "makewish.html",
            title="心愿说 - 许愿",
            user=self.get_current_user()
            )
    def post(self):
        try:
            wish = self.get_argument("wish")
            user = self.get_current_user().decode('UTF-8')
            time = self.get_argument("time", default="")
            contact = self.get_argument("contact")
            reward = self.get_argument("reward")
            sql = u"INSERT INTO `wish` (`ID` ,`user` ,`time` ,`wish` ,`contact` ,`reward` ,`status`) VALUES (NULL, '%s', '%s', '%s', '%s', '%s', '求实现')" % (user, time, wish, contact, reward)
            execute_sql(sql)
            self.write("成功提交~")
        except Exception,e:
            self.write("出错了:"+str(e))
