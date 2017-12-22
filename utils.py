from tornado.web import RequestHandler
import session


class BaseHandler(RequestHandler):
    def get_current_user(self):
        cookie = self.get_secure_cookie('user')
        if not cookie:
            return None
        else:
            return cookie

    def prepare(self):
        print self.current_user

