import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from lex import tokens

DEBUG = True

def p_program(p):
    'program : constant-declaration SWITCH identifier "{" switch_cases "}"'
    p[0] = [p[1]] + [[p[2]] + [p[4]]] + [p[5]] + [p[6]] + p[8]

# BNF
def p_constant_declaration(p):
    '''constant-declaration : LET pattern-initializer'''
    if DEBUG:
        print ('In constant_declaration', p[1:])
    p[0] = [p[1]] + [p[2]]

def p_pattern_initializer(p):
    '''pattern-initializer : IDENTIFIER initializer'''
    if DEBUG:
        print ('In pattern-initializer', p[1:])
    p[0] = [p[1]] + [p[2]]

def p_initializer(p):
    '''initializer : "=" expression'''
    if DEBUG:
        print ('In initializer', p[1:])
    p[0] = p[2]

def p_expression(p):
    '''expression : numeric-literal
                  | STRING
    '''
    if DEBUG:
        print ('In expression', p[1:])
    p[0] = p[1]

def p_numeric_literal(p):
    '''numeric-literal : INTEGER
                       | floating-point-literal
    '''
    if DEBUG:
        print ('In numeric literal', p[1:])
    p[0] = p[1]


def p_floating_point_literal(p):
    '''floating-point-literal : INTEGER "." INTEGER'''
    if DEBUG:
        print ('In floating_point_literal', p[1:])
    # p[0] = str(p[1]) + p[2] + str(p[3])

def p_identifier(p):
    ''' identifier : TEXT "="
                   | SWITCH TEXT "{" '''
    if (len(p) == 3):   # Matches first grammar rule
        p[0] = p[1]
    else:
        p[0] = p[1]                                          # Texts that correspond to identifiers (variable names): 'identifier'

def p_value(p):
    '''value : STRING
              | NUMBER'''
    p[0] = p[1]                                             # Returns value associated with an identifier/variable name: 'string' or number

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


def p_case_item_list(p):
    'case_item_list : CASETEXT'
    p[0] = p[1].replace(" ", "").split(",")     # List ['C1', 'C2', 'C3']


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

def p_switch_cases_empty(p):                            # Processing base case p_empty
    'switch_cases : empty'
    p[0] = []

def p_empty(p):                                         # Recursive base case for p_switch_cases
    'empty :'
    pass

# Error rule for syntax errors
def p_error(p):
    print "Syntax error!! ",p

# Build the parser
# Use this if you want to build the parser using SLR instead of LALR
# yacc.yacc(method="SLR")
yacc.yacc()




