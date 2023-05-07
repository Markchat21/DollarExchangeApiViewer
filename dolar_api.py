import requests
import api_url
from requests.exceptions import HTTPError, ConnectionError, Timeout


class DollarExchangeAPI:
    def __init__(self, url=api_url.url, status_message=None, data=None, exchange_num=None):
        self.url = url
        self.status_message = status_message
        self.data = data
        self.exchange_num = exchange_num

    # Hacemos el request a la url y manejamos las posibles excepciones
    def call(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
            self.status_message = http_err
        except ConnectionError as conn_err:
            print(f'Connection error occurred: {conn_err}')
            self.status_message = conn_err
        except Timeout as timeout_err:
            print(f'Timeout error occurred: {timeout_err}')
            self.status_message = None
        except Exception as other_err:
            print(f'Other error ocurred: {other_err}')
            self.status_message = other_err
        else:
            print('Success!')
            self.status_message = None
            self.data = response.json()

    def info_buy(self):
        # Devuelve el precio de compra del tipo de cambio deseado
        return self.data[self.exchange_num]['casa']['compra']

    def info_sell(self):
        # Devuelve el precio de venta del tipo de cambio deseado
        return self.data[self.exchange_num]['casa']['venta']


class DollarExchangeTypes(DollarExchangeAPI):
    def __init__(self):
        DollarExchangeAPI.__init__(self, url=api_url.url, status_message=None, data=None)

    def dollar_oficial(self):
        self.exchange_num = exchange_types['Oficial']

    def dollar_blue(self):
        self.exchange_num = exchange_types['Blue']

    def dollar_bcra(self):
        self.exchange_num = exchange_types['BCRA']

    def dollar_mayorista(self):
        self.exchange_num = exchange_types['MayoristaBancos']

    def dollar_bna_billete(self):
        self.exchange_num = exchange_types['BancoNacionBillete']

    def dollar_bna_publico(self):
        self.exchange_num = exchange_types['BancoNacionPublico']


# Definimos los tipos de cambio disponibles
exchange_types = dict(Oficial=0,
                      Blue=1,
                      MayoristaBancos=2,
                      BCRA=3,
                      BancoNacionBillete=4,
                      BancoNacionPublico=5)
