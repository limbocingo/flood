#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "file.h"

#define MAX_TOKEN_SIZE 70

char *lines[] = {};

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

struct Token tokens[flines];

Token **lexer(char *lines[])
{
    char *line;
    char *ctoken;
    char cchar;
    int lsize;

    int c;


    c = 0;
    Token **tokens[flines][20];
    tokens = malloc(sizeof(Token) + 3 * sizeof(potmeter *));
    tokens[0][0].name = "testing";
    tokens[0][0].type = KEYWORD;

    printf("%s", tokens[0][0].name);

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
    lines = readf(file);

    lexer(lines);
    return 0;
}