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
	mov	dword ptr [rbp - 8], edi
	mov	qword ptr [rbp - 16], rsi
	mov	rax, qword ptr [rbp - 16]
	mov	rsi, qword ptr [rax]
	lea	rdi, [rip + L_.str]
	mov	al, 0
	call	_printf
	cmp	dword ptr [rbp - 8], 1
	jle	LBB0_6
## %bb.1:
	lea	rdi, [rip + L_.str.1]
	lea	rsi, [rip + L_.str.2]
	mov	al, 0
	call	_printf
	mov	dword ptr [rbp - 20], 1
LBB0_2:                                 ## =>This Inner Loop Header: Depth=1
	mov	eax, dword ptr [rbp - 20]
	cmp	eax, dword ptr [rbp - 8]
	jge	LBB0_5
## %bb.3:                               ##   in Loop: Header=BB0_2 Depth=1
	mov	rax, qword ptr [rbp - 16]
	movsxd	rcx, dword ptr [rbp - 20]
	mov	rsi, qword ptr [rax + 8*rcx]
	lea	rdi, [rip + L_.str.3]
	mov	al, 0
	call	_printf
## %bb.4:                               ##   in Loop: Header=BB0_2 Depth=1
	mov	eax, dword ptr [rbp - 20]
	add	eax, 1
	mov	dword ptr [rbp - 20], eax
	jmp	LBB0_2
LBB0_5:
	jmp	LBB0_6
LBB0_6:
	xor	eax, eax
	add	rsp, 32
	pop	rbp
	ret
	.cfi_endproc
                                        ## -- End function
	.section	__TEXT,__cstring,cstring_literals
L_.str:                                 ## @.str
	.asciz	"filename: %s\n"

L_.str.1:                               ## @.str.1
	.asciz	"%s\n"

L_.str.2:                               ## @.str.2
	.asciz	"argv: "

L_.str.3:                               ## @.str.3
	.asciz	"\t%s\n"

.subsections_via_symbols
