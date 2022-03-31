

;
; file: skel.asm
; This file is a skeleton that can be used to start assembly programs.

%include "asm_io.inc"
segment .data
;
; initialized data is put in the data segment here
;
result DW 0


segment .bss
;
; uninitialized data is put in the bss segment
;


 

segment .text
        global  asm_cotizar
asm_cotizar:
        enter   0,0               ; setup routine
        pusha
        
        mov     eax,[ebp + 12]
        mov     ebx,[ebp + 8]
        mul     ebx
        mov     [result], eax
        
        popa
        mov     eax, [result]            ; return back to C
        leave                     
        ret


