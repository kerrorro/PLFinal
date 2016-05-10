import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from lex import tokens

DEBUG = True

# def p_program(p):
#     'program : constant-declaration SWITCH identifier "{" switch_cases "}"'
#     p[0] = [p[1]] + [[p[2]] + [p[4]]] + [p[5]] + [p[6]] + p[8]

# BNF
def p_constant_declaration(p):
    '''constant-declaration : LET identifier-initializer'''
    if DEBUG:
        print ('In constant_declaration', p[1:])
    p[0] = [p[1]] + [p[2]]

def p_identifier_initializer(p):
    '''identifier-initializer : IDENTIFIER initializer'''
    if DEBUG:
        print ('In identifier-initializer', p[1:])
    p[0] = [p[1]] + [p[2]]

def p_initializer(p):
    '''initializer : "=" expression'''
    if DEBUG:
        print ('In initializer', p[1:])
    p[0] = p[2]

def p_expression(p):
    '''expression : numeric-literal
                  | STRING
                  | IDENTIFIER
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

#
# def p_identifier(p):
#     ''' identifier : TEXT "="
#                    | SWITCH TEXT "{" '''
#     if (len(p) == 3):   # Matches first grammar rule
#         p[0] = p[1]
#     else:
#         p[0] = p[1]                                          # Texts that correspond to identifiers (variable names): 'identifier'

# def p_switch_cases(p):
#     '''switch_cases : switch_case switch_cases |
#                       switch_case '''
#     if (len(p) == 3):
#         p[0] = [p[1]] + [p[2]]
#     else:
#         p[0] = p[1]

def p_switch_statement(p):
    '''switch-statement : SWITCH expression "{" switch-cases "}"'''
    p[0] = [p[1],p[2],p[4]]

# TODO Kerro's idea for defining switch_cases this way might work
def p_switch_cases(p):
    '''switch-cases : switch-case switch-cases
                    | switch-case switch-case'''
    p[0] = [p[1]] + p[2]                                # [[['C1', 'C2'], statement], [['C1', 'C2'], statement]]]

def p_switch_case_single(p):
    '''switch-cases : switch-case'''
    p[0] = p[1]

def p_switch_case(p):
    '''switch-case : CASE case-item-list ":" statement
                   | DEFAULT ":" statement '''
    if p[1] == 'case':
        p[0] = [p[2]] + [p[4]]                               # A list that contains the case and statement
    elif p[1] == 'default':                                  # [['C1', 'C2'], statement]
        p[0] = [[p[1]]] + [p[3]]                             # [['Default'], statements]

# TODO I think this is not going to work since we cannot guarantee whether after switch-case is empty
# def p_switch_cases_empty(p):                            # Processing base case p_empty
#     'switch-cases : empty'
#     p[0] = []
#
# def p_empty(p):                                         # Recursive base case for p_switch_cases
#     'empty :'
#     pass

def p_case_item_list(p):
    'case-item-list : CASETEXT'
    p[0] = p[1].replace(" ", "").split(",")     # List ['C1', 'C2', 'C3']

# def case_label(p):
#     '''CASE case-itemlist ":"'''
#     p[0] = p[1].replace(" ","").split(",")
#
# def p_case_item_list(p):
#     'case-item-list : expression | expression "," case-item-list'
#

def p_arithmetic(p):
    ''' statement : numeric-literal "+" numeric-literal
                    | numeric-literal "-" numeric-literal
                    | numeric-literal "*" numeric-literal
                    | numeric-literal "/" numeric-literal
    '''
    p[0] = [p[2],[p[1],p[3]]]

def p_print_function(p):
    ''' statement : PRINT "(" expression ")"
    '''
    p[0] = [p[1] ,[p[2]]]
#
# Error rule for syntax errors
def p_error(p):
    print "Syntax error!! ",p

# Build the parser
# Use this if you want to build the parser using SLR instead of LALR
# yacc.yacc(method="SLR")
yacc.yacc()




