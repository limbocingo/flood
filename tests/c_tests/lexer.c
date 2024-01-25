#include <stdio.h>
#include <stdio.h>
#include <stdlib.h>

#include "file.h"
#include "lexer.h"

Type
c_type(char c) 
{
    switch (c) 
    {
        ///////////////
        // Operators //
        ///////////////
        case '-':
            return OPERATOR; 
        case '+':
            return OPERATOR; 
        case '%':
            return OPERATOR;
        case '^':
            return OPERATOR;
        case '*':
            return OPERATOR;
        case '/':
            return OPERATOR;
        
        /////////////////
        // Punctuation //
        /////////////////
        case '"':
            return PUNCTUATION;
        case '(':
            return PUNCTUATION;
        case ')':
            return PUNCTUATION;
        case '[':
            return PUNCTUATION;
        case ']':
            return PUNCTUATION;
        case '#':
            return PUNCTUATION;
        case '=':
            return PUNCTUATION;
        case '>':
            return PUNCTUATION;
        case '<':
            return PUNCTUATION;
        case ',':
            return PUNCTUATION;
        case '.':
            return PUNCTUATION;
        case ';':
            return PUNCTUATION;
        case ':':
            return PUNCTUATION;
        case '{':
            return PUNCTUATION;
        case '}':
            return PUNCTUATION;
        case '&':
            return PUNCTUATION;
        case '@':
            return PUNCTUATION;
        case '|':
            return PUNCTUATION;
    }
}

void
f_tokenize(char **lines) 
{
    Token tokens[32][32];
    tokens[0]->type = STRING;
    tokens[0]->value = "dsadsads";
    
    
    
    printf("%s\n", tokens[0][0].value);
    printf("%d\n", tokens[0][0].type);
    printf("%d\n", c_type('@'));
}
