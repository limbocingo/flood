#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "file.h"

#define MAX_LINE_SIZE 1024

long int sizef(FILE *file)
{
    fseek(file, 0L, SEEK_END);    // set postion end
    long int sizef = ftell(file); // get size
    fseek(file, 0L, SEEK_SET);    // set postion start

    return sizef;
}

FILE *openf(char *path)
{
    FILE *file;
    long int size;

    file = fopen(path, "r");
    if (file == NULL)
    {
        printf("ERROR: file not found\n");
        exit(1);
    }

    size = sizef(file);
    if (size == 0)
    {
        printf("%s: INFO: file is empty, closing\n", path);
        exit(1);
    }

    return file;
}

long int countlf(FILE *file)
{
    char cchar;
    long int lines;

    lines = 0;
    while ((cchar = getc(file)) != EOF) if (cchar == '\n') lines++;

    fseek(file, 0L, SEEK_SET); // set postion start

    return lines;
}

size_t *liness(FILE *file) {
    char cchar;
    long int current_size, filelc, cline;
    
    filelc = countlf(file);
    size_t *lines;

    lines = malloc(filelc * sizeof(size_t *));
    current_size = 0;
    cline = 0;
    while ((cchar = fgetc(file)) != EOF) {
        if (cchar == '\n') {
            lines[cline] = current_size + 1;
            current_size = 0;
            cline++;
        }
        current_size++;
    }
    printf("%li\n", cline);

    return lines;
}

/*
    TODO: resolve stack smashing detected
*/
char **readf(FILE *file, char *path)
{
    long int size, currl, nlines;
    size_t sizec;
    char **lines, content[MAX_LINE_SIZE];

    printf("%s: INFO: file open\n", path);

    size = sizef(file) + 1;
    nlines = countlf(file) + 6;

    printf("%s: INFO: file lines: `%li`\n", path, nlines);

    lines = malloc(nlines * sizeof(char *));
    currl = 0;
    while (fgets(content, size, file) != NULL)
    {
        lines[currl] = malloc(MAX_LINE_SIZE); // 1024
        strcpy(lines[currl], content);        // copy content >> array

        printf("%s: INFO: line added `%li`\n", path, currl);

        currl++;
    }
    lines[nlines] = '\0';

    printf("%s: INFO: file closed\n", path);
    fclose(file);

    return lines;
}
