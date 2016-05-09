#------------------------------------------------------------
# lex.py
#
# tokenizer
# ------------------------------------------------------------

import ply.lex as lex

# List of token names.   
tokens = ('LET', 'SWITCH', 'VARIABLE', 'VALUE', 'CASE', 'STATEMENT', )
literals = ['=', ':', '{', '}']

# Reserved words
reserved = {
    'nil' : 'NIL',
}

# Regular expression rules for simple tokens
t_LET = r'^let'
t_SWITCH = r'^switch'
t_CASE = r'case'
t_STATEMENT = r''

(switch)([.*]+)

def t_VARIABLE(t):
    r'^switch ([.*]+) {'
    print "Condition token:", t.group(1)
    return t.group(1)

def t_CASETEXT(t):
    r'case ([.*]+)[ ]{0,1}:'
    print "CaseText token:", t.group(1)
    return t.group(1)




# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

# Build the lexer
lex.lex()

if __name__ == '__main__':
    lex.runmain()



def p_exp_atom(p):
    'exp : atom'
    p[0] = p[1]

