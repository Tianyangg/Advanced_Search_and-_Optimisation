from sexpdata import *
import matplotlib.pyplot as plt
import random
import io
import math
#import fire
#from pathlib import Path
import numpy as np
import csv
#import main
import sys
import numpy
import copy
import argparse
import csv




sys.setrecursionlimit(15000)

# define the function dictionary:
func = {'add', 'sub', 'mul', 'div', 'pow', 'sqrt', 'log', 'exp', 'max', 'ifleq', 'diff', 'avg', 'data'}
terminate = {'const', 'var'}

num = []
nn = 0
def parse_ev(s):
    l = loads(s)
    return evaluate(l)

def evaluate(l):
    #print(l)
    if value_type(l):
        return l

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
            return  0
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
        except ValueError:
            return 0
        except OverflowError:
            return sys.float_info.max
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
            return sys.float_info.max
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
        except ValueError:
            return 0
        except OverflowError:
            return sys.float_info.max
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

def mod(x , y):
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
        #ind = mod(a, nn)
        ind = abs(math.floor(a)) % nn
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
        k = math.floor(abs(math.floor(a)) % nn)
        l = math.floor(abs(math.floor(b)) % nn)
        temp = math.fabs(k - l)
        small = min(k, l)
        large = max(k, l)
        if temp == 0:
            return 0
        else:
            try:
                result = sum(num[small: large - 1])/temp
                return result
            except ValueError:
                return 0
            except OverflowError:
                return sys.float_info.max

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


def fitness(expr, n, m, data):
    path = data
    # read files here: replace later
    x, y = readdata(path, n)

    mse = []
    for i in range(0, m):
        predict = question1(expr, n, ' '.join(x[i]))
        try:
            se = math.pow((float(y[i]) - float(predict)), 2)
            mse = mse + [se]
        except OverflowError:
            se = numpy.inf
            mse = mse + [se]
            #se = 0.00001

    #if numpy.nan in mse:
        #print('nan here')
    # get rid of all the nan and replace that with inf
    mse = [numpy.inf if x == numpy.nan else x for x in mse]
    #print('mse',mse)
    if len(mse) == 0:
        #print('mse = 0')
        return numpy.inf
    try:
        f = sum(mse)/len(mse)
        return f
    except ValueError or OverflowError:
        return numpy.inf



def initialization(size, maxdepth, n, m, data):
    # initialize using ramp half and half
    ind = full(maxdepth)
    p = [ind]
    ftemp = fitness(dumps(ind), n, m, data)
    fi = [ftemp]
    # full method
    for i in range(1, int(2*size/3)):
        individual = full(maxdepth)
        ftemp = fitness(dumps(individual), n, m, data)
        while initialization in p or not isinstance(p, list) or ftemp in fi:
            individual = full(maxdepth)
            ftemp = fitness(dumps(individual), n, m, data)
        p = p + [individual]
        fi = fi + [ftemp]

    #print('full method done')
    # growth method
    for i in range(int(2*size/3) + 1, size):
        individual = grow(maxdepth)
        ftemp = fitness(dumps(individual),n, m, data)
        while initialization in p or not isinstance(p, list) or ftemp in fi:
            individual = grow(maxdepth)
            ftemp = fitness(dumps(individual), n, m, data)
        p = p + [individual]
        fi = fi + [ftemp]
    #print('all done')

    return p, fi

def full(maxdepth):
    if maxdepth == 0:
        #return random.randint(1, 5)
        leaf = random.choice(tuple(terminate))
        if leaf == 'var':
            return [Symbol('data'), random.randint(0, 10)]
        else:
            return random.randint(1, 5)
    else:
        node = random.choice(tuple(func)) # randomly pick a root
        if node == 'add':
            return [Symbol('add'), full(maxdepth - 1), full(maxdepth - 1)]
        if node == 'sub':
            return [Symbol('sub'), full(maxdepth - 1), full(maxdepth - 1)]
        if node == 'mul':
            return [Symbol('mul'), full(maxdepth - 1), full(maxdepth - 1)]
        if node == 'div':
            return [Symbol('div'), full(maxdepth - 1), full(maxdepth - 1)]
        if node == 'pow':
            return [Symbol('pow'), full(maxdepth - 1), full(maxdepth - 1)]
        if node == 'sqrt':
            return [Symbol('sqrt'), full(maxdepth - 1)]
        if node == 'log':
            return [Symbol('log'), full(maxdepth - 1)]
        if node == 'exp':
            return [Symbol('exp'), full(maxdepth - 1)]
        if node == 'max':
            return [Symbol('max'), full(maxdepth - 1), full(maxdepth - 1)]
        if node == 'ifleq':
            return [Symbol('ifleq'), full(maxdepth - 1), full(maxdepth - 1), full(maxdepth - 1), full(maxdepth - 1)]
        if node == 'data':
            return [Symbol('data'),  full(maxdepth - 1)]
        if node == 'diff':
            return [Symbol('diff'), full(maxdepth - 1), full(maxdepth - 1)]
        else: # 'avg'
            return [Symbol('avg'), full(maxdepth - 1), full(maxdepth - 1)]

def grow(maxdepth):
    rand = random.uniform(0, 1)
    if rand <= 0.3 or maxdepth == 0:
        if random.uniform(0, 1) < 0.5:
            return [Symbol('data'), random.randint(0, 3)]
        else:
            return random.randint(0, 5)
    else:
        node = random.choice(tuple(func))  # randomly pick a root
        if node == 'add':
            return [Symbol('add'), grow(maxdepth - 1), grow(maxdepth - 1)]
        if node == 'sub':
            return [Symbol('sub'), grow(maxdepth - 1), grow(maxdepth - 1)]
        if node == 'mul':
            return [Symbol('mul'), grow(maxdepth - 1), grow(maxdepth - 1)]
        if node == 'div':
            return [Symbol('div'), grow(maxdepth - 1), grow(maxdepth - 1)]
        if node == 'pow':
            return [Symbol('pow'), grow(maxdepth - 1), grow(maxdepth - 1)]
        if node == 'sqrt':
            return [Symbol('sqrt'), grow(maxdepth - 1)]
        if node == 'log':
            return [Symbol('log'), grow(maxdepth - 1)]
        if node == 'exp':
            return [Symbol('exp'), grow(maxdepth - 1)]
        if node == 'max':
            return [Symbol('max'), grow(maxdepth - 1), grow(maxdepth - 1)]
        if node == 'ifleq':
            return [Symbol('ifleq'), grow(maxdepth - 1), grow(maxdepth - 1), grow(maxdepth - 1), grow(maxdepth - 1)]
        if node == 'data':
            return [Symbol('data'), grow(maxdepth - 1)]
        if node == 'diff':
            return [Symbol('diff'), grow(maxdepth - 1), grow(maxdepth - 1)]
        else:  # 'avg'
            return [Symbol('avg'), grow(maxdepth - 1), grow(maxdepth - 1)]


def get_parents(pop, fit):
    # binary tounament selection
    length = len(pop) - 1

    tournament = []
    ftemp = []
    for i in range(0, 4):
        tournament.append(random.randint(0, length))
    for i in tournament:
        ftemp.append(fit[i])
    minpos = ftemp.index(min(ftemp))
    parent1 = pop[minpos]

    tournament = []
    for i in range(0, 4):
        tournament.append(random.randint(0, length))
    for i in tournament:
        ftemp.append(fit[i])
    minpos = ftemp.index(min(ftemp))
    parent2 = pop[minpos]

    if parent1 == parent2:
        tournament = []
        for i in range(0, 4):
            tournament.append(random.randint(0, length))
        for i in tournament:
            ftemp.append(fit[i])
        minpos = ftemp.index(min(ftemp))
        parent2 = pop[minpos]

    return parent1, parent2

def roulette(pop, fit):
    #if len(pop) != len(fit):
        #print('wrong')
    fit_scale = [1/x for x in fit]
    summ = sum(fit_scale)

    fit_proportion = [x/summ if x else 0 for x in fit_scale]
    # get parent1
    pick = random.uniform(0, sum(fit_proportion))
    #print(pick)
    current = 0
    for i in range(0, len(fit_proportion)):
        current = current + fit_proportion[i]
        if current >= pick:
            parent1 = pop[i]
            break
        else:
            parent1 = pop[i]
    # get parent2
    pick = random.uniform(0, sum(fit_proportion))
    current = 0
    for i in range(0, len(fit_proportion)):
        current = current + fit_proportion[i]
        if current >= pick:
            parent2 = pop[i]
            break
        else:
            parent2 = pop[i]

    while parent1 == parent2:
        pick = random.uniform(0, sum(fit_proportion))
        current = 0
        for i in range(0, len(fit_proportion)):
            current = current + fit_proportion[i]
            if current >= pick:
                parent2 = pop[i]
                break
            else:
                parent2 = pop[i]

    return parent1, parent2


# return crossover point
# input the tree and the number of nodes
def point(tree, n, index):
    randnum = random.uniform(0, 1)
    if randnum < 1/n or isinstance(tree, int) or isinstance(tree, float):
        index = index + [0]
        return tree, index
    else:
        tree_len = len(tree)
        if tree_len == 2:
            index = index + [1]
            return point(tree[1], n/2, index)
        else:
            rand = random.uniform(0, 1)
            for i in range(1, tree_len - 1):
                if rand < i * 1/n:
                    index = index + [i]
                    return point(tree[i], n/2, index)
                    #return tree[i], index
                #else:
                    #return point(tree[i], n/2, index)

            index = index + [tree_len - 1]
            return point(tree[tree_len - 1], n, index)

def cross_point(tree, n, index, probability):
    if n <= 3 or tree_depth(tree) <= 2:
        index = index + [0]
        return tree, index
    if probability < 1/n or isinstance(tree, int) or isinstance(tree, float):
        index = index + [0]
        return tree, index
    else:
        tree_len = len(tree)
        if tree_len == 2:
            index = index + [1]
            ntemp = math.pow(number_of_nodes(tree[1]), 1/2)
            #print('num: ', ntemp)
            return cross_point(tree[1], ntemp, index, probability)
        else:
            rand = random.uniform(0, 1)
            nodes = []
            for i in range (1, tree_len):
                nodes.append(number_of_nodes(tree[i]))
            overall = sum(nodes)
            proportion = [x/overall for x in nodes]
            temp = 0
            for i in range(1, tree_len):
                #print(i)
                temp = temp + proportion[i-1]
                if rand < temp:
                #if rand < i * 1/(tree_len-1):
                    index = index + [i]
                    #depth = tree_depth(tree[i])
                    #ntemp = math.pow(2, depth) - 1
                    ntemp = math.pow(number_of_nodes(tree[i]), 1/2)
                    #print('num: ', ntemp)
                    return cross_point(tree[i], ntemp , index, probability)


def replace(tree, subtree, r):
    temp = tree
    if len(r) == 1 or isinstance(temp, int) or isinstance(temp, float): # the case [0]
        return subtree
    if len(r) == 2:
        temp[r[0]] = subtree
        return tree
    else:
        for i in r:
            #print('temp: ', temp)
            if i == 0:
                temp = subtree
            else:
                temp = temp[i]
    return tree

def crossover(pop, f):
    pop_copy = copy.deepcopy(pop)
    p1, p2 = get_parents(pop_copy, f)
    p1 = mutation(p1, 0.3)
    p2 = mutation(p2, 0.3)
    offspring1 = copy.deepcopy(p1)
    # we want different parents
    #n_p1 = pow(2, tree_depth(p1) + 1) - 1
    #n_p2 = pow(2, tree_depth(p1) + 1) - 1
    n_p1 = number_of_nodes(p1)
    n_p2 = number_of_nodes(p2)

    rand1 = random.uniform(0, 1)
    (stree1, route1) = cross_point(p1, n_p1, [], rand1)
    rand2 = random.uniform(0, 1)
    (stree2, route2) = cross_point(p2, n_p2, [], rand2)

    #if isinstance(stree1, int):
        #print('leaf selected')

    while abs(tree_depth(stree1) - tree_depth(stree2)) > 3 or stree1 == stree2:
        #print('roullete')
        p1, p2 = get_parents(pop_copy, f)
        p1 = mutation(p1, 0.3)
        p2 = mutation(p2, 0.3)
        offspring1 = copy.deepcopy(p1)

        n_p1 = pow(number_of_nodes(p1), 1/1)
        n_p2 = pow(number_of_nodes(p2), 1/1)
        rand1 = random.uniform(0, 1)
        (stree1, route1) = cross_point(p1, n_p1, [], rand1)
        rand2 = random.uniform(0, 1)
        (stree2, route2) = cross_point(p2, n_p2, [], rand2)

    offspring1 = replace(offspring1, stree2, route1)
    return offspring1

def tree_depth(tree):
    if not tree:
        return 0
    if isinstance(tree, list):
        #print ('recursive', tree)
        return 1 + max(tree_depth(item) for item in tree)
    else:
        return 0

def mysorting(po, fit, p):
    #if len(po) != len(fit):
        #print('invalid length in mysorting')
    #sort based on fitness small to large!!!!!
    for i1 in range(len(fit)):
        #swap = True
        for j in range(0, len(fit) - 1):
            if math.isnan(fit[j]) or math.isinf(fit[j]):
                fit[j], fit[j + 1] = fit[j + 1], fit[j]
                po[j], po[j + 1] = po[j + 1], po[j]
            if fit[j] > fit[j + 1] or random.uniform(0, 1) < p:
                fit[j], fit[j + 1] = fit[j + 1], fit[j]
                po[j], po[j + 1] = po[j + 1], po[j]
    return po, fit


def mutation(tree, p):
    if random.uniform(0, 1) < p:
        node_number = math.pow(number_of_nodes(tree), 1/2)
        #node_number = math.pow(2, tree_depth(tree)) - 1
        rand1 = random.uniform(0, 1)
        old_sub, route = cross_point(tree, node_number, [], rand1)
        # initialize a new tree
        old_depth = tree_depth(old_sub)
        new_sub = full(old_depth)
        tree = replace(tree, new_sub, route)
        return tree
    else:
        return tree


def number_of_nodes(tree):
    if isinstance(tree, list):
        return sum(number_of_nodes(el) if isinstance(el, list) else 1 for el in tree)
    else:
        return 1

# lambda, n, m, data, time_budget
def genetic(lam, n, m, data, time_buget):
    #print('genetic')
    population, f= initialization(lam, 2, n, m, data)

    best = []

    for g in range(1, 100):
        #print('generation:', g)
        #print(len(population), len(f))

        p_operate = copy.deepcopy(population)

        for i in range (0, 50):
            o1 = crossover(p_operate, f)
            #o1 = mutation(crossover(p_operate, f), 0.5)
            f1 = fitness(dumps(o1), n, m, data)

            while tree_depth(o1) > 20 or o1 in population or f1 in f:
                #print('trapped')
                o1 = crossover(p_operate, f)
                f1 = fitness(dumps(o1), n, m, data)
            #print('individual: ', i, 'depth: ', tree_depth(o1))

            population.append(o1)
            f.append(f1)


        #print('len ', len(f) , len(population))

        new_pop, new_f = mysorting(population, f, 0.1)
        #print(f)

        population = new_pop[0:lam]
        f = new_f[0:lam]

        print('most fit rmse: ', fitness(dumps(population[0]), 5, 100, 'test5.txt'))
        print('most fit rmse: ', fitness(dumps(population[1]), 5, 100, 'test5.txt'))
        print('most fit rmse: ', fitness(dumps(population[2]), 5, 100, 'test5.txt'))
        best = best + [f[0]]

    population, f = mysorting(population, f, 0)
    return population

def testing():
    result = genetic(50, 5, 100, '/Users/tianyangsun/Documents/Uob_Y3_S2/02 Search and Optimisation/labs/08_Time_series_prediction/test5.txt', 100)
    #print(result[0])
    f = []
    for i in result:
        f = f + [fitness(dumps(i), 5, 100, '/Users/tianyangsun/Documents/Uob_Y3_S2/02 Search and Optimisation/labs/08_Time_series_prediction/test5.txt')]
    mysorting(result, f, 0)

    for i in range(0, 3):
        print('depth: ', tree_depth(result[i]))
        print(result[i])
        print(f[i])


def question1(expr, n, x):
    xnew = [float(i) for i in x.split()]
    global num
    global nn

    num = xnew
    nn = n

    r = parse_ev(expr)
    return r

# data: path to the text file
# n is the dimension of the input vector
def readdata(filepath, n):
    with open(filepath, 'r') as f1:
        X_data = [row[0:n] for row in csv.reader(f1, delimiter='\t')]
    with open(filepath, 'r') as f2:
        Y_data = [row[n] for row in csv.reader(f2, delimiter='\t')]
    return X_data, Y_data




testing()


parser = argparse.ArgumentParser()

parser.add_argument("-question", help="should given question 1,2 or 3", type=int)
#the dimension of input vector
parser.add_argument("-n", help="should input an vector size", type=int)
#the size of the trainning data
parser.add_argument("-m", help="should input an data size", type=int)
#input vector it is string not list
parser.add_argument("-x", help="should input a vector", type=str)
#should input an expression
parser.add_argument("-expr", help="should input an expression", type=str)
#input the file name
parser.add_argument("-data", help="should input an file name", type=str)
#input pop size
parser.add_argument("-lambdainput", help="should input pop size", type=int)
#the time budget
parser.add_argument("-time_budget", help="should input the time budget", type=float)

args = parser.parse_args()

if args.question==1 :
    get_vector=args.x
    get_result_1=question1(args.expr, args.n, get_vector)
    print(get_result_1)

if args.question==2:
    #get_data=readFile(args.data)
    get_result_2=fitness(args.expr, args.n, args.m, args.data)
    print (get_result_2)

#if args.question==3:
    # (pop_size,gen_pop_tree_depth,filename,m,n,time_budget,generation,mutation_rate,crossover_rate)

    #get_data=readFile(args.data)

    #get_result_3_epxr=GP(args.lambdainput,args.n,args.m,get_data,args.time_budget)
    #print (get_result_3_epxr)
    #print("time cost:",get_result_3_time,"\n \t best expression:",get_result_3_expr,"\t fitness:",get_result_3_fitness)



#test1 = "(max (sub (exp (sub (max 1.51229626953 1.71622876119) (exp -3.08529569426))) (pow (sub 0.191006438257 (sqrt -1.16461426173)) (avg 0.191006438257 (sqrt -1.10218355829)))) (ifleq (max (ifleq -0.936985333931 (sqrt 1.47757969558) -2.60300802177 (sub 3.8838508921 2.94681475796)) (sub -2.5805249348 1.34708932127)) (max (sub -2.90247306556 1.99236282422) (sub -2.54069153393 2.32701296268)) (max (sub -2.36251362023 1.24580200377) (exp (max -2.21263331848 -2.2956562051))) (mul (max -2.75120420704 3.14472767419) (sub (sqrt -1.61429976848) 2.53315506829))))"

#question1(test1, )

