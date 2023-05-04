import requests
import api_url
from requests.exceptions import HTTPError, ConnectionError, Timeout


class DolarExchangeAPI:
    def __init__(self, url=api_url.url):
        self.url = url

    # Hacemos el request a la url y manejamos las posibles excepciones
    def call(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
            return http_err
        except ConnectionError as conn_err:
            print(f'Connection error occurred: {conn_err}')
            return conn_err
        except Timeout as timeout_err:
            print(f'Timeout error occurred: {timeout_err}')
            return timeout_err
        else:
            print('Success!')
            return response.json()


class DolarExchangeTypes:
    def __init__(self, exchange_type):
        self.exchange_type = exchange_type  # Tipo de cambio que queremos consultar

    def info_buy(self):
        # Devuelve el precio de compra del tipo de cambio deseado
        return dolar_info[self.exchange_type]['casa']['compra']

    def info_sell(self):
        # Devuelve el precio de venta del tipo de cambio deseado
        return dolar_info[self.exchange_type]['casa']['venta']


# Definimos los tipos de cambio disponibles
exchange_types = dict(Oficial=0,
                      Blue=1,
                      MayoristaBancos=2,
                      BCRA=3,
                      BancoNacionBillete=4,
                      BancoNacionPublico=5)

# Creamos un objeto de la clase DolarExchangeAPI para traer toda la informacion en formato json
dolar_info = DolarExchangeAPI().call()

# Creamos objetos para los tipos de cambio que deseamos consultar
dolar_oficial = DolarExchangeTypes(exchange_types['Oficial'])

dolar_blue = DolarExchangeTypes(exchange_types['Blue'])

dolar_mayoristas = DolarExchangeTypes(exchange_types['MayoristaBancos'])

dolar_bcra = DolarExchangeTypes(exchange_types['BCRA'])

dolar_bna_billete = DolarExchangeTypes(exchange_types['BancoNacionBillete'])

dolar_bna_publico = DolarExchangeTypes(exchange_types['BancoNacionPublico'])
