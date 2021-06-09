/*
    C is a general-purpose, procedural programming language developed by Dennis Ritchie in 1972.

    https://en.wikipedia.org/wiki/C_(programming_language)
*/

#include <stdio.h>

int main(void) {
    // do something
    printf("Hello world!");

    return 0;
}

/*
    command line arguments
    - argc: number of arguments
    - argv: pointer to array with arguments
*/
int main(int argc, char *argv[]) {
    // print file name
    printf("Running: %s\n", argv[0]);

    // print arguments
    if (argc > 1) {
        printf("%s\n", "Arguments: ");
        
        int i;
        for (i = 1; i < argc; i++) {
            printf("\t%s\n", argv[i]);
        }
    }
    // do something

    return 0;
}

/* 
    compile and run from command-line:
        $ gcc <filename>.c -o <filename>
        $ ./<filename>

    compile and run with makefile:
        main: <filename>.c
            gcc -o main <filename>.c

    compile and inspect assembly code:
        $ gcc <filename>.c -S

    build system (sublime text):
        {
            "shell": true,
            "cmd": ["gcc ${file} -o ${file_path}/${file_base_name} && ${file_path}/${file_base_name}"],
            "file_regex": "^(..[^:]*):([0-9]+):?([0-9]+)?:? (.*)$",
            "working_dir": "${file_path}",
        }
*/

// size in memory
int a = 10;
sizeof(a)
// 4

// pointer
(int) &a
// -389511672