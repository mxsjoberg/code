// 2020-11
#include <stdio.h>

int main(int argc, char *argv[]) {
    // filename
    printf("filename: %s\n", argv[0]);
    // arguments
    if (argc > 1) {
        printf("%s\n", "argv: ");
        for (int i = 1; i < argc; i++) {
            printf("\t%s\n", argv[i]);
        }
    }
}

// $ gcc hello-c.c -o _hello ; ./_hello
// filename: ./_hello

// $ gcc hello-c.c -o _hello-c.s -S -O0 -masm=intel -fno-stack-protector; cat _hello-c.s
// <asm>