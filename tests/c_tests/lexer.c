#include <stdio.h>
#include <stdio.h>
#include <stdlib.h>

#include "file.h"
#include "lexer.h"

void
f_lex(char **lines) {
    Token tokens[32][32];
    tokens[0][0].type = STRING;
    tokens[0][0].value = "dsadsads";
    printf("%s", tokens[0][0].value);
}
