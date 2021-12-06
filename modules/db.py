from decouple import config

import pymongo

class Database:
    def __init__(self):
        self.client = pymongo.MongoClient(F'mongodb://{config("DB_USER")}:{config("DB_PASS")}@{config("DB_HOST")}:{config("DB_PORT")}/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&ssl=false')
        self.db = self.client[config("DB_NAME")]
        
    def get_tracking_data(self, serial, initial_timestamp, final_timestamp):
        query = self.db.dados_rastreamento.find({'serial': serial, 'datahora': {'$gte': initial_timestamp, '$lte': final_timestamp}})
        query_array = sorted(list(query), key=lambda x: x['datahora'])
        return(query_array)
    
    def set_result_metrics(self, data):
        query = self.db.resultados_icaro.insert_one({'distancia_percorrida': data['distancia_percorrida'], 'tempo_em_movimento': data['tempo_em_movimento'], 'tempo_parado': data['tempo_parado'], 'centroides_paradas': data['centroides_paradas'], 'serial': data['serial']})
        return(query)
    
    def get_result_metrics(self):
        query = self.db.resultados_icaro.find({}, {'_id': False})
        return(list(query))