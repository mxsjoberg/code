; 2021-05
; x86-64 (intel syntax)
    section .text
    global _main

_main:
    mov rax, 0x02000004     ; write (4)
    mov rdi, 1              ; stdout
    mov rsi, message        ; address of output
    mov rdx, 10             ; bytes : "hello x86" + /n = 10
    syscall                 ; invoke write
    mov rax, 0x02000001     ; exit (1)
    xor rdi, rdi            ; 0
    syscall                 ; invoke to exit

    section .data

message:
    db "hello x86", 10      ; define byte : text, \n (10)

; $ nasm -f macho64 hello-x86.asm 
; $ ld hello-x86.o -o _hello -lSystem -L/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/lib
; $ ./_hello
; hello x86