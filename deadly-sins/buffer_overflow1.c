#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

// Compiling: gcc -g -w -fno-stack-protector -z execstack -o buffer_overflow1 buffer_overflow1.c
int main(int argc, char *argv[]){
    char buf[4];
    strcpy(buf, argv[1]);
    printf("%s\n", buf);
    return 0;
}
