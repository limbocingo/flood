#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "file.h"
#include "lexer.h"


int main(int argc, char *argv[])
{
    FILE   *file    = f_buf(argv[1]);
    char  **f_lines = f_read_by_lines(file);    
    
    f_tokenize(f_lines);

    return 0;
}
