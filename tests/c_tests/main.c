#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "buffer.h"


int main(int argc, char *argv[])
{
    FILE * file = B_File(argv[0]);
    size_t count = B_CountLetter(file, 't');
    return 0;
}
