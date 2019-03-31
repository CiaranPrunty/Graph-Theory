# Graph-Theory

Ciaran Prunty : G00344402   3rd year Graph Theory Project 

The goal of the following graph theory project was to create a program that can convert a nondeterministic finite automaton(nfa) from a regular expression  , the nfa is then used to see if the regular expression matches any string given to the program.
By using the shunter’s algorithm you can take the given expression and go through each character of the String. When the first character is an open bracket ‘(‘ ,it is added to the stack . The other characters that will get added to the stack are ‘*’ ,  ’|’  and  ’.’ , 

if the next character's a 'b' then it is added to the post fix . If a ')' is encountered during the string then the first thing on the stack is added to the output (post fix) until all characters inside the string are covered.

I added the thompson constructor to mny code . The Thompson constructor parses the post fix expression from the shunter algorithm and turns it into a nfa. 

I was unable to get the expression matching completed correctly .
