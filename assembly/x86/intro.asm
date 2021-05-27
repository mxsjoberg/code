; program (intel syntax)
section .text
    global      start                   ; start point for execution

start:
    mov         rax, 0x02000004         ; write
    mov         rdi, 1                  ; stdout
    mov         rsi, message            ; address of string to output
    mov         rdx, 12                 ; bytes
    syscall                             ; invoke to write
    mov         rax, 0x02000001         ; exit
    xor         rdi, rdi                ; 0
    syscall                             ; invoke to exit

; declare data used in program
section .data

message:
    db          "hello assembly", 10       ; db -> raw bytes, text + newline = 11 + 1 = 12, line feed = 0xa = 10 = \n

; run from command-line (64-bit MacOS):
;   $ nasm -f macho64 intro.asm
;   $ ld -macosx_version_min 10.7.0 -o intro intro.o
;   $ ./intro

; build system (sublime text):
; {
;     "shell": true,
;     "cmd": ["nasm -f macho64 ${file} && ld -no_pie -macosx_version_min 10.7.0 -o ${file_path}/${file_base_name} ${file_path}/${file_base_name}.o && ${file_path}/${file_base_name}"],
;     "file_regex": "^(..[^:]*):([0-9]+):?([0-9]+)?:? (.*)$",
;     "working_dir": "${file_path}",
; }