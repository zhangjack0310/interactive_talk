#coding:utf-8
from tornado.web import RequestHandler
import json
from service import form_data
from models import get_data, push_new_data,delete_data
from utils import BaseHandler
import session




class MainHandler(BaseHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def get(self):

        self.redirect('http://localhost/static/aj1.html')





class LoginHandler(BaseHandler):
    def get(self):
        self.write('<html><body><form action="/login" method="post">'
                   'Name: <input type="text" name="name">'
                   '<input type="submit" value="Sign in">'
                   '</form></body></html>')

    def post(self):
        cookie = self.get_argument('name')
        session.Session.new(cookie)
        self.redirect("/")

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
        index = self.get_argument('index','')
        print index
        if index and index.isdigit():
            print delete_data(int(index))
            result = {"is_succ":True}
        else:
            result = {"is_succ": False}
        result.update(form_data())

        self.set_header("Content-Type", "application/json")
        self.finish(json.dumps(result, ensure_ascii=False))
