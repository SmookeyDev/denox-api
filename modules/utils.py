from math import radians, cos, sin, asin, sqrt
from modules.db import Database
from datetime import datetime

import itertools

class Utils():
    def __init__(self):
        self.db = Database()
        
    def collection_to_pairs(self, data):
        first, second = itertools.tee(data) ## DIVIDE OS DADOS EM DOIS ITERADORES
        next(first, None) ## PULA O PRIMEIRO ELEMENTO
        return list(zip(first, second)) ## RETORNA UMA LISTA COM OS PARES
    
    def distance_calculator(self, lon1, lat1, lon2, lat2):
        ## CONVERTE GRAUS DECIMAIS PARA RADIANOS
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
        
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        
        ## FORMULA DE HAVERSINE
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a))
        r = 6373.0 ## RAIO DA TERRA EM KM
        
        distance = r * c
        
        return distance
    
    def get_metrics_data(self, data):
        ## CONVERTE A DATA PARA TIMESTAMP E RETORNA OS DADOS NECESSÁRIOS
        initial_timestamp = int(datetime.strptime(data['datahora_inicio'], "%d/%m/%Y %H:%M:%S").timestamp()) 
        final_timestamp = int(datetime.strptime(data['datahora_fim'], "%d/%m/%Y %H:%M:%S").timestamp())
        return data['serial'], initial_timestamp, final_timestamp
    
