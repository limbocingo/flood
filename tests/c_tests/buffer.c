#include <stdio.h>

#include "buffer.h"

FILE *
B_File (char const * path)
{
    return fopen(path, "r");
}

size_t
B_Size ( FILE * buffer )
{
    fseek(buffer, 0, SEEK_END);
    return ftell(buffer);
}

size_t
B_CountLetter ( FILE * buffer, char letter )
{
    printf("%zu", B_Size(buffer));
    rewind(buffer);
    return ftell(buffer);
}
