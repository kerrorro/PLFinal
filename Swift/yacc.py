import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from lex import tokens

DEBUG = True

def p_programs(p):
    ''' programs : program programs
                 | program
    '''
    if DEBUG:
        print('In programs', p[1] + p[2])
    p[0] = p[1] + p[2]

def p_programs_base_case(p):
    ''' programs : program
    '''
    if DEBUG:
        print('In programs_base_case,',[p[1]])
    p[0] = [p[1]]

def p_program(p):
    '''program : switch-statement
               | constant-declaration
               | expression
               | statement
    '''
    if DEBUG:
        print('In program', p[1])
    p[0] = p[1]                           #

def p_switch_statement(p):
    '''switch-statement : SWITCH expression "{" switch-cases default "}"'''
    if DEBUG:
        print ('In switch statement', [p[1],p[2],p[4]])
    p[0] = [p[1],p[2],p[4]]

def p_switch_cases(p):
    '''switch-cases : switch-case switch-cases
    '''
    if DEBUG:
        print ('In switch-cases', [p[1]] + p[2])
    p[0] = [p[1]] + p[2]

def p_switch_cases_base_case(p):
    'switch-cases : switch-case'
    if DEBUG:
        print ('In switch-cases-end', [p[1]])
    p[0] = [p[1]]

def p_default(p):
    'default : DEFAULT ":" statement'
    if DEBUG:
        print('In default:', [[p[1]]] + p[3])
    p[0] = [[p[1]]] + p[3]                                   # [['Default'], statements]

def p_switch_case(p):
    '''switch-case : CASE case-item-list ":" statement
    '''
    if DEBUG:
        print ('In switch statement', [p[2]] + [p[4]])
    if p[1] == 'case':                                      # A list that contains the case and statement
        p[0] = [p[2]] + [p[4]]                              # [['C1', 'C2'], statement]



def p_case_item_list(p):
    '''case-item-list : expression
                      | expression "," case-item-list '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1],p[3]]

def p_arithmetic(p):
    ''' statement : numeric-literal "+" numeric-literal
                    | numeric-literal "-" numeric-literal
                    | numeric-literal "*" numeric-literal
                    | numeric-literal "/" numeric-literal
    '''
    p[0] = [p[2],[p[1],p[3]]]

# TODO it wil have a bug in this switch x { case 5: print("Hello") case 6: print("World!") }
def p_print_function(p):
    'statement : PRINT "(" expression ")"'
    p[0] = [p[1] ,p[3]]

def p_constant_declaration(p):
    'constant-declaration : LET identifier-initializer'
    if DEBUG:
        print ('In constant-declaration', [p[1], p[2]])
    p[0] = [p[1], p[2]]

def p_identifier_initializer(p):
    'identifier-initializer : IDENTIFIER initializer'
    if DEBUG:
        print ('In identifier-initializer', p[1:])
    p[0] = [p[1]] + [p[2]]                          # [IDENTIFIER , initializer]

def p_initializer(p):
    'initializer : "=" expression'
    if DEBUG:
        print ('In initializer', p[1:])
    p[0] = p[2]                                     # expression

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
    p[0] = float(str(p[1]) + p[2] + str(p[3]))

# Error rule for syntax errors
def p_error(p):
    print "Syntax error!! ",p


# Build the parser
# Use this if you want to build the parser using SLR instead of LALR
# yacc.yacc(method="SLR")
yacc.yacc()




