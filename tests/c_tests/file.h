#include <stdio.h>

extern FILE *openf(char *path);
extern char **readf(FILE *file, char *path);
extern size_t *liness(FILE *file);
