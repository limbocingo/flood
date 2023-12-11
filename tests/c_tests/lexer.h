#include <stdio.h>

typedef enum
{
    KEYWORD,
    OPERATOR,
    PUNCTUATION,
    STRING,
    INTEGER,
    UNKNOWN
} Type;

typedef struct
{
    char *value;
    Type  type;
} Token;

void f_lex(char **lines);
