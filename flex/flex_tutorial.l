/* 
    Generate the generated code by flex flex_tutorial.l, than compile with -lfl

/* Definition Section:
   - Used for any C code that needs to be included, such as library imports or global definitions.
   - Here, no libraries or definitions are required.
*/
%{
#include <stdio.h>   /* Standard I/O library for printf() function */
%}


/* Rules Section:
   - Each rule specifies a pattern to match in the input, and an action to take when that pattern is found.
   - Patterns have priority from top to bottom: the first matching rule in the list takes precedence.
*/
%%
[a-z]   { 
          /* Action for lowercase letters (a to z):
             - Prints "Single lower case character" when any single lowercase letter is encountered.
             - Higher priority: This rule matches only single lowercase letters.
             
             Example:
               Input: 'a'  --> Output: "Single lower case character"
               Input: 'g'  --> Output: "Single lower case character"
          */
          printf("Single lower case character\n"); 
        }
.       { 
          /* Action for any other single character:
             - Matches any character not handled by other rules, printing "Not a lowercase character".
             - Lower priority than [a-z], so lowercase letters won't trigger this rule.
             
             Example:
               Input: 'A' --> Output: "Not a lowercase character"
               Input: '1' --> Output: "Not a lowercase character"
               Input: '?' --> Output: "Not a lowercase character"
          */
          printf("Not a lowercase character\n"); 
        }
\n      { 
          /* Action for newline character:
             - When a newline is detected, it returns 0, signaling the end of scanning.
             - Terminates input processing.
             
             Example:
               Input: '\n'  --> Ends yylex() execution
          */
          return 0; 
        }
%%

/* yywrap() Function:
   - Called when the end of file is reached.
   - Return 1 to indicate the end of input, or 0 to continue if there are more input files.
   - Here, it always returns 1, ending the scanning process after one file.
*/
int yywrap() {
    return 1;
}

int main() {
  /* Main Function:
     - Prompts user to enter a string, then calls yylex() to start scanning the input.
     - yylex() will process input according to the rules defined above until a newline is encountered.
     
     Example Execution:
       User Input: "aZ\n"
       Output:
         Enter string: 
         Single lower case character
         Not a lowercase character
  */
  printf("Enter string: ");
  yylex();   /* Start scanning input */
}

