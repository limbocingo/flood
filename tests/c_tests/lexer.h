#include <stdio.h>

typedef struct
{
    char *value;
    enum
    {
        KEYWORD,
        OPERATOR,
        PUNCTUATION,
        STRING,
        INTEGER
    } type;
} Token;

void f_lex(char **lines);
