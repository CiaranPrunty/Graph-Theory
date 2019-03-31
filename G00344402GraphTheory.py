# G00344402 Ciaran Prunty

def shunt(infix):
    """The Shunting Yard Algorithm for converting infix regular 
    expressions to post fix """

    specials = {'*': 50, '.': 40, '|': 30, '?': 30, '+':30}
    # creates dictionary

    # profix and stack variables
    postfix = ""
    stack = ""

    # forloop that will parse the expression
    for c in infix:
        # first if adds the opening bracket to the stack
        if c == '(':
            stack = stack + c
        # the ( bracket is on the stack, if the for loop encounters a ) bracket we check the stack
        # going to check the stack all the way down until we find the open braket in the stack.
        elif c == ')':
            # while loops through the stack until it encounters the ( bracket. it also adds everything it encounter along the way to the postfix variable.
            while stack[-1] != '(':
                postfix = postfix + stack[-1]
                stack = stack[:-1]
            # removes the ( bracket so there's nothing left in the stack.
            stack = stack[:-1]
        elif c in specials:
            # if stack isn't empty, the while will execute.
            while stack and specials.get(c, 0) <= specials.get(stack[-1], 0):
                postfix = postfix + stack[-1]
                stack = stack[:-1]
            stack = stack + c
        else:
            postfix = postfix + c


    # anything left on stack after running though the for loop needs to be added to the end of the post fix 
    while stack:
        postfix = postfix + stack[-1]
        stack = stack[:-1]

    return postfix



# Thompson 's construction  G00344402 Ciaran Prunty

class state:
    lalel = None
    edge1 = None
    edge2 = None 

class nfa:
    initial = None
    accept = None

    def __init__(self,initial,accept):
        self.initial = initial
        self.accept = accept

def compile(pofix):
    nfastack =[]

    for c in pofix:
        if c == '.':
            nfa2 = nfastack.pop()
            nfa1 = nfastack.pop()
            nfa1.accept.edge1 = nfa2.initial
            
            newnfa = nfa(nfa1.initial,nfa2.accept)
            nfastack.append(newnfa)
        elif c == '|':
            nfa2= nfastack.pop()
            nfa1= nfastack.pop()

            initial = state()
            initial.edge1= nfa1.initial
            initial.edge2= nfa2.initial
            
            accept = state()
            nfa1.accept.edge1 = accept
            nfa2.accept.edge2 = accept 

            newnfa = nfa(initial,accept)
            nfastack.append(newnfa)

        elif c == '*':

            nfa1 = nfastack.pop()

            initial=state()
            accept=state()
            initial.edge1=nfa1.initial
            initial.edge2 = accept

            nfa1.accept.edge1 = nfa1.initial
            nfa1.accept.edge2 = accept

            newnfa = nfa(initial, accept)
            nfastack.append(newnfa)

        else:
            accept=state()
            initial=state()

            initial.lalel = c
            initial.edge1= accept
            #pushes new nfa to the stack
            newnfa = nfa(initial, accept)
            nfastack.append(newnfa)
    return nfastack.pop()

def followes(state):
    states = set()
    states.add(state)

    if state.label is None:
        if state.edge1 is not None:
            states |= followes(state.edge1)
        if state.edge2 is not None:
            states |= followes(state.edge2)
    
    return states 

def match (infix, string):

    postfix = shunt(infix)
    nfa = compile(postfix)

    current = set()
    nexts = set()

    current |= followes(nfa.initial)
    #loop through each character in the string
    for s in string:
        #loops through current set of states 
        for c in current:
            #check is state is labelled s 
            if c.label == s:
                nexts |= followes(c.edge1)
        current = nexts
        nexts = set()

    return(nfa.accept in current)

infixes = ["a.b.c*", "(a.(b|d))*", "a.(b.b)*.c"]
strings = ["", "abc","abbc", "abad", "abbbc"]

for i in infixes:
    for s in strings:
        print(match(i ,s), i,s)

