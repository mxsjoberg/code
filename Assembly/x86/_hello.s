	.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 13, 0	sdk_version 13, 3
	.intel_syntax noprefix
	.globl	_main                           ## -- Begin function main
	.p2align	4, 0x90
_main:                                  ## @main
	.cfi_startproc
## %bb.0:
	push	rbp
	.cfi_def_cfa_offset 16
	.cfi_offset rbp, -16
	mov	rbp, rsp
	.cfi_def_cfa_register rbp
	sub	rsp, 32
	mov	dword ptr [rbp - 4], 0
	mov	rax, qword ptr [rip + L___const.main.message]
	mov	qword ptr [rbp - 19], rax
	mov	eax, dword ptr [rip + L___const.main.message+8]
	mov	dword ptr [rbp - 11], eax
	mov	ax, word ptr [rip + L___const.main.message+12]
	mov	word ptr [rbp - 7], ax
	mov	al, byte ptr [rip + L___const.main.message+14]
	mov	byte ptr [rbp - 5], al
	lea	rdx, [rbp - 19]
	mov	edi, 4
	mov	esi, 1
	mov	ecx, 14
	mov	al, 0
	call	_syscall
	xor	eax, eax
	add	rsp, 32
	pop	rbp
	ret
	.cfi_endproc
                                        ## -- End function
	.section	__TEXT,__cstring,cstring_literals
L___const.main.message:                 ## @__const.main.message
	.asciz	"hello assembly"

.subsections_via_symbols
