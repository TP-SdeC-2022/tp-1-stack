#include "cdecl.h"
#include <stdio.h>

//declaracion de modulo asm a invocar, especificando el uso de la convencion de llamadas estandar de C
unsigned PRE_CDECL asm_cotizar( unsigned int cotizacion, unsigned int precio) POST_CDECL;

//funcion que se usara para la invocacion desde capa superior
unsigned cotizacion(unsigned int cotizacion, unsigned int precio)
{
    unsigned ret_status;
    //se llama a la capa inferior
    ret_status = asm_cotizar(cotizacion,precio); //los parametros son cargados en el stack y el retorno a traves de EAX
    return ret_status; //se retorna el resultado 
}
