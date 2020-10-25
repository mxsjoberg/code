; NOTE: 64-bit MacOS
;
; nasm -f macho64 intro.asm
; ld -macosx_version_min 10.7.0 -o intro intro.o
; ./intro

section .text
    global      start

start:
    mov         rax, 0x02000004         ; write
    mov         rdi, 1                  ; stdout
    mov         rsi, message            ; address of string to output
    mov         rdx, 13                 ; bytes
    syscall                             ; invoke to write
    mov         rax, 0x02000001         ; exit
    xor         rdi, rdi                ; 0
    syscall                             ; invoke to exit

section .data

message:
    db          "hello world", 10       ; NOTE: db = 1 byte ; text + newline = 12 byte

; assemble:
;   $ nasm -f macho64 <filename>.asm (output is <filename>.o)

; link and create executable:
;   $ ld -macosx_version_min 10.7.0 -o <filename> <filename>.o

; run:
;   $ ./<filename>