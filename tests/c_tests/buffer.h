#define RESET_POS(BUFFER) fseek( BUFFER, 0L, SEEK_SET )

extern size_t B_CountLetter ( FILE * buffer, char letter );
extern FILE * B_File (char const * path);