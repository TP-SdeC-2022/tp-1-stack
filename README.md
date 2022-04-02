# TP#1 - CALCULADORA DE COTIZACION DE CRIPTOMONEDAS
## Stack - Sartori Gaston - Tantera Julian

Para la implementacion del programa de 3 capas se utilizaron los siguientes lenguajes:
- Capa superior: Python
- Capa intermedia: C
- Capa inferior: Assembly

### Capa superior: Python
En esta capa se utilizo la API de Alpha Vantage para la obtencion de la cotizacion de 2 criptomonedas: Bitcoin y Ethereum. Tambien se obtuvieron de la misma, la cotizacion entre USD y ARS, y entre USD y EUR.
Obtenida esta informacion, se utiliza como parametro para la invocaciuon de la capa intermedia para que realize el calculo de conversion entre monedas. Ej: \
    API get -> BTCtoUSD, USDtoARS \
    Llamada a capa intermedia -> BTCtoUSD, USDtoARS \
    Retorno de capa intermedia <- BTCtoARS 

### Capa intermedia: C
Esta capa funciona como intermediario entre la capa superior y la capa inferior. Al ser invocada por la capa superior, lo unico que realiza es invocar a la capa inferior con los parametros recibidos de la primera, y retornarle a esta, el resultado obtenido por la capa inferior.Ej: \
    Invocacion desde capa superior <- BTCtoUSD, USDtoARS \
    Llamada a capa inferior -> BTCtoUSD, USDtoARS \
    Retorno de capa inferior <- BTCtoARS \
    Retorno a capa superior -> BTCtoARS 

### Capa inferior: Assembly 
En esta capa es donde se realiza el calculo de conversion, es invocada por la capa intermedia con los parametros necesarios y se realiza el calculo, retornando el resultado obtenido.Ej: \
    Invocacion desde capa intermedia <- BTCtoUSD, USDtoARS \
    Calculo = BTCtoUSD x USDtoARS = BTCtoARS \
    Retorno a capa intermedia -> BTCtoARS 

### Comunicacion entre capas superior e intermedia
Para la comunicacion entre los lenguajes de capa superior, Pyton, y el de capa intermedia, C, se utilizo la libreria de Python CTypes, para utilizar una DLL compilada en C.
El codigo de C y Assembly, es compilado y linkeado en una DLL, la cual luego es utilizada desde el programa Python. Se define un wrapper en Python para la funcion en C a invocar y se invoca como cualquier otra funcion de Python.

### Comunicacion entre capas intermedia e inferior
La comunicacion entre la capa intermedia e inferior se realiza a traves de las conveciones de llamadas estandar de C. Esto define que los parametros se comunican a traves del stack. Y el retono se realiza a traves del registro EAX. 

