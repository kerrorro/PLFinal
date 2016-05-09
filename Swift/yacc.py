import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from lex import tokens

DEBUG = False

# BNF

def p_case_item_list(p):
    'case_item_list : CASETEXT'
    p[0] = p[1].replace(" ", "").split(",")     # List ['C1', 'C2', 'C3']

def p_value(p):
    '''value : STRING
              | NUMBER'''
    p[0] = p[1]                                             # Returns value associated with an identifier/variable name: 'string' or number

def p_identifier(p):
    ''' identifier : TEXT "="
                   | SWITCH TEXT "{" '''
    if (len(p) == 3):   # Matches first grammar rule
        p[0] = p[1]
    else:
        p[0] = p[1]                                          # Texts that correspond to identifiers (variable names): 'identifier'

def p_statement(p):
    'statement : TEXT'
    p[0] = p[1]                                              # Lone text is known as a statement: 'statement'

def p_switch_case(p):
    '''switch_case : CASE case_item_list ":" statement
                   | DEFAULT ":" statement '''
    if (len(p)== 5):                                         # Matches first grammar rule
        p[0] = [p[2]] + [p[4]]                               # A list that contains the case and statement
    else:                                                    # [['C1', 'C2'], statement]
        p[0] = [[p[1]]] + [p[3]]                             # [['Default'], statements]

# def p_switch_cases(p):
#     '''switch_cases : switch_case switch_cases |
#                       switch_case '''
#     if (len(p) == 3):
#         p[0] = [p[1]] + [p[2]]
#     else:
#         p[0] = p[1]

def p_switch_cases(p):
    'switch_cases : switch_case switch_cases'
    p[0] = [p[1]] + p[2]                                # [[['C1', 'C2'], statement], [['C1', 'C2'], statement]]]

def p_switch_cases_empty(p):                            # Processing base case p_empty
    'switch_cases : empty'
    p[0] = []

def p_empty(p):                                         # Recursive base case for p_switch_cases
    'empty :'
    pass


def p_AST(p):
    'AST : LET identifier "=" value SWITCH identifier "{" switch_cases "}"'
    p[0] = [p[1]] + [[p[2]] + [p[4]]] + [p[5]] + [p[6]] + p[8]

# Error rule for syntax errors
def p_error(p):
    print "Syntax error!! ",p

# Build the parser
# Use this if you want to build the parser using SLR instead of LALR
# yacc.yacc(method="SLR")
yacc.yacc()




