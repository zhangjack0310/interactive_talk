#coding:utf-8
import tornado.ioloop
import tornado.web
from tornado.web import RequestHandler
import time
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
        coloums = ['物品', '数量', '经办人']
        self.render('./ajjax.html',coloums=coloums)

class SendHandler(RequestHandler):
    def get(self):
        self.finish(str(time.time()))


application = tornado.web.Application([
    (r"/", MainHandler),
(r"/send_data", SendHandler),

], **settings)

if __name__ == "__main__":
    parse_command_line()
    application.listen(8887)
    tornado.ioloop.IOLoop.instance().start()