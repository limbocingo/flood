#include <stdio.h>
#include <stdlib.h>


#include "file.h"


void
F_GlobalError (char * message)
{
    printf("%s: error: %s\n", F_path, message);
    exit(EXIT_FAILURE);
}
