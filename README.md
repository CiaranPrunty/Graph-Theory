# Graph-Theory

Ciaran Prunty : G00344402   3rd year Graph Theory Project 

The goal of the following graph theory project was to create a program that can convert a nondeterministic finite automaton(nfa) from a regular expression  , the nfa is then used to see if the regular expression matches any string given to the program.
By using the shunter’s algorithm you can take the given expression and go through each character of the String. When the first character is an open bracket ‘(‘ ,it is added to the stack . The other characters that will get added to the stack are ‘*’ ,  ’|’  and  ’.’ , 
