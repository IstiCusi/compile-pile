
%{
#include <stdio.h>

#define IDENTIFIER 1
#define INTEGER 2
#define FLOAT 3
#define STRING 4
#define COMMENT 5
#define BRACES 6
#define BRACKETS 7
#define PARENTHESIS 8
#define VAR 9
%}

WHITESPACE   [ \t\n]+
IDENTIFIER   [a-zA-Z_][a-zA-Z0-9_]*
INTEGER      [0-9]+
FLOAT        [0-9]+\.[0-9]*([eE][-+]?[0-9]+)?
STRING       "\"([^\"\\]|\\.)*\"|'([^'\\]|\\.)*'"
COMMENT      #.*\n
BRACES       \{[^}]*\}
BRACKETS     \[[^\]]*\]
PARENTHESIS  \([^)]*\)
VAR          \$[a-zA-Z_][a-zA-Z0-9_]*

%%

{WHITESPACE}     { }
{IDENTIFIER}     { printf("Identifier: %s\n", yytext); return IDENTIFIER; }
{INTEGER}        { printf("Integer: %s\n", yytext); return INTEGER; }
{FLOAT}          { printf("Float: %s\n", yytext); return FLOAT; }
{STRING}         { printf("String: %s\n", yytext); return STRING; }
{COMMENT}        { printf("Comment: %s\n", yytext); }
{BRACES}         { printf("Braces content: %s\n", yytext); return BRACES; }
{BRACKETS}       { printf("Brackets content: %s\n", yytext); return BRACKETS; }
{PARENTHESIS}    { printf("Parenthesis content: %s\n", yytext); return PARENTHESIS; }
{VAR}            { printf("Variable: %s\n", yytext); return VAR; }
.                { printf("Unknown character: %c\n", yytext[0]); return yytext[0]; }

%%

int main(int argc, char **argv) {
  printf("Input: ");
  int token;
  while ((token = yylex())) {
    switch (token) {
      case IDENTIFIER:
        printf("-> Found an identifier.\n");
        break;
      case INTEGER:
        printf("-> Found an integer.\n");
        break;
      case FLOAT:
        printf("-> Found a float.\n");
        break;
      case STRING:
        printf("-> Found a string.\n");
        break;
      case BRACES:
        printf("-> Found content in braces.\n");
        break;
      case BRACKETS:
        printf("-> Found content in brackets.\n");
        break;
      case PARENTHESIS:
        printf("-> Found content in parentheses.\n");
        break;
      case VAR:
        printf("-> Found a variable.\n");
        break;
      default:
        printf("-> Found an unhandled token.\n");
        break;
    }
  }
  return 0;
}
