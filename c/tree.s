	.file	"tree.c"
	.intel_syntax noprefix
	.text
	.type	e, @function
e:
	push	r14
	movsx	r14, ecx
	lea	r8d, 1[rcx]
	push	r13
	mov	r13d, r8d
	push	rbp
	mov	rbp, rdx
	push	rbx
	mov	ebx, esi
	sub	rsp, 24
	movsx	r9d, BYTE PTR 68[rdx+r14]
	add	r9d, ecx
.L2:
	cmp	r9d, r13d
	jle	.L9
	mov	ecx, r13d
	mov	rdx, rbp
	mov	esi, ebx
	mov	DWORD PTR 12[rsp], r8d
	mov	DWORD PTR 8[rsp], r9d
	mov	QWORD PTR [rsp], rdi
	call	e
	test	eax, eax
	jne	.L5
	movsx	rax, r13d
	mov	r8d, DWORD PTR 12[rsp]
	mov	r9d, DWORD PTR 8[rsp]
	movsx	eax, BYTE PTR 68[rbp+rax]
	mov	rdi, QWORD PTR [rsp]
	add	r13d, eax
	jmp	.L2
.L9:
	movsx	rdx, ebx
	mov	sil, BYTE PTR 4[rbp+r14]
	xor	eax, eax
	cmp	BYTE PTR 4[rdi+rdx], sil
	jne	.L1
	movsx	edx, BYTE PTR 68[rdi+rdx]
	push	rax
	mov	rcx, rbp
	lea	esi, 1[rbx]
	push	0
	add	edx, ebx
	call	mt
	pop	rdx
	pop	rcx
	test	eax, eax
	setne	al
	movzx	eax, al
	jmp	.L1
.L5:
	mov	eax, 1
.L1:
	add	rsp, 24
	pop	rbx
	pop	rbp
	pop	r13
	pop	r14
	ret
	.size	e, .-e
	.type	mt, @function
mt:
	push	r15
	mov	eax, 1
	push	r14
	push	r13
	push	r12
	push	rbp
	push	rbx
	sub	rsp, 24
	mov	QWORD PTR [rsp], rdi
	mov	DWORD PTR 12[rsp], r8d
	cmp	esi, edx
	jge	.L10
	mov	ebx, esi
	mov	r15d, edx
	mov	r13, rcx
	mov	r14d, r9d
	mov	ebp, r8d
	xor	r12d, r12d
.L12:
	cmp	ebp, r14d
	jge	.L21
	mov	eax, DWORD PTR 80[rsp]
	bt	eax, r12d
	jc	.L13
	mov	rdi, QWORD PTR [rsp]
	mov	ecx, ebp
	mov	rdx, r13
	mov	esi, ebx
	call	e
	test	eax, eax
	je	.L13
	mov	rdx, QWORD PTR [rsp]
	movsx	rax, ebx
	mov	rcx, r13
	mov	r9d, r14d
	movsx	esi, BYTE PTR 68[rdx+rax]
	push	rax
	mov	edx, r15d
	mov	eax, DWORD PTR 88[rsp]
	add	esi, ebx
	bts	eax, r12d
	push	rax
	mov	r8d, DWORD PTR 28[rsp]
	mov	rdi, QWORD PTR 16[rsp]
	call	mt
	pop	rdx
	pop	rcx
	test	eax, eax
	jne	.L16
.L13:
	movsx	rax, ebp
	inc	r12d
	movsx	eax, BYTE PTR 68[r13+rax]
	add	ebp, eax
	jmp	.L12
.L21:
	xor	eax, eax
	jmp	.L10
.L16:
	mov	eax, 1
.L10:
	add	rsp, 24
	pop	rbx
	pop	rbp
	pop	r12
	pop	r13
	pop	r14
	pop	r15
	ret
	.size	mt, .-mt
	.type	add, @function
add:
	push	r15
	lea	rax, 4[rdi]
	lea	r15, 68[rdi]
	push	r14
	push	r13
	xor	r13d, r13d
	push	r12
	push	rbp
	mov	rbp, rdi
	push	rbx
	sub	rsp, 24
	mov	r12, QWORD PTR P[rip]
	movsx	rbx, DWORD PTR np[rip]
	mov	QWORD PTR [rsp], rax
	lea	r14, 68[r12]
.L23:
	cmp	ebx, r13d
	jle	.L35
	movsx	rdx, DWORD PTR 0[rbp]
	cmp	DWORD PTR -68[r14], edx
	jne	.L24
	mov	rsi, QWORD PTR [rsp]
	lea	rdi, -64[r14]
	mov	QWORD PTR 8[rsp], rdx
	call	memcmp@PLT
	test	eax, eax
	jne	.L24
	mov	rdx, QWORD PTR 8[rsp]
	mov	rsi, r15
	mov	rdi, r14
	call	memcmp@PLT
	test	eax, eax
	je	.L22
.L24:
	inc	r13d
	add	r14, 132
	jmp	.L23
.L35:
	cmp	ebx, DWORD PTR cap[rip]
	jne	.L27
	mov	esi, 64
	test	ebx, ebx
	je	.L28
	lea	esi, [rbx+rbx]
.L28:
	mov	DWORD PTR cap[rip], esi
	movsx	rsi, esi
	mov	rdi, r12
	imul	rsi, rsi, 132
	call	realloc@PLT
	mov	QWORD PTR P[rip], rax
.L27:
	lea	eax, 1[rbx]
	mov	ecx, 33
	mov	rsi, rbp
	imul	rbx, rbx, 132
	add	rbx, QWORD PTR P[rip]
	mov	DWORD PTR np[rip], eax
	mov	rdi, rbx
	rep movsd
.L22:
	add	rsp, 24
	pop	rbx
	pop	rbp
	pop	r12
	pop	r13
	pop	r14
	pop	r15
	ret
	.size	add, .-add
	.type	f, @function
f:
	push	r15
	push	r14
	push	r13
	push	r12
	push	rbp
	push	rbx
	mov	ebx, edi
	sub	rsp, 216
	lea	r12, 144[rsp]
.L37:
	mov	eax, DWORD PTR lv[rip]
	mov	DWORD PTR [rsp], eax
	mov	rax, QWORD PTR lvl[rip]
	mov	QWORD PTR 16[rsp], rax
	cmp	DWORD PTR [rsp], ebx
	jg	.L62
	movsx	rax, DWORD PTR [rsp]
	mov	rsi, QWORD PTR 16[rsp]
	mov	rcx, QWORD PTR 16[rsp]
	lea	r15, 0[0+rax*4]
	movsx	r8, DWORD PTR -4[rsi+r15]
	mov	eax, DWORD PTR [rcx+rax*4]
	mov	DWORD PTR 8[rsp], r8d
	imul	r14, r8, 132
	mov	DWORD PTR 40[rsp], eax
.L38:
	mov	esi, DWORD PTR 8[rsp]
	cmp	DWORD PTR 40[rsp], esi
	jle	.L63
	xor	r13d, r13d
.L43:
	mov	rax, QWORD PTR P[rip]
	mov	DWORD PTR 44[rsp], r13d
	mov	DWORD PTR 28[rsp], r13d
	cmp	r13d, DWORD PTR [rax+r14]
	jge	.L64
	xor	r11d, r11d
.L42:
	mov	rax, QWORD PTR P[rip]
	add	rax, r14
	cmp	r11d, DWORD PTR N[rip]
	mov	QWORD PTR 32[rsp], rax
	jge	.L65
	mov	rsi, QWORD PTR 32[rsp]
	lea	rdi, 76[rsp]
	mov	ecx, 33
	mov	edx, 132
	rep movsd
	mov	esi, DWORD PTR 44[rsp]
	lea	rdi, 80[rsp]
	mov	DWORD PTR 60[rsp], r11d
	movsx	eax, BYTE PTR [r12+r13]
	lea	r8d, [rax+rsi]
	movsx	rbp, r8d
	mov	DWORD PTR 56[rsp], r8d
	lea	rax, 5[rbp]
	lea	r10, 1[rbp]
	cmp	rax, rdx
	lea	rsi, [rdi+rbp]
	mov	QWORD PTR 48[rsp], r10
	cmovb	rax, rdx
	mov	edx, DWORD PTR 76[rsp]
	add	rdi, r10
	sub	rax, r10
	sub	edx, r8d
	lea	rcx, -4[rax]
	movsx	rdx, edx
	call	__memmove_chk@PLT
	mov	eax, 132
	lea	rcx, 69[rbp]
	mov	r10, QWORD PTR 48[rsp]
	cmp	rcx, rax
	mov	edx, DWORD PTR 76[rsp]
	mov	r8d, DWORD PTR 56[rsp]
	lea	rsi, [r12+rbp]
	cmovb	rcx, rax
	lea	rdi, [r12+r10]
	sub	edx, r8d
	sub	rcx, r10
	movsx	rdx, edx
	sub	rcx, 68
	call	__memmove_chk@PLT
	mov	r11d, DWORD PTR 60[rsp]
	inc	DWORD PTR 76[rsp]
	xor	eax, eax
	mov	BYTE PTR 144[rsp+rbp], 1
	mov	BYTE PTR 80[rsp+rbp], r11b
.L40:
	mov	rcx, QWORD PTR 32[rsp]
	movsx	edx, BYTE PTR 68[rcx+rax]
	add	edx, eax
	cmp	DWORD PTR 28[rsp], edx
	jge	.L39
	inc	BYTE PTR [r12+rax]
.L39:
	inc	rax
	cmp	DWORD PTR 28[rsp], eax
	jge	.L40
	lea	rdi, 76[rsp]
	mov	DWORD PTR 32[rsp], r11d
	call	add
	mov	r11d, DWORD PTR 32[rsp]
	inc	r11d
	jmp	.L42
.L65:
	inc	r13
	jmp	.L43
.L64:
	inc	DWORD PTR 8[rsp]
	add	r14, 132
	jmp	.L38
.L63:
	mov	rdi, QWORD PTR 16[rsp]
	lea	rsi, 8[r15]
	call	realloc@PLT
	mov	edx, DWORD PTR [rsp]
	mov	QWORD PTR lvl[rip], rax
	inc	edx
	mov	DWORD PTR lv[rip], edx
	mov	edx, DWORD PTR np[rip]
	mov	DWORD PTR 4[rax+r15], edx
	jmp	.L37
.L62:
	movsx	r13, ebx
	mov	ebp, ebx
	lea	r15, S[rip]
	xor	r12d, r12d
	lea	r14, 4[0+r13*4]
.L45:
	mov	rax, QWORD PTR lvl[rip]
	cmp	DWORD PTR [rax+r14], r12d
	jle	.L36
	imul	rdx, r12, 132
	xor	r8d, r8d
	add	rdx, QWORD PTR P[rip]
	mov	eax, 1
.L50:
	cmp	ebx, r8d
	jle	.L53
	test	eax, eax
	je	.L48
	mov	rdi, QWORD PTR [r15+r8*8]
	xor	ecx, ecx
	xor	esi, esi
	mov	QWORD PTR 8[rsp], r8
	mov	QWORD PTR [rsp], rdx
	call	e
	mov	r8, QWORD PTR 8[rsp]
	mov	rdx, QWORD PTR [rsp]
	test	eax, eax
	sete	al
	inc	r8
	movzx	eax, al
	jmp	.L50
.L53:
	test	eax, eax
	je	.L48
	lea	rax, S[rip]
	lea	edi, 1[rbx]
	mov	QWORD PTR [rax+r13*8], rdx
	call	f
	cmp	ebp, eax
	cmovl	ebp, eax
.L48:
	inc	r12
	jmp	.L45
.L36:
	add	rsp, 216
	mov	eax, ebp
	pop	rbx
	pop	rbp
	pop	r12
	pop	r13
	pop	r14
	pop	r15
	ret
	.size	f, .-f
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC0:
	.string	"%d\n"
	.section	.text.startup,"ax",@progbits
	.globl	main
	.type	main, @function
main:
	push	r13
	push	r12
	push	rbp
	mov	ebp, 3
	push	rbx
	sub	rsp, 152
	dec	edi
	jle	.L67
	mov	rdi, QWORD PTR 8[rsi]
	call	atoi@PLT
	mov	ebp, eax
.L67:
	mov	edi, 8
	mov	DWORD PTR N[rip], ebp
	xor	r12d, r12d
	xor	r13d, r13d
	call	malloc@PLT
	mov	rbx, rax
	mov	QWORD PTR lvl[rip], rax
	xor	eax, eax
	mov	DWORD PTR [rbx], eax
.L68:
	cmp	r12d, ebp
	jge	.L73
	mov	eax, r13d
	lea	rdi, 16[rsp]
	mov	ecx, 32
	mov	DWORD PTR 12[rsp], 1
	rep stosd
	lea	rdi, 12[rsp]
	mov	BYTE PTR 16[rsp], r12b
	inc	r12d
	mov	BYTE PTR 80[rsp], 1
	call	add
	jmp	.L68
.L73:
	mov	eax, DWORD PTR np[rip]
	xor	edi, edi
	mov	DWORD PTR lv[rip], 1
	mov	DWORD PTR 4[rbx], eax
	call	f
	lea	rsi, .LC0[rip]
	mov	edi, 2
	mov	edx, eax
	xor	eax, eax
	call	__printf_chk@PLT
	add	rsp, 152
	xor	eax, eax
	pop	rbx
	pop	rbp
	pop	r12
	pop	r13
	ret
	.size	main, .-main
	.local	S
	.comm	S,524288,32
	.local	N
	.comm	N,4,4
	.local	lvl
	.comm	lvl,8,8
	.local	lv
	.comm	lv,4,4
	.local	cap
	.comm	cap,4,4
	.local	np
	.comm	np,4,4
	.local	P
	.comm	P,8,8
	.section	.note.GNU-stack,"",@progbits
