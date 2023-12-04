#include <stdio.h>
#include <stdio.h>
#include <stdlib.h>

#include "file.h"
#include "lexer.h"

void
lexer(char **lines) {
    for (int i = 0; Operators[i] != END; i++) 
    {
        printf("%d\n", Operators[i]);
    }
}
