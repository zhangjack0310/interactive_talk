#coding:utf-8
from tornado.web import RequestHandler,HTTPError
import json
from service import form_data,is_validate_user
from models import push_new_data,delete_data, edit_data
from utils import BaseHandler
import session
import tornado
import time





class MainHandler(BaseHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
    @tornado.web.authenticated
    def get(self):
        self.redirect('http://localhost/static/base.html')





class LoginHandler(BaseHandler):
    def get(self):
        self.render('static/login.html')

    def post(self):
        user = self.get_argument('user')
        password = self.get_argument('password')
        if is_validate_user(user, password):
            self.set_secure_cookie('user', session.Session.new(user))
            return self.redirect("/")
        else:
            return self.render('static/login.html', validate_user=False)

class GetDataSendHandler(BaseHandler):
    def get(self):
        result = form_data()
        self.set_header("Content-Type", "application/json")
        self.finish(json.dumps(result, ensure_ascii=False))

class SubmitHandler(BaseHandler):
    def post(self):
        info = self.request.body
        insert_data = eval(info)
        print insert_data
        if not insert_data.values() == ['']*len(insert_data):
            push_new_data(insert_data)
            result = dict(is_succ=True, data='success insert')
            result.update(form_data())
            self.set_header("Content-Type", "application/json")
            self.finish(json.dumps(result, ensure_ascii=False))
        else:
            result = dict(is_succ=False, data='empty data')
            self.set_header("Content-Type", "application/json")
            self.finish(json.dumps(result, ensure_ascii=False))


class DataDeleteHandler(BaseHandler):
    def get(self):
        index = self.get_argument('index', '')
        print index
        if index and index.isdigit():
            print delete_data(int(index))
            result = {"is_succ":True}
        else:
            result = {"is_succ": False}
        result.update(form_data())

        self.set_header("Content-Type", "application/json")
        self.finish(json.dumps(result, ensure_ascii=False))


class DataEditHandler(BaseHandler):
    def post(self):
        time.sleep(3)
        info = self.request.body
        edt_data = eval(info)
        print edt_data
        web_id = edt_data.get('web_id')
        if not web_id:
            raise HTTPError(403)
        edit_data(edt_data,web_id)

        self.finish()
