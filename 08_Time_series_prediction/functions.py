from sexpdata import *

import io
import math
import fire
from pathlib import Path
import numpy as np
import csv

num = []
nn = 0
def parse_ev(s):
    l = loads(s)
    return evaluate(l)

def evaluate(l):
    ## print(l)
    if l[0] == Symbol('add'):
        return add(l[1], l[2])

    if l[0] == Symbol('sub'):
        return sub(l[1], l[2])

    if l[0] == Symbol('mul'):
        return mul(l[1], l[2])

    if l[0] == Symbol('div'):
        return div(l[1], l[2])

    if l[0] == Symbol('pow'):
        return power(l[1], l[2])

    if l[0] == Symbol('sqrt'):
        return mysq(l[1])

    if l[0] == Symbol('log'):
        return logarithm(l[1])

    if l[0] == Symbol('exp'):
        return myexp(l[1])

    if l[0] == Symbol('max'):
        return mymax(l[1], l[2])

    if l[0] == Symbol('data'):
        return dat(l[1])

    if l[0] == Symbol('ifleq'):
        return ifleq(l[1], l[2], l[3], l[4])

    if l[0] == Symbol('diff'):
        return diff(l[1], l[2])

    if l[0] == Symbol('avg'):
        return avg(l[1], l[2])



def mymax(a, b):
    if value_type(a) and value_type(b):
        return max(a, b)
    if not value_type(a) and value_type(b):
        return mymax(evaluate(a), b)
    if value_type(a) and not value_type(b):
        return mymax(a, evaluate(b))
    else:
        return mymax(evaluate(a), evaluate(b))

def myexp(a):
    if value_type(a):
        return math.exp(a)
    else:
        return myexp(evaluate(a))

def logarithm(a):
    if value_type(a):
        #print(a)
        r = math.log(a, 2)
        return r
    else:
        r = evaluate(a, 2)
        return r

def mysq(a):
    if value_type(a):
        r = math.sqrt(a)
        return r
    else:
        r = evaluate(a)
        return r

def power(a, b):
    if value_type(a) and value_type(b):
        return a ** b
    if not value_type(a) and value_type(b):
        r = evaluate(a)
        return r ** b
    if value_type(a) and not value_type(b):
        r = evaluate(b)
        return  a ** r
    else:
        r1 = evaluate(a)
        r2 = evaluate(b)
        return r1 ** r2

def div(a, b):
    if value_type(a) and value_type(b):
        if b == 0:
            return 0
        else:
            return a/b
    if not value_type(a) and value_type(b):
        if b == 0:
            return 0
        else:
            r = evaluate(a)
            return div(r, b)
    if value_type(a) and not value_type(b):
        r = evaluate(b)
        return  div(a, r)
    else:
        return div(evaluate(a), evaluate(b))

def sub(a, b):
    if value_type(a) and value_type(b):
        return a - b
    if not value_type(a) and value_type(b):
        return sub(evaluate(a), b)
    if value_type(a) and not value_type(b):
        return  sub(a, evaluate(b))
    else:
        return sub(evaluate(a), evaluate(b))

def add(a, b):
    if value_type(a) and value_type(b):
        return a + b
    if not value_type(a) and value_type(b):
        return add(evaluate(a), b)
    if value_type(a) and not value_type(b):
        return  add(a, evaluate(b))
    else:
        return add(evaluate(a), evaluate(b))

def mul(a, b):
    if value_type(a) and value_type(b):
        return a * b
    if not value_type(a) and value_type(b):
        return mul(evaluate(a), b)
    if value_type(a) and not value_type(b):
        return  mul(a, evaluate(b))
    else:
        return mul(evaluate(a),  evaluate(b))

def ifleq(a, b, c, d):
    if mymax(evaluate(a), evaluate(b)) == evaluate(b): # if a < b
        return evaluate(c)
    else:
        return evaluate(d)

def mod(x , y): #qu yu
    return int(divmod(x, y)[1])

def dat(a):
    if value_type(a):
        ind = mod(a, nn)
        return num[ind]
    else:
        return dat(evaluate(a))
def diff(a, b):
    if value_type(a) and value_type(b):
        return sub(dat(a), dat(b))
    if not value_type(a) and value_type(b):
        return diff(evaluate(a), b)
    if value_type(a) and not value_type(b):
        return diff(a, evaluate(b))
    else:
        return diff(evaluate(a),  evaluate(b))

def avg(a, b):
    if value_type(a) and value_type(b):
        k = mod(a, nn)
        l = mod(b, nn)
        temp = math.fabs(k - l)
        small = min(k, l)
        large = max(k, l)
        if small == large:
            return num[dat(k)-1]
        else:
            return div(sum(num[small: large - 1]), temp)

    if not value_type(a) and value_type(b):
        return avg(evaluate(a), b)
    if value_type(a) and not value_type(b):
        return avg(a, evaluate(b))
    else:
        return avg(evaluate(a),  evaluate(b))



def value_type(a):
    if isinstance(a, int) or isinstance(a, float):
        return True
    else:
        return False



