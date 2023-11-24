#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>

char ** readf(char *filepath, char* lines[]) {
    FILE * fp;

    char * line = NULL;
    size_t len  = 0;
    
    ssize_t line_len;

    fp = fopen(filepath, "r");

    if (fp == NULL) {
        printf("ERROR:%s: file not found.\n", filepath);
        exit(1);
    }

    int i = 0;
    while ((line_len = getline(&line, &len, fp)) != -1) {
        printf("%s", lines[i]);
        lines[i] = line;
        i++;
    }

    fclose(fp);
    if (line)
        free(line);
    
    return lines;
}

int main(void)
{
    char * path    = "test.flood";
    char * lines[];
    readf(path, lines);
    // int  size     = sizeof(lines) / sizeof(lines[0]);
    printf("%s\n", lines[0]);

    return 0;
}