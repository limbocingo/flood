#include <stdio.h>

extern const char    *F_path;
extern       size_t   F_lines;

extern char  **f_read_by_lines(FILE *f);
extern FILE   *f_buf(char const *path);
