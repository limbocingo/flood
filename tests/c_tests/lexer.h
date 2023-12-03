#include <stdio.h>

typedef struct
{
    char *name;
    char *value;
    enum Type
    {
        KEYWORD,
        OPERATOR,
        PUNCTUATION,
        STRING,
        INTEGER
    } type;
} Token;
