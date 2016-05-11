#------------------------------------------------------------
# lex.py
#
# tokenizer
# ------------------------------------------------------------

import ply.lex as lex

DEBUG = False

# List of token names.   
tokens = ('LET', 'SWITCH', 'CASE','PRINT' , 'DEFAULT','STRING',
          'IDENTIFIER', 'QUOTEDTEXT', 'INVALIDQUOTEDTEXT' ,'INTEGER')
literals = ['=', ':', '{', '}','+',',','(',')','.','/','*','-']

# Reserved words
reserved = ['LET', 'SWITCH', 'CASE','PRINT','DEFAULT','STRING']

# Regular expression rules for simple tokens
t_INVALIDQUOTEDTEXT = r'\'.*?\''
t_QUOTEDTEXT = r'\".*?\"'
t_INTEGER = r'[0-9]+'
t_STRING = r'String'

def t_IDENTIFIER(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    # IDENTIFIER token is used for constant / variable name
    if DEBUG:
        print ('In t_IDENTIFIER',t)
    if t.value.upper() in reserved:
        # if t in reserved, it changes to the reserved token type
        t.type = t.value.upper()
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t\n'

# Error handling rule
def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

# Build the lexer
lex.lex()

if __name__ == '__main__':
    lex.runmain()