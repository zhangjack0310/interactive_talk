#coding:utf-8
import tornado.ioloop
import tornado.web
from tornado.web import RequestHandler
import time
import json
from datetime import datetime
from models import get_data
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
        self.render('./ajjax.html', head=head)

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


class SubmitHandler(RequestHandler):
    def get(self):
        pass



application = tornado.web.Application([
    (r"/", MainHandler),
(r"/send_data", SendHandler),

], **settings)

if __name__ == "__main__":
    parse_command_line()
    application.listen(8887)
    tornado.ioloop.IOLoop.instance().start()