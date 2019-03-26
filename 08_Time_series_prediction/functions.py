from sexpdata import *

import io
import math
import fire
from pathlib import Path
import numpy as np
import csv
import numpy
num = []
nn = 0

def parse_ev(s):
    l = loads(s)
    return evaluate(l)

def evaluate(l):
    #print(l)
    if value_type(l):
        return l
    if not isinstance(l, list):
        print(l)
    if l[0] == Symbol('add'):
        return add(l[1], l[2])

    if l[0] == Symbol('sub'):
        return sub(l[1], l[2])

    if l[0] == Symbol('mul'):
        return mul(l[1], l[2])

    if l[0] == Symbol('div'):
        #print('div', div(l[1], l[2]))
        return div(l[1], l[2])

    if l[0] == Symbol('pow'):
        #print('pow', power(l[1], l[2]))
        return power(l[1], l[2])

    if l[0] == Symbol('sqrt'):
        return mysq(l[1])

    if l[0] == Symbol('log'):
        #print('log', logarithm(l[1]))
        return logarithm(l[1])

    if l[0] == Symbol('exp'):
        #print('exp', myexp(l[1]))
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
        try:
            return  math.exp(a)
        except OverflowError:
            return  numpy.inf
    else:
        try:
            return myexp(evaluate(a))
        except OverflowError:
            return  0


def logarithm(a):
    if value_type(a):
        if a > 0:
            r = math.log(a, 2)
            return r
        else:
            return 0
    else:
        r = evaluate(a)
        return r

def mysq(a):
    if value_type(a):
        if a > 0:
            try:
                r = math.sqrt(a)
                return r
            except ValueError:
                return 0
            except OverflowError:
                return numpy.inf
        else:
            return 0
    else:
        r = mysq(evaluate(a))
        return r

def power(a, b):
    if value_type(a) and value_type(b):
        #return a ** b
        if a == 0:
            return 0
        else:
            try:
                re = a ** b
                if not isinstance(re, complex):
                    return re
                else:
                    return 0
            except OverflowError or ValueError:
                return 0
            except ValueError:
                return 0
    if not value_type(a) and value_type(b):
        r = evaluate(a)
        if r == 0:
            return 0
        else:
            try:
                re = r ** b
                if not isinstance(re, complex):
                    return re
                else:
                    return 0
            except OverflowError or ValueError:
                return 0
            except ValueError:
                return 0
    if value_type(a) and not value_type(b):
        r = evaluate(b)
        if a == 0:
            return 0
        else:
            try:
                re = a ** r
                if not isinstance(re, complex):
                    return re
                else:
                    return 0
            except OverflowError or ValueError:
                return 0
            except ValueError:
                return 0

    else:
        r1 = evaluate(a)
        r2 = evaluate(b)
        if r1 == 0:
            return 0
        else:
            try:
                re = r1 ** r2
                if not isinstance(re, complex):
                    return re
                else:
                    return 0
                #return r1 ** r2
            except OverflowError or ValueError:
                return 0
            except ValueError:
                return 0

def div(a, b):
    if value_type(a) and value_type(b):
        if b == 0:
            return 0
        else:
            try:
                return a/b
            except OverflowError:
                return 0
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
        try:
            return a - b
        except OverflowError:
            return 0
    if not value_type(a) and value_type(b):
        return sub(evaluate(a), b)
    if value_type(a) and not value_type(b):
        return  sub(a, evaluate(b))
    else:
        return sub(evaluate(a), evaluate(b))

def add(a, b):
    if value_type(a) and value_type(b):
        try:
            return a + b
        except ValueError:
            return 0
        except OverflowError:
            return 0
        except Exception as error:
            print(error)
            return 0
    if not value_type(a) and value_type(b):
        return add(evaluate(a), b)
    if value_type(a) and not value_type(b):
        return  add(a, evaluate(b))
    else:
        return add(evaluate(a), evaluate(b))

def mul(a, b):
    if value_type(a) and value_type(b):
        try:
            return a * b
        except OverflowError:
            return 0
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
    if int(y) == 0:
        return 0
    else:
        try:
            if math.isnan(x) or math.isnan(y):
                return 0
            result = divmod(int(x), int(y))[1]
            return result
        except OverflowError or ValueError:
            return 0
def dat(a):
    if value_type(a):
        ind = mod(a, nn)
        return num[ind]
    else:
        return int(dat(evaluate(a)))
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
        if temp == 0:
            return 0
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




