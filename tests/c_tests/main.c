#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "file.h"

#define MAX_TOKEN_SIZE 70

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
} Token[5];

Token **lexer(char *lines[])
{
    Token tokens[5];

    // printf("\n");
    // for (int nline = 0; nline < flines; nline++)
    // {
    //     line = lines[nline];
    //     lsize = strlen(line);
    //     printf("%d", lsize);

    //     for (int nchar = 0; nchar < lsize; nchar++) {
    //         cchar = line[nchar];
    //         printf("%s", tokens[line][c]);
    //         if (cchar == ' ') {
    //             c++;
    //             tokens[nline][c];
    //         }
    //         else {
    //             strncat(tokens[nline][c], &cchar, 1);
    //         }
    //     }
    // }
    // printf("\n");
}

int main(int argc, char *argv[])
{
    char **lines;
    FILE *file;

    file = openf(argv[1]);
    // lines = readf(file, argv[1]);
    size_t *_liness = liness(file);
    size_t linesc = sizeof(_liness) * sizeof(_liness[0]);
    printf("%u\n", linesc);
    for (long int i = 0; i < linesc; i++) {
        printf("%u `%d`\n", i, _liness[i]);
    }
    //lexer(lines);

    return 0;
}