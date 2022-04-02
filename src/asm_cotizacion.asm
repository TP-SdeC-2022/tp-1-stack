segment .data
result DW 0

segment .bss

segment .text
        global  asm_cotizar
asm_cotizar:                      
        enter   0,0               ; setup routine
        pusha
        
        ;se realiza el calculo con los parametros recibidos a traves del stack
        mov     eax,[ebp + 12]
        mov     ebx,[ebp + 8]
        mul     ebx
        mov     [result], eax
        
        popa
        mov     eax, [result]            ; retorno a C a traves del registro EAX
        leave                     
        ret


