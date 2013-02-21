#coding:utf-8
import os
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
from tornado.web import Application
from handler.home import HomeHandler
from tornado import options
import constant
import logging

options.define(name='port', default=8888, type=int, help='the server port')
handlers = [
    (r'/$', HomeHandler)
]

class MyApplication(Application):
    
    def __init__(self):
        
        settings = {
            'static_path': os.path.join(os.path.dirname(__file__), "static"),
            'template_path': os.path.join(os.path.dirname(__file__), "template"),
            'debug':constant.DEBUG
        }
        super(MyApplication, self).__init__(handlers=handlers, **settings)
        
    def log_request(self, handler):
        'log every request'
        
        logger = logging.getLogger('Tours.MyApplication')
        if handler.get_status() < 400:
            log_method = logger.info
        elif handler.get_status() < 500:
            log_method = logger.warning
        else:
            log_method = logger.error
        request_time = 1000.0 * handler.request.request_time()
        log_method("%d %s %.2fms", handler.get_status(), handler._request_summary(), request_time)

if __name__ == '__main__':
    options.parse_command_line()
    port = options.options.port
    application = MyApplication()
    server = HTTPServer(application, xheaders=True)
    server.listen(port)
    print 'server start at port %s' %port
    IOLoop.instance().start()