import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from lex import tokens

DEBUG = False

# Namespace & built-in functions

name = {}

def _if(l):
    if l[0] == True:
        return l[1]
    else:
        return l[2]

name['if'] = _if

def let(l):
    # Is a list such that if index i is even it's a key (variable name) ,
    # if index i is odd it's a value
    # example: [var1, val1, var2, val2]
    kv_list = l[0]
    if len(l) > 1:
        let_dict = {}
        for i in range(0,len(kv_list),2):
            let_dict[kv_list[i]] = kv_list[i+1]

        f_list_tuple = l[-1]

        if not type(f_list_tuple) == type([]):
            return l[-1]

        f = f_list_tuple[0]
        list = f_list_tuple[1]

        for i in range(0,len(list)):
            if list[i] in let_dict:
                list[i] = let_dict[list[i]]
        try:
            return f(list)
        except TypeError:
            return [f] + [list]
    else:
        return kv_list[1]

name['let'] = let

def cons(l):
    return [l[0]] + l[1]

name['cons'] = cons

def concat(l):
    return l[0] + l[1]

name['concat'] = concat

def listar(l):
    return l

name['list'] = listar

def car(l):
    return l[0][0]

name['car'] = car

def cdr(l):
    return l[0][1:]

name['cdr'] = cdr

def eq(l):
    return l[0] == l[1]

name['eq'] = eq
name['='] = eq

def _and(l):
    return not False in l

name['and'] = _and

def _or(l):
    return True in l

name['or'] = _or

def cond(l):
    if l[0]:
        return l[1 ]

name['cond'] = cond

def add(l):
    return sum(l)

name['+'] = add

def minus(l):
    if len(l) == 0:
        return 0
    elif len(l) == 1:
        '''Unary minus'''
        return -l[0]
    else:
        return l[0] - sum(l[1:])

name['-'] = minus

def multiply(l):
    if len(l) == 0:
        return 1
    elif len(l) == 1:
        return l[0]
    else:
        result = 1
        for num in l:
            result *= num
        return result

name['*'] = multiply

def divide(l):
    try:
        if len(l) == 0:
            raise Exception("Need at least 1 argument for dividing.")
        # Returns reciprocal of argument if only one present
        elif len(l) == 1:
            if "-" in str(l[0]):
                return "-1/" + str(-l[0])
            else:
                return "1/" + str(l[0])
        else:
            if 0 in l[2:]:
                raise Exception("Cannot divide by 0.")
            else:
                result = l[0]
                if ("-" in str(l[0])):
                    negDividend = True
                else:
                    negDividend = False
                for i in range(1, len(l)):
                    if ("-" in str(l[i])):
                        negDivisor = True
                    else:
                        negDivisor = False
                    # Don't have to correct for flooring of int div for python in these cases:
                    # 1) Dividend divides divisor perfectly
                    # 2) Dividend and divisor are both + or - --> + quotient
                    if (l[0] % l[i] == 0) or (negDividend and negDivisor) or (not negDividend and not negDivisor):
                        result //= l[i]
                    else:
                        result //= l[i]
                        # Corrects for python flooring negative int div, where lisp rounds towards 0
                        result += 1

                return result
    except Exception as e:
        print(e)

name['/'] = divide

def _print(l):
    print lisp_str(l[0])

name['print'] = _print

#  Evaluation functions

def lisp_eval(simb, items):
    if simb in name:
        return call(name[simb], eval_lists(items))
    else:
       return [simb] + items

def call(f, l):
    try:
        return f(eval_lists(l))  
    except TypeError:
        return [f] + [eval_lists(l)]

def eval_lists(l):
    r = []
    for i in l:
        if is_list(i):
            if i:
                r.append(lisp_eval(i[0], i[1:]))
            else:
                r.append(i)
        else:
            r.append(i)
    return r

# Utilities functions

def is_list(l):
    return type(l) == type([])

def lisp_str(l):
    if type(l) == type([]):
        if not l:
            return "()"
        r = "("
        for i in l[:-1]:
            r += lisp_str(i) + " "
        r += lisp_str(l[-1]) + ")"
        return r
    elif l is True:
        return "#t"
    elif l is False:
        return "#f"
    elif l is None:
        return 'nil'
    else:
        return str(l)

# BNF

def p_exp_atom(p):
    'exp : atom'
    p[0] = p[1]

def p_exp_qlist(p):
    'exp : quoted_list'
    p[0] = p[1]

def p_exp_call(p):
    'exp : call'
    p[0] = p[1]

def p_quoted_list(p):
    'quoted_list : QUOTE list'
    p[0] = [p[1]] + p[2]

def p_list(p):
    'list : LPAREN items RPAREN'
    p[0] = p[2]

def p_items(p):
    'items : item items'
    p[0] = [p[1]] + p[2]

def p_items_empty(p):
    'items : empty'
    p[0] = []

def p_empty(p):
    'empty :'
    pass

def p_item_atom(p):
    'item : atom'
    p[0] = p[1]

def p_item_list(p):
    'item : list'
    p[0] = p[1]

def p_item_list(p):
    'item : quoted_list'
    p[0] = p[1]

def p_item_call(p):
    'item : call'
    p[0] = p[1]

def p_item_empty(p):
    'item : empty'
    p[0] = p[1]

def p_call(p):
    'call : LPAREN SIMB items RPAREN'
    if DEBUG: print "Calling", p[2], "with", p[3]
    #p[0] = (lisp_eval(p[2], p[3]) if call == "default" else [p[2]] + p[3])
    p[0] = [p[2]] + p[3]


def p_atom_simbol(p):
    'atom : SIMB'
    p[0] = p[1]

def p_atom_bool(p):
    'atom : bool'
    p[0] = p[1]

def p_atom_num(p):
    'atom : NUM'
    p[0] = p[1]

def p_atom_word(p):
    'atom : TEXT'
    p[0] = p[1]

def p_atom_empty(p):
    'atom :'
    pass

def p_bool(p):
   '''bool : TRUE
           | FALSE'''
   p[0] = p[1]

# def p_true(p):
#     'bool : TRUE'
#     p[0] = True
#
# def p_false(p):
#     'bool : FALSE'
#     p[0] = False

def p_nil(p):
    'atom : NIL'
    p[0] = None

# Error rule for syntax errors
def p_error(p):
    print "Syntax error!! ",p

# Build the parser
# Use this if you want to build the parser using SLR instead of LALR
# yacc.yacc(method="SLR")
yacc.yacc()




