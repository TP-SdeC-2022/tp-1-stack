libcotizacion.so: c_cotizacion.o asm_cotizacion.o 
	gcc -m32 -shared -W -o libcotizacion.so c_cotizacion.o asm_cotizacion.o

c_cotizacion.o:c_cotizacion.c
	gcc -m32 -c c_cotizacion.c

asm_cotizacion.o:asm_cotizacion.asm
	nasm -f elf32 asm_cotizacion.asm

asm_io.o:asm_io.asm
	nasm -f elf32 -d ELF_TYPE asm_io.asm