#include <stdio.h>
#include <stdlib.h>

#include "file.h"

const char *F_path;
size_t      F_lines;

size_t
f_size(FILE *f)
{
    size_t f_size;
    
    fseek(f, 0L, SEEK_END);
    f_size = ftell(f);
    fseek(f, 0L, SEEK_SET);

    return f_size;
}

size_t
f_lines_count(FILE *f)
{
    char   f_curr_char;
    size_t f_lines;

    f_lines = 0;   
    while ( ( f_curr_char = getc(f) ) != EOF ) 
    {
        if (f_curr_char == '\n') 
            f_lines++;
    }

    fseek(f, 0L, SEEK_SET);

    return f_lines;
}

FILE *
f_buf(char const *path)
{
    FILE   *f;
    size_t  _f_size;

    f = fopen(path, "r");
    if (f == NULL)
    {
        printf("?: error: file not found\n");
        exit(EXIT_FAILURE);
    }

    _f_size = f_size(f);
    if (_f_size == 0)
    {
        printf("%s: error: file is empty, closing\n", path);
        exit(EXIT_FAILURE);
    }

    F_path  = path;
    F_lines = f_lines_count(f) + 1;

    return f;
}

size_t *
f_lines_size(FILE *f)
{   
    size_t   *f_lines_size;

    size_t   f_char_index;
    long int f_curr_line;
    char     f_curr_char;

    f_lines_size = malloc((F_lines) * sizeof(*f_lines_size));
    if (f_lines_size == NULL) {
        printf("%s: error: device can not handle the file\n", F_path);
        exit(EXIT_FAILURE);
    }

    f_curr_line  = 0;
    f_char_index = 0;
    while (( f_curr_char = fgetc(f) ) != EOF) {
        f_char_index++;
        if (f_curr_char == '\n') {
            f_lines_size[f_curr_line] = f_char_index + 1;

            f_char_index = 0;
            f_curr_line++;
        }
    }
    f_lines_size[f_curr_line] = f_char_index;

    fseek(f, 0L, SEEK_SET); 
    
    return f_lines_size;
}

char ** 
f_read_by_lines(FILE *f) // rbl: read by lines
{
    char    **f_lines;    
    size_t   *_f_lines_size;
    long int  f_curr_line_index;

    printf("%s: info: starting to read file...\n", F_path);
    printf("%s: info: file lines: `%li`\n", F_path, F_lines);

    _f_lines_size = f_lines_size(f);
    
    f_lines = malloc(F_lines * sizeof(char *));
    if (f_lines == NULL) {
        printf("%s: error: device can not handle the file\n", F_path);
        exit(EXIT_FAILURE);
    }

    for (f_curr_line_index = 0; F_lines > f_curr_line_index; f_curr_line_index++) {
        f_lines[f_curr_line_index] = malloc(_f_lines_size[f_curr_line_index]);
        fgets(f_lines[f_curr_line_index], _f_lines_size[f_curr_line_index] + 1, f);
    }

    printf("%s: info: closing file...\n", F_path);
    fclose(f);
    printf("%s: info: file closed\n", F_path);

    return f_lines;
}
