#include <stdio.h>

enum Operator
{   
    SUM='+',
    MINUS='-',
    MULTIPLIER='*',

    OP_COUNT,

    END=-1
};

static const enum Operator Operators[] = {
    SUM,
    MINUS,
    MULTIPLIER,

    OP_COUNT,

    END
};

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

void lexer(char **lines);
