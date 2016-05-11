# -*- coding: utf-8 -*-
import cmd
from yacc import yacc

def parse(program):
    result = yacc.parse(program)
    if result != None:
        return result

################ Environments
Symbol = str          # A Lisp Symbol is implemented as a Python str
List   = list         # A Lisp List is implemented as a Python list
Number = (int, float) # A Lisp Number is implemented as a Python int or float

def standard_env():
    "An environment with some Scheme standard procedures."
    import math, operator as op
    env = Env()
    env.update(vars(math)) # sin, cos, sqrt, pi, ...
    env.update({
        '+':       op.add,
        '-':       op.sub,
        '*':       op.mul,
        '/':       op.div,
    })
    return env

class Env(dict):
    "An environment: a dict of {'var':val} pairs, with an outer Env."
    def __init__(self, parms=(), args=(), outer=None):
        self.update(zip(parms, args))
        self.outer = outer
    def find(self, var):
        "Find the innermost Env where var appears."
        return self if (var in self) else self.outer.find(var)

global_env = standard_env()

################ Procedures

class Procedure(object):
    "A user-defined Scheme procedure."
    def __init__(self, parms, body, env):
        self.parms, self.body, self.env = parms, body, env
    def __call__(self, *args):
        return eval(self.body, Env(self.parms, args, self.env))

################ eval
toReturn = None
assignmentDict = {}
def eval(x, env=global_env):
    "Evaluate an expression in an environment."
    if isinstance(x, Symbol) and (x in env):      # variable reference
        print("LOOK UP SYMBOL:", x, "RETURN FUNCTION",env.find(x)[x])
        return env.find(x)[x]
    elif isinstance(x, Symbol) and '"' not in x:
        try:
            if x in assignmentDict.keys():
                return assignmentDict[x]
            else:
                raise Exception("use of unresolved identifier %s" % x)
        except Exception as e:
            raise e
    elif not isinstance(x, List):  # constant literal
        if isinstance(x, str):
            if x.lower() == 'false' or x == '#f':
                return False
            elif x.lower() == 'true' or x == '#t':
                return True
        return x
    elif x[0] == 'if':             # (if test conseq alt)
        (_, test, conseq, alt) = x
        exp = (conseq if eval(test, env) else alt)
        return eval(exp, env)
    elif x[0] == 'let':
        (_, var_val_list) = x
        variable = var_val_list[0]
        value = eval(var_val_list[1],env)
        if variable in assignmentDict:
            raise Exception("%s previously declared" % variable)
        else:
            assignmentDict[variable] = value
            print(assignmentDict)
    elif x[0] == 'print':
        arg = eval(x[1], env)
        print (arg)
        return(arg)
    elif x[0] == 'switch':
        identifier = eval(x[1])
        case_item_lists = x[2]
        print ('In switch, x[2] = ', case_item_lists)
        for case_item_list in case_item_lists:
            case_label = case_item_list[0]
            print ('In switch, case_label = ', case_label)
            statement = case_item_list[1]
            if identifier in case_label:
                eval(statement)
                break
            if 'default' == case_label[0]:
                eval(statement)
                break
    else:                          # (proc arg...)
        proc = eval(x[0], env)
        args = [eval(exp, env) for exp in x[1:]]
        print("PROC:", proc, "ARGS:", args)
        return proc(*args)



class MiniLisp(cmd.Cmd):     # See https://docs.python.org/2/library/cmd.html
    """
    MiniLisp evalúa expresiones sencillas con sabor a lisp,
    más información en http://www.juanjoconti.com.ar
    """

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "ml> "
        self.intro  = "Bienvenido a MiniLisp"

    def do_exit(self, args):
        """Exits from the console"""
        return -1

    def do_EOF(self, args):
        """Exit on system end of file character"""
        print "Good bye!"
        return self.do_exit(args)

    def do_help(self, args):
        print self.__doc__

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def default(self, line):
        """Called on an input line when the command prefix is not recognized.
           In that case we execute the line as Python code.
        """
        absSyntaxTree = parse(line)
        print "AST: ", absSyntaxTree
        if absSyntaxTree is not None:
            for program in absSyntaxTree:
                eval(program)

        #print "Evaluated: ", eval(absSyntaxTree)


if __name__ == '__main__':
    ml = MiniLisp()
    ml.cmdloop()     # See https://docs.python.org/2/library/cmd.html


#def parse(program):
