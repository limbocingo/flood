#include <stdio.h>

#define NEW_LINE     '\n'
#define BLANK        ' '
#define NOT_FOUND    '?'

#define RESET_POS(BUFFER) fseek( BUFFER, 0L, SEEK_SET )


extern   const char *      F_path;

extern   char **           F_Lines ( FILE *       buffer );
extern   FILE *            F_Open (  char const * path );
