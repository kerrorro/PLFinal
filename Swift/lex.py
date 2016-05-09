#------------------------------------------------------------
# lex.py
#
# tokenizer
# ------------------------------------------------------------

import ply.lex as lex

# List of token names.   
tokens = ('LET', 'SWITCH', 'CASE', 'TEXT', 'CASETEXT', 'NUMBER', 'STRING')
literals = ['=', ':', '{', '}']

# Reserved words
reserved = ['LET', 'SWITCH', 'CASE']

# Regular expression rules for simple tokens
t_LET = r'^let'
t_SWITCH = r'^switch'
t_CASE = r'case'
t_STRING = r'\'[A-Za-z0-9_]+\''

def t_NUMBER(t):
    try:
        float(t)
        return t
    except TypeError:
        pass


def t_TEXT(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    if (t.group(0) not in reserved):
        return t                        # Any string that is not a reserved word


def t_CASETEXT(t):
    r'case ([.*]+)[ ]{0,1}:'
    print "CaseText token:", t.group(1)
    return t.group(1)                   # The string between 'case' and ':' representing the variable to check for




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