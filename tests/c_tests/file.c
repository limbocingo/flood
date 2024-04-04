#include <stdio.h>
#include <stdlib.h>

#include "error.c"

#include "file.h"
#include "buffer.h"


size_t
F_BufferSize (FILE * buffer)
{
    fseek(buffer, 0L, SEEK_END);
    return ftell(buffer);
}

size_t 
F_Size (FILE * buffer)
{
    size_t     buffer_size;
    buffer_size = F_BufferSize(buffer);
 
    RESET_POS(buffer);

    return buffer_size;
}

size_t 
F_LinesCount (FILE * buffer)
{
    size_t           lines_count;
    char             current_char;

    F_Search('\n');

    lines_count = 1;
    current_char  = BLANK;

    while ( current_char != EOF )  // EOF (end of the file)
    {
        current_char = getc(buffer);   

        if ( current_char == NEW_LINE )
            lines_count++;
    }

    RESET_POS(buffer);

    return lines_count;
}

size_t *
F_LinesSize (FILE * buffer)
{   
    size_t *        lines_size;
    size_t          line_size;
    
    size_t          buffer_lines;
    
    size_t          line_index;
    char            current_char;

    buffer_lines = F_LinesCount( buffer );

    lines_size = malloc( buffer_lines );
    if ( lines_size == NULL )
        // If for some reason the memory couldn't
        // be allocated (it's very impossible).
        F_GlobalError("device can not handle memmory alocation in `F_LinesSize`");
    
    for (line_size = 1; current_char != EOF; line_size++)
        if (line_index == buffer_lines)
            lines_size[line_index] = line_size;
        
        if (getc(buffer) == NEW_LINE) {
            line_index++;
            lines_size[line_index] = line_size;
            line_size = 1;
        }
    
    RESET_POS(buffer);
    
    return lines_size;
}

FILE *
F_Open (char const * path)
{
    FILE *           buffer;

    buffer = fopen(path, "r");
    if ( buffer == NULL )
        F_GlobalError("file not found");
 
    F_path = path; // Declare the path of the file globally

    return buffer;
}

char ** 
F_Lines (FILE * buffer)
{
    char **     lines;    
    size_t *    lines_size;
    size_t      lines_count;

    long int    current_line;

    lines_size = F_LinesSize(buffer);
    lines_count = F_LinesCount(buffer);
    
    lines = malloc(lines_count * sizeof(char *));

    if ( lines == NULL )
        // This shouldn't happen, but just in case.
        F_GlobalError("cannot allocate the memory");

    for ( current_line = 0; lines_count > current_line; current_line++ ) {
        lines[current_line] = malloc(lines_size[current_line]);
        fgets(lines[current_line], lines_size[current_line], buffer);
    }

    free(lines);
    fclose(buffer);

    return lines;
}
