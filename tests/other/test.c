#include <stdio.h>

char * lines[] = {};


void readf(char * filepath) {
    FILE * file = fopen(filepath, "r");
    if (file == NULL) {
        printf("ERROR:%s: file not found.\n", filepath);
        return;
    }

    fseek(file, 0L, SEEK_END);     // set postion end 
    long int lenght = ftell(file); // get size
    fseek(file, 0L, SEEK_SET);     // set postion start

    if (lenght == 0) {
        printf("INFO:%s: file is empty, closing...\n", filepath);
        return;
    }

    char * line;
    size_t llen = 0;

    int lnum = 0;
    while (getline(&line, &llen, file) != -1) {
        lines[lnum] = line;
        printf("%i", lnum);
        printf("%s", lines[lnum]);
        lnum++;
    }
    printf("%s\n", lines[1]);

    fclose(file);
}

int main(int argc, char *argv[])
{
    readf(argv[1]);

    return 0;
}