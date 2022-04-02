import json
import requests
import ctypes

#se carga la libreria dinamica compilada en c y asm, definiendo los tipos de arg y ret de la funcion
libcotizacion = ctypes.CDLL('./libcotizacion.so')
libcotizacion.cotizacion.argtypes=(ctypes.c_uint,ctypes.c_uint,)
libcotizacion.cotizacion.restype=(ctypes.c_uint)

#se define un wrapper para la funcion de la libreria
def cotizar(cotizacion, precio):
    return libcotizacion.cotizacion(ctypes.c_uint(cotizacion),ctypes.c_uint(precio))

#se define la llamada a la API
def getprecio(monedacotizar, monedarequerida):
    rget = requests.get('https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency='+monedacotizar+ '&to_currency='+monedarequerida+'&apikey=9N3E66AEYSMKXXHT')
    dataget = json.loads(rget.text)
    precio = dataget['Realtime Currency Exchange Rate']['5. Exchange Rate']
    return float(precio)

#se obtiene el precio de las cotizaciones
BTCtoUSD = getprecio('BTC','USD')
ETHtoUSD = getprecio('ETH','USD')
USDtoARS = getprecio('USD','ARS')
USDtoEUR = getprecio('USD','EUR')

#se desplaza la coma un lugar hacia la derecha y se castea a entero
BTCtoUSDi=int(BTCtoUSD*10)
ETHtoUSDi=int(ETHtoUSD*10)
USDtoARSi=int(USDtoARS*10)
USDtoEURi=int(USDtoEUR*10)

#se realiza el calculo de cotizacion correspondiente llamando a la funcion wrapper y se desplza la coma 2 lugares hacia la izquierda
print('COTIZACION BITCOIN')
print('%.2f' % BTCtoUSD + ' USD')
BTCtoARS=cotizar(BTCtoUSDi,USDtoARSi)/100
print('%.2f' % BTCtoARS + ' ARS')
BTCtoEUR=cotizar(BTCtoUSDi,USDtoEURi)/100
print('%.2f' % BTCtoEUR + ' EUR')

print('COTIZACION ETHEREUM')
print('%.2f' % ETHtoUSD + ' USD')
ETHtoARS=cotizar(ETHtoUSDi,USDtoARSi)/100
print('%.2f' % ETHtoARS + ' ARS')
ETHtoEUR=cotizar(ETHtoUSDi,USDtoEURi)/100
print('%.2f' % ETHtoEUR + ' EUR')
