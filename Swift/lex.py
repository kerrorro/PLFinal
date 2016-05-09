#------------------------------------------------------------
# lex.py
#
# tokenizer
# ------------------------------------------------------------

import ply.lex as lex

# List of token names.   
tokens = ('LET', 'SWITCH', 'CASE', 'IDENTIFIER', 'CASETEXT', 'STRING','DEFAULT','INTEGER')
literals = ['=', ':', '{', '}']

# Reserved words
reserved = ['LET', 'SWITCH', 'CASE']

# Regular expression rules for simple tokens
t_LET = r'let'
t_SWITCH = r'^switch'
t_CASE = r'case'
t_DEFAULT = r'default'
t_STRING = r'\"[A-Za-z0-9_]*\"'
t_INTEGER = r'[0-9]+'

def t_IDENTIFIER(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    if t.value.upper() in reserved:
        t.type = t.value.upper()                    # Any string that is not a reserved word
    return t

def t_CASETEXT(t):
    r'case ([.*]+)[ ]{0,1}:'
    print "CaseText token:", t.value.group(1)
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