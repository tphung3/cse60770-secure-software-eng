#include <stdio.h>

// Compiling: gcc -g -w -o buffer_overflow1 buffer_overflow1.c
int main(int argc, char *argv[]){
    char buf[4];
    strcpy(buf, argv[1]);
    printf("%s\n", buf);
    return 0;
}

