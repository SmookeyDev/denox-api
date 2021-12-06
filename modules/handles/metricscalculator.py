from modules.utils import Utils
from modules.metrics import Metrics
from modules.db import Database

from tornado.web import RequestHandler
from json import loads

class MetricsCalculator(RequestHandler):
    def post(self):
        body = loads(self.request.body)
        try:
            serial, initial_timestamp, final_timestamp = Utils().get_metrics_data(body) ## PEGA O BODY
            metrics_response = Metrics().metrics_calculator(serial, initial_timestamp, final_timestamp) ## EFETUA OS CALCULOS
            Database().set_result_metrics(metrics_response) ## SALVA OS RESULTADOS NO BANCO
        except Exception as e:
            self.set_status(400)
            self.finish("")