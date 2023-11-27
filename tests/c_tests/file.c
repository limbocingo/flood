#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "file.h"

#define MAX_LINE_SIZE 79

long int sizef(FILE *file)
{
    fseek(file, 0L, SEEK_END);    // set postion end
    long int sizef = ftell(file); // get size
    fseek(file, 0L, SEEK_SET);    // set postion start

    return sizef;
}

FILE *openfr(char *path)
{
    FILE *file;
    long int size;

    file = fopen(path, "r");
    if (file == NULL)
    {
        printf("NOTFOUND: ERROR: file not found.\n", path);
        exit(1);
    }

    size = sizef(file);
    if (size == 0)
    {
        printf("%s: INFO: file is empty, closing...\n", path);
        exit(1);
    }

    return file;
}

int countlf(FILE *file)
{
    char cchar;
    int lines;

    lines = 1;
    while ((cchar = getc(file)) != EOF)
    {
        if (cchar == '\n')
            lines++;
    }

    fseek(file, 0L, SEEK_SET); // set postion start

    return lines;
}

char **readf(char *path)
{
    FILE *file;

    long int size;
    char **lines, content[MAX_LINE_SIZE];
    int currl;

    file = openfr(path);
    size = sizef(file);

    lines = malloc(countlf(file) * sizeof(char *));
    currl = 0;
    while (fgets(content, size, file) != NULL)
    {
        lines[currl] = malloc(sizeof(content)); // allocate memory

        strncpy(lines[currl], content, sizeof(content)); // copy the line in the array

        lines[3] = '\0';
        currl++;
    }

    fclose(file);

    return lines;
}
