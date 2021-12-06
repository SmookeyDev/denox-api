from tornado.web import Application
from tornado.ioloop import IOLoop

from modules.handles.metricscalculator import MetricsCalculator
from modules.handles.metricsreturn import MetricsReturn


def make_app():
    return Application([
        (r"/api/calcula_metricas", MetricsCalculator),
        (r"/api/retorna_metricas", MetricsReturn)
    ])
    
if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    IOLoop.current().start()