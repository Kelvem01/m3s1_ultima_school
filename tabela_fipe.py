# criando classe de iteradores e geradores


import requests

class FipeIterator:
    # classe que itera sobre uma lista 

    def __init__(self,id_value:str): #criando metodo construtor

        url = 'https://parallelum.com.br/fipe/api/v1/carros/marcas/{}/modelos'
        url = url.format(id_value)
        headers = {'user-agent': 'MyStudyApp'}

        resposta = requests.get(url, headers = headers)
        carros = resposta.json()

        self.modelos = carros ['modelos']

        self.atual_elemento = 0
        self.proximo_elemento =1
        self.maximo = len(self.modelos)
    #fim do metodo construtor

    def __iter__(self):  # criando iterador 
        return self
    
    def __next__(self):
        if self.atual_elemento >= self.maximo:
            raise StopIteration
        
        resultado = self.modelos[self.atual_elemento]
        self.atual_elemento = self.proximo_elemento
        self.proximo_elemento += self.atual_elemento
        return resultado
    
marcas = FipeIterator('30')

for marca in marcas :
    print(marca)
