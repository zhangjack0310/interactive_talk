#coding:utf-8
import tornado.ioloop
import tornado.web
from tornado.web import RequestHandler
import time
import json
from datetime import datetime
from models import get_data, push_new_data
from tornado.options import define, options, parse_command_line
settings = {'debug':True,
            "static_path": "static",}
define("debug", default=True, help="run in debug mode")




class MainHandler(RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def get(self):
        data = get_data()
        head = data.get('key')
        # self.render('./ajjax.html', head=head)
        self.set_header("Content-Type", "application/json")
        self.finish({"laobzhang": "good"})

class SendHandler(RequestHandler):
    def get(self):
        data = get_data()

        head = data.get('key')
        res = data.get('info')
        html = "<tbody id='test'>"
        # print "</td><td>".join(head)
        for i in res:
            t = [i[k] for k in head]
            html += "<tr id='jq'><td></td><td>".format() + "</td><td>".join(t) + '</td></tr>'
        # print html
        html += '</tbody>'
        self.finish(html)


class GetDataSendHandler(RequestHandler):
    def get(self):
        data = get_data()
        info_data = data.get('info')
        head = data.get('key')
        new_info = {i:'' for i in head}
        new_info.update({"test":""})
        result = dict(info_data=info_data, head=head, new_info=new_info)
        self.set_header("Content-Type", "application/json")
        self.finish(json.dumps(result, ensure_ascii=False))

class SubmitHandler(RequestHandler):
    def post(self):
        info = self.request.body
        insert_data = eval(info)
        print insert_data
        if not insert_data.values() == ['']*len(insert_data):
            push_new_data(insert_data)
            data = get_data()
            info_data = data.get('info')
            head = data.get('key')
            result = dict(is_succ=True, data='success insert', info_data=info_data, head=head)
            self.set_header("Content-Type", "application/json")
            self.finish(json.dumps(result, ensure_ascii=False))
        else:
            result = dict(is_succ=False, data='empty data')
            self.set_header("Content-Type", "application/json")
            self.finish(json.dumps(result, ensure_ascii=False))



application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/send_data", SendHandler),
    (r"/submit_data", SubmitHandler),
    (r"/get_data", GetDataSendHandler),
    (r"/api/send_data", SendHandler),
    (r"/api/submit_data", SubmitHandler),
    (r"/api/get_data", GetDataSendHandler),
    ], **settings)

if __name__ == "__main__":
    parse_command_line()
    application.listen(8887)
    tornado.ioloop.IOLoop.instance().start()