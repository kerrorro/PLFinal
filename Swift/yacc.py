import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from lex import tokens

DEBUG = True
# def p_program(p):
#     'program : constant-declaration switch-statement'
#     p[0] = [p[1]] + [[p[2]] + [p[4]]] + [p[5]] + [p[6]] + p[8]

# BNF

# def p_godly(p):
#     ''' godly : constant-declaration switch-statement'''
#     p[0] = [p[1],p[2]]

def p_program(p):
    '''program : switch-statement
               | constant-declaration
               | constant-declaration switch-statement
               | expression'''
    returnList = []
    for _p in p:
        if _p is not None:
            returnList.append(_p)
    p[0] = returnList

def p_switch_statement(p):
    '''switch-statement : SWITCH expression "{" switch-cases "}"'''
    if DEBUG:
        print ('In switch statement', p[1:])
    # p[0] = [p[1],p[2],p[4]]
    p[0] = p[1]

def p_expression(p):
    '''expression : numeric-literal
                  | STRING
                  | IDENTIFIER
    '''
    if DEBUG:
        print ('In expression', p[1:])
    p[0] = p[1]

def p_switch_cases(p):
    '''switch-cases : switch-case switch-cases
                    | switch-case switch-case'''
    if DEBUG:
        print ('In switch statement', p[1:])
    p[0] = [p[1]] + p[2]                                # [[['C1', 'C2'], statement], [['C1', 'C2'], statement]]]

def p_switch_case_single(p):
    'switch-cases : switch-case'
    if DEBUG:
        print ('In switch case single', p[1:])
    p[0] = p[1]

def p_switch_case(p):
    '''switch-case : CASE case-item-list ":" statement
                   | DEFAULT ":" statement '''
    if DEBUG:
        print ('In switch statement', p[1:])
    if p[1] == 'case':
        p[0] = [p[2]] + [p[4]]                               # A list that contains the case and statement
    elif p[1] == 'default':                                  # [['C1', 'C2'], statement]
        p[0] = [[p[1]]] + [p[3]]                             # [['Default'], statements]

def p_case_item_list(p):
    '''case-item-list : expression
                      | expression "," case-item-list '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = [p[1],p[3]]

def p_arithmetic(p):
    ''' statement : numeric-literal "+" numeric-literal
                    | numeric-literal "-" numeric-literal
                    | numeric-literal "*" numeric-literal
                    | numeric-literal "/" numeric-literal
    '''
    p[0] = [p[2],[p[1],p[3]]]

def p_print_function(p):
    'statement : PRINT "(" expression ")"'
    p[0] = [p[1] ,[p[2]]]

def p_constant_declaration(p):
    'constant-declaration : LET identifier-initializer'
    if DEBUG:
        print ('In constant-declaration', p[1:])
    p[0] = [p[1]] + [p[2]]

def p_identifier_initializer(p):
    'identifier-initializer : IDENTIFIER initializer'
    if DEBUG:
        print ('In identifier-initializer', p[1:])
    p[0] = [p[1]] + [p[2]]

def p_initializer(p):
    'initializer : "=" expression'
    if DEBUG:
        print ('In initializer', p[1:])
    p[0] = p[2]



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

# Error rule for syntax errors
def p_error(p):
    print "Syntax error!! ",p


# Build the parser
# Use this if you want to build the parser using SLR instead of LALR
# yacc.yacc(method="SLR")
yacc.yacc()




