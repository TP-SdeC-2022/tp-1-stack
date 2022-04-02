#include "cdecl.h"
#include <stdio.h>

unsigned PRE_CDECL asm_cotizar( unsigned int cotizacion, unsigned int precio) POST_CDECL;

unsigned cotizacion(unsigned int cotizacion, unsigned int precio)
{
    unsigned ret_status;
    ret_status = asm_cotizar(cotizacion,precio);
    return ret_status;
}
