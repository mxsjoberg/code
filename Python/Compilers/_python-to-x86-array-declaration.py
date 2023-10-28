from mako.template import Template

def codegen(name, values):
    code_template = """section .data
    ${name} db ${values}

section .text
global _start

_start:
    mov eax, 1      ; sys_write
    xor ebx, ebx    ; stdout
    int 0x80        ; syscall
"""

    code = Template(code_template)
    return code.render(name=name, values="".join(str(value) for value in values))

print(codegen("array", [1, 2, 3]))
# section .data
#     array db 123

# section .text
# global _start

# _start:
#     mov eax, 1      ; sys_write
#     xor ebx, ebx    ; stdout
#     int 0x80        ; syscall