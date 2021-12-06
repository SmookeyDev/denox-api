from modules.utils import Utils
from sklearn.cluster import KMeans

class Metrics():
    def __init__(self):
        self.utils = Utils()
        
        self.total_distance = 0
        self.moving_time = 0 
        self.stopped_time = 0
        
        self.current_latitude = 0
        self.current_longitude = 0
        self.last_latitude = 0
        self.last_longitude = 0
        
        self.stopped_positions = []
        self.centroids = []
        
    def metrics_calculator(self, serial, start_time, end_time):
        travels = self.utils.db.get_tracking_data(serial, start_time, end_time) ## PEGA OS DADOS DE VIAGENS
        pairs_travels = self.utils.collection_to_pairs(travels) ## CONVERTE EM PARES
        
        for pair in pairs_travels:
            travel1, travel2 = pair ## PEGA O PAR
            self.total_distance += self.utils.distance_calculator(travel1['longitude'], travel1['latitude'], travel2['longitude'], travel2['latitude']) ## CALCULA A DISTANCIA DOIS PONTOS
            
            if travel1['situacao_movimento'] == True: ## SE O PRIMEIRO PONTO FOR MOVIMENTO
                self.moving_time += int(travel2['datahora']) - int(travel1['datahora']) ## SOMA O TEMPO DE MOVIMENTO
                
            if travel1['situacao_movimento'] == False: ## SE O PRIMEIRO PONTO ESTIVER PARADO
                self.stopped_time += int(travel2['datahora']) - int(travel1['datahora']) ## SOMA O TEMPO PARADO
        
        for travel in travels:
            if travel['situacao_movimento'] == False: ## SE O PONTO ESTIVER PARADO
                self.current_latitude = travel['latitude'] ## PEGA A LATITUDE
                self.current_longitude = travel['longitude'] ## PEGA A LONGITUDE
                
                if self.last_latitude != self.current_latitude and self.last_longitude != self.current_longitude: ## SE O PONTO FOR DIFERENTE DO ANTERIOR
                    self.last_latitude = self.current_latitude ## DEFINE A LATITUDE ATUAL PARA A ANTERIOR
                    self.last_longitude = self.current_longitude  ## DEFINE A LONGITUDE ATUAL PARA A ANTERIOR
                    self.stopped_positions.append([self.current_latitude, self.current_longitude]) ## ADICIONA A POSIÇÃO NO ARRAY
             
        
        self.total_distance = round(self.total_distance, 2) ## ARREDONDA A DISTANCIA
        
        if len(self.stopped_positions) > 0: ## SE O NÚMERO DE PARADAS FOR MAIOR QUE ZERO
            kmeans = KMeans(n_clusters=len(self.stopped_positions)) ## CRIA UM KMEANS COM O TAMANHO DO ARRAY
            kmeans.fit(self.stopped_positions) ## ADICIONA OS PONTOS NO KMEANS
            self.centroids = kmeans.cluster_centers_.tolist() ## PEGA OS CENTROIDES
            
        return {
            "distancia_percorrida": self.total_distance,
            "tempo_em_movimento": self.moving_time,
            "tempo_parado": self.stopped_time,
            "centroides_paradas": self.centroids,
            "serial": serial
        } ## RETORNA OS DADOS