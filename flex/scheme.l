%{
#include <stdio.h>
#define MAX_STRING 1024
char strbuf[MAX_STRING];
int str_index = 0;

void print_token(const char* token_type, const char* yytext) {
    printf("%s: %s\n", token_type, yytext);
}
void add_to_buffer(const char* text) {
    for (int i = 0; text[i] != '\0' && str_index < MAX_STRING - 1; i++) {
        strbuf[str_index++] = text[i];
    }
    strbuf[str_index] = '\0';
}
%}

%x STRING

%%

\(                   { print_token("Left Parenthesis", yytext); }
\)                   { print_token("Right Parenthesis", yytext); }
define               { print_token("Keyword 'define'", yytext); }
lambda               { print_token("Keyword 'lambda'", yytext); }
if                   { print_token("Keyword 'if'", yytext); }
else                 { print_token("Keyword 'else'", yytext); }
cond                 { print_token("Keyword 'cond'", yytext); }
quote                { print_token("Keyword 'quote'", yytext); }
set!                 { print_token("Keyword 'set!'", yytext); }
#[tf]                { print_token("Boolean Literal", yytext); }

-?[0-9]+                     { print_token("Integer Literal", yytext); }
-?[0-9]*\.[0-9]+([eE][-+]?[0-9]+)? { print_token("Floating Point Literal", yytext); }

\"                   { BEGIN(STRING); str_index = 0; }
<STRING>[^\"\\\n]+   { add_to_buffer(yytext); }
<STRING>\\n          { add_to_buffer("\n"); }
<STRING>\\t          { add_to_buffer("\t"); }
<STRING>\\\"         { add_to_buffer("\""); }
<STRING>\\           { add_to_buffer("\\"); }
<STRING>\"           { print_token("String Literal", strbuf); BEGIN(INITIAL); }
<STRING>\n           { printf("Error: Unterminated String\n"); BEGIN(INITIAL); }

\'[a-zA-Z][-a-zA-Z0-9]* { print_token("Symbol", yytext); }
;[^\n]*                 { }
[-+*/]                  { print_token("Arithmetic Operator", yytext); }
[a-zA-Z][-a-zA-Z0-9]*   { print_token("Identifier", yytext); }
[ \t]+                  { }
\n                      { return 0; }
.                       { print_token("Unknown Character", yytext); }

%%

int yywrap() {
    return 1;
}

int main() {
    printf("Input: ");
    yylex();
    return 0;
}

