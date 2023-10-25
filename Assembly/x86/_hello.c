// gcc _hello.c -S -O0 -masm=intel -fno-stack-protector

#include <unistd.h>

int main() {
	const char message[] = "hello assembly";
	syscall(4, STDOUT_FILENO, message, sizeof(message) - 1);
	return 0;
}