#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "file.h"

#define MAX_TOKEN_SIZE 70

char *lines[] = {};

typedef struct
{
    char *name;
    enum Type
    {
        KEYWORD,
        OPERATOR,
        PUNCTUATION,
        STRING,
        INTEGER
    } type;
} Token;



Token **lexer(char *lines[])
{
    char *line;
    char *ctoken;
    char cchar;
    int lsize;

    printf("\n");
    ctoken = malloc(MAX_TOKEN_SIZE);
    for (int nline = 0; nline < flines; nline++)
    {
        line = lines[nline];
        lsize = strlen(line);
        printf("%d", lsize);

        for (int nchar = 0; nchar < lsize; nchar++) {
            cchar = line[nchar];
            printf("%s", ctoken);
            if (cchar == ' ') {
                ctoken = "";
            }
            else {
                strncat(ctoken, cchar, 1);
            }
        }
    }
    printf("\n");
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