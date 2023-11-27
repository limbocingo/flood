#include <stdio.h>


#include "file.h"

char *lines[] = {};

int main(int argc, char *argv[])
{
    char **lines;
    lines = readf(argv[1]);
    for (int i = 0; i < 3; i++) {
        printf("%s", lines[i]);
    }


    return 0;
}