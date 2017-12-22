#coding:utf-8
import tornado.ioloop
import tornado.web
from tornado.options import define, options, parse_command_line
from views import MainHandler,SubmitHandler,GetDataSendHandler,DataDeleteHandler,LoginHandler
from settings import settings
define("debug", default=True, help="run in debug mode")






application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/api/submit_data", SubmitHandler),
    (r"/api/get_data", GetDataSendHandler),
    (r"/api/delete_data", DataDeleteHandler),
    (r"/login", LoginHandler),
    ], **settings)

if __name__ == "__main__":
    parse_command_line()
    application.listen(8887)
    tornado.ioloop.IOLoop.instance().start()