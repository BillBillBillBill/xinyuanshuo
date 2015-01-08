#coding:utf-8
import tornado.web
from mysql import *
from base import *

class LoginHandler(BaseHandler):
    def get(self):
        self.render(
            "login.html",
            title="心愿说 - 登录",
            user=self.get_current_user(),
            msg="")
    def post(self):
        querysql = "SELECT * FROM `user` WHERE `name` = '%s' AND `password` = '%s'" % (self.get_argument("username",""), self.get_argument("password",""))
        if len(query_for_list(querysql)) != 0:
            self.set_secure_cookie("user", self.get_argument("username"))
            self.redirect("/")
        else:
            self.render(
            "login.html",
            title="心愿说 - 登录",
            user=self.get_current_user(),
            msg="帐户名或登录密码不正确，请重新输入"
            )

class LogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie("user")
        self.redirect("/")


class SignupHandler(BaseHandler):
    def get(self):
        self.render(
            "signup.html",
            user=self.get_current_user(),
            title="心愿说 - 注册")
    def post(self):
        try:
            name = self.get_argument("username")
            password = self.get_argument("password")
            querysql = "SELECT * FROM `user` WHERE `name` = '%s'" % name
            assert len(query_for_list(querysql)) == 0
            sql = "INSERT INTO `user` (`ID`, `name`, `password`, `task`, `wish`) VALUES (NULL, '%s', '%s', '', '')" % (name, password)
            execute_sql(sql)
            self.set_secure_cookie("user", name)
            self.write("注册成功")
        except Exception:
            self.write("用户名/密码不符合规范或已存在相同的用户名")

class UcHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        user=self.get_current_user().decode("utf-8")
        querysql = u"SELECT * FROM `wish` WHERE `status` = '求实现' AND `user` = '%s'" % user
        wl_need = query_for_list(querysql)
        querysql = u"SELECT * FROM `wish` WHERE `status` NOT LIKE '%%已完成%%' AND `status` != '求实现' AND `user` = '"+user+"'"
        wl_ing = query_for_list(querysql)
        querysql = u"SELECT * FROM `wish` WHERE `status` LIKE '%%已完成%%' AND `user` = '"+user+"'"
        wl_finish = query_for_list(querysql)
        status1 = user+u"正在帮助"
        status2 = u"已完成by"+user
        querysql = "SELECT * FROM `wish` WHERE `status` = '%s' OR `status` = '%s'" % (status1,status2)
        helpwl = query_for_list(querysql)
        self.render(
            "usercenter.html",
            title="心愿说 - 个人中心",
            user=self.get_current_user(),
            wishlist_need=wl_need,
            wishlist_ing=wl_ing,
            wishlist_finish=wl_finish,
            helpwl=helpwl
            )

