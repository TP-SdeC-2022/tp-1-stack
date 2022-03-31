import json
import requests
import ctypes

libcotizacion = ctypes.CDLL('./libcotizacion.so')

libcotizacion.cotizacion.argtypes=(ctypes.c_uint,ctypes.c_uint,)
libcotizacion.cotizacion.restype=(ctypes.c_uint)

url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey=9N3E66AEYSMKXXHT'
r = requests.get(url)
data = json.loads(r.text)
BTCtoUSD = data['Realtime Currency Exchange Rate']['5. Exchange Rate']

url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=ARS&apikey=9N3E66AEYSMKXXHT'
r = requests.get(url)
data = json.loads(r.text)
USDtoARS = data['Realtime Currency Exchange Rate']['5. Exchange Rate']

BTCf=float(BTCtoUSD)*10
USDf=float(USDtoARS)*10

BTCi=int(BTCf)
USDi=int(USDf)

print(BTCf)
print(USDf)
print(BTCi)
print(USDi)

cotizado=libcotizacion.cotizacion(ctypes.c_uint(BTCi),ctypes.c_uint(USDi))
cotizadocond=cotizado/100
print("retorno en python:")
print(cotizado)
print(cotizadocond)
