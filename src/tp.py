import json
import requests
import ctypes

libcotizacion = ctypes.CDLL('./libcotizacion.so')
libcotizacion.cotizacion.argtypes=(ctypes.c_uint,ctypes.c_uint,)
libcotizacion.cotizacion.restype=(ctypes.c_uint)

def cotizar(cotizacion, precio):
    return libcotizacion.cotizacion(ctypes.c_uint(cotizacion),ctypes.c_uint(precio))

def getprecio(monedacotizar, monedarequerida):
    rget = requests.get('https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency='+monedacotizar+ '&to_currency='+monedarequerida+'&apikey=9N3E66AEYSMKXXHT')
    dataget = json.loads(rget.text)
    return dataget['Realtime Currency Exchange Rate']['5. Exchange Rate']


BTCtoUSD = getprecio('BTC','USD')
ETHtoUSD = getprecio('ETH','USD')
USDtoARS = getprecio('USD','ARS')
USDtoEUR = getprecio('USD','EUR')

BTCtoUSDi=int(float(BTCtoUSD)*10)
ETHtoUSDi=int(float(ETHtoUSD)*10)
USDtoARSi=int(float(USDtoARS)*10)
USDtoEURi=int(float(USDtoEUR)*10)

print('1 Bitcoin = ' + str(BTCtoUSD) + 'USD')
BTCtoARS=cotizar(BTCtoUSDi,USDtoARSi)/100
print('1 Bitcoin = ' + str(BTCtoARS) + 'ARS')
BTCtoEUR=cotizar(BTCtoUSDi,USDtoEURi)/100
print('1 Bitcoin = ' + str(BTCtoEUR) + 'EUR')

print('1 Ethereum = ' + str(ETHtoUSD) + 'USD')
ETHtoARS=cotizar(ETHtoUSDi,USDtoARSi)/100
print('1 Ethereum = ' + str(ETHtoARS) + 'ARS')
ETHtoEUR=cotizar(ETHtoUSDi,USDtoEURi)/100
print('1 Ethereum = ' + str(ETHtoEUR) + 'EUR')
