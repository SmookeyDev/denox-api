from tornado.web import RequestHandler
from modules.db import Database
from json import dumps

class MetricsReturn(RequestHandler):
    def set_default_headers(self):
        self.set_header("Content-Type", 'application/json')
    
    def get(self):
        data = Database().get_result_metrics()
        self.write(dumps(data))        