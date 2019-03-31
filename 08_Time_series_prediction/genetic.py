from sexpdata import *
import matplotlib.pyplot as plt
import random
import io
import math

import numpy as np
import csv

import sys
import numpy
import copy
import argparse
import csv
import time


debug = True

sys.setrecursionlimit(15000)

# define the function dictionary:
func = {'add', 'sub', 'mul', 'div', 'pow', 'sqrt', 'log', 'exp', 'max', 'ifleq', 'diff', 'avg', 'data'}
terminate = {'const'}

num = []
nn = 0
def parse_ev(s):
    l = loads(s)
    return evaluate(l)

def value_type(a):
    if isinstance(a, int) or isinstance(a, float):
        return True
    else:
        return False


def evaluate(l):
    #print(l)
    if value_type(l):
        return l

    if l[0] == Symbol('add'):
        a = evaluate(l[1])
        b = evaluate(l[2])
        try:
            return a + b
        except ValueError:
            return 0
        except OverflowError:
            #return sys.float_info.max
            return 0

    if l[0] == Symbol('sub'):
        a = evaluate(l[1])
        b = evaluate(l[2])
        try:
            return a - b
        except ValueError:
            return 0
        except OverflowError:
            return 0

    if l[0] == Symbol('mul'):
        a = evaluate(l[1])
        b = evaluate(l[2])
        try:
            return a * b
        except ValueError:
            return 0
        except OverflowError:
            #return sys.float_info.max
            return 0
        #return mul(l[1], l[2])

    if l[0] == Symbol('div'):
        a = evaluate(l[1])
        b = evaluate(l[2])
        if b == 0:
            return 0
        else:
            try:
                return a/b
            except ValueError:
                return 0
            except OverflowError:
                #return sys.float_info.max
                return 0
        #return div(l[1], l[2])

    if l[0] == Symbol('pow'):
        a = evaluate(l[1])
        b = evaluate(l[2])
        if a == 0 and b == 0:
            return 1
        else:
            try:
                re = math.pow(a, b)
                if isinstance(re, complex):
                    return 0
                else:
                    return re
            except ValueError:
                return 0
            except OverflowError:
                #return sys.float_info.max
                return 0
        #return power(l[1], l[2])

    if l[0] == Symbol('sqrt'):
        try:
            re = math.sqrt(evaluate(l[1]))
            if isinstance(re, complex):
                return 0
            else:
                return re
        except ValueError:
            return 0
        except OverflowError:
            #return sys.float_info.max
            return 0

    if l[0] == Symbol('log'):
        try:
            return math.log(evaluate(l[1]), 2)
        except ValueError:
            return 0
        except OverflowError:
            #return sys.float_info.max
            return 0
        #return logarithm(l[1])

    if l[0] == Symbol('exp'):
        try:
            return math.exp(evaluate(l[1]))
        except ValueError:
            return 0
        except OverflowError:
            #return sys.float_info.max
            return 0
        #return myexp(l[1])

    if l[0] == Symbol('max'):
        return max(evaluate(l[1]), evaluate(l[2]))

    if l[0] == Symbol('data'):
        ind = int(abs(math.floor(evaluate(l[1]))) % nn)
        return num[ind]

    if l[0] == Symbol('ifleq'):
        if evaluate(l[1]) <= evaluate(l[2]):
            return evaluate(l[3])
        else:
            return evaluate(l[4])

    if l[0] == Symbol('diff'):
        ind1 = int(abs(math.floor(evaluate(l[1]))) % nn)
        ind2 = int(abs(math.floor(evaluate(l[2]))) % nn)
        try:
            return num[ind1] - num[ind2]
        except ValueError:
            return 0
        except OverflowError:
            #return sys.float_info.max
            return 0
        #return diff(l[1], l[2])

    if l[0] == Symbol('avg'):
        a = evaluate(l[1])
        b = evaluate(l[2])
        k = int(math.floor(abs(math.floor(a)) % nn))
        l = int(math.floor(abs(math.floor(b)) % nn))
        if k == l:
            return 0
        small = min(k, l)
        large = max(k, l)
        try:
            return sum(num[small: large])/math.fabs(k - l)
        except ValueError:
            return 0
        except OverflowError:
            #return sys.float_info.max
            return 0


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
    p = []
    fi = []
    for j in range(2, maxdepth):
        for i in range(0, int(size/2*(maxdepth - 1))):
            ran = random.uniform(0, 1)
            if ran <= 0.5:
                individual = grow(maxdepth)
                ftemp = fitness(dumps(individual),n, m, data)
                while initialization in p or not isinstance(individual, list) or ftemp in fi:
                    individual = grow(maxdepth)
                    ftemp = fitness(dumps(individual), n, m, data)
                p.append(individual)
                fi.append(ftemp)
            else:
                individual = full(maxdepth)
                ftemp = fitness(dumps(individual), n, m, data)
                while initialization in p or not isinstance(individual, list) or ftemp in fi:
                    individual = full(maxdepth)
                    ftemp = fitness(dumps(individual), n, m, data)
                p.append(individual)
                fi.append(ftemp)
    return p, fi

def full(maxdepth):
    if maxdepth == 0:
        #return random.randint(1, 5)
        leaf = random.choice(tuple(terminate))
        if leaf == 'var':
            return [Symbol('data'), random.randint(0, 10)]
        else:
            return random.randint(-5, 5)
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
    if rand <= 0.1  or maxdepth == 0:
         if random.uniform(0, 1) < 0.5:
             return [Symbol('data'), random.randint(0, 6)]
         else:
             return random.randint(-10, 10)
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


def replace(tree, subtree, r):
    temp = tree
    if len(r) <= 1 or isinstance(temp, int) or isinstance(temp, float): # the case [0]
        return subtree
    if len(r) == 2:
        temp[r[0]] = subtree
        return tree
    else:
        #nmd = r[len(r) - 1]

        for i in r:
            #print('hey', i, temp)
            if i == r[-1]:
            #   print('selected')
                temp[i] = subtree
                break
            else:
                temp = temp[i]
            #print('temp: ', temp)
            # if i == 0:
            #     temp = subtree
            # else:
            #     temp = temp[i]

    return tree


def tree_depth(tree):
    if not tree:
        return 0
    if isinstance(tree, list):
        #print ('recursive', tree)
        return 1 + max(tree_depth(item) for item in tree)
    else:
        return 0

def mysorting(po, fit, p):
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
        routes = valid_address(tree)
        r1 = select_route(routes)
        #r1 = random.choice(routes)
        old_sub = get_subtree(tree, r1)

        # initialize a new tree
        old_depth = tree_depth(old_sub)
        ctr = 0

        new_sub = grow(2)
        # while old_depth == 0 and ctr <= 10:
        #     r1 = random.choice(routes)
        #     old_sub = get_subtree(tree, r1)
        #     # initialize a new tree
        #     old_depth = tree_depth(old_sub)
        #     ctr += 1
        #
        # if old_depth >= 2:
        #     rand_depth = random.randint(1, old_depth)
        #     new_sub = grow(rand_depth)
        #     while not isinstance(new_sub, list):
        #         rand_depth = random.randint(1, old_depth)
        #         new_sub = grow(rand_depth)
        #
        # else:
        #     new_sub = full(1)
        tree = replace(tree, new_sub, r1)
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

    start_time = time.time()

    population, f= initialization(lam, 3, n, m, data)

    g = 0
    while(1):
        g += 1
        end_time = time.time()
        if (end_time - start_time) > time_buget:
            break
        else:
            p_operate = copy.deepcopy(population)
            #p_operate, f = mysorting(p_operate, f, 0.1)
            for i in range (0, 50):
                #o1 = crossover(p_operate, f)
                #o1 = mutation(crossover(p_operate, f), 0.5)
                o1, o2 = cross(p_operate, f)
                node_num1 = number_of_nodes(o1)
                node_num2 = number_of_nodes(o2)
                #f1 = fitness(dumps(o1), n, m, data)
                #f2 = fitness(dumps(o2), n, m, data)

                while node_num1 > 5 * n or node_num2 > 5 * n or o1 in population or o2 in population: # or fitness(dumps(o2), n, m, data) in f:
                    o1, o2 = cross(p_operate, f)
                    node_num1 = number_of_nodes(o1)
                    node_num2 = number_of_nodes(o2)

                    end_time = time.time()
                    if (end_time - start_time) > time_buget:
                        break

                f1 = fitness(dumps(o1), n, m, data)
                f2 = fitness(dumps(o2), n, m, data)


                population.append(o1)
                population.append(o2)
                f.append(f1)
                f.append(f2)

                end_time = time.time()
                if (end_time - start_time) > time_buget:
                    break

            new_pop, new_f = mysorting(population, f, 0.1)

            population = new_pop[0:lam]
            f = new_f[0:lam]
            print(g, '\t' , f[0:20 ])

            end_time = time.time()
            if (end_time - start_time) > time_buget:
                break
    population, f = mysorting(population, f, 0)
    return population[0]

def testing():
    fits = []
    for i in range(0, 10):
        result = genetic(100, 5, 100, '/Users/tianyangsun/Documents/Uob_Y3_S2/02 Search and Optimisation/labs/08_Time_series_prediction/test4.txt', 60)
        f = fitness(dumps(result), 5, 100, '/Users/tianyangsun/Documents/Uob_Y3_S2/02 Search and Optimisation/labs/08_Time_series_prediction/test4.txt')
        fits.append(f)
    print(fits)


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

def valid_address(tree):
    if not isinstance(tree, list):
        return [[]]
    else:
        if len(tree) == 2:
            return [[]] + [[1]+x for x in valid_address(tree[1])] # + [x for x in valid_address(tree[1])]
        if len(tree) == 3:
            x1 = [[]]+ [[1]+x for x in valid_address(tree[1])] # + [x for x in valid_address(tree[1])]
            x2 = [[2]+x for x in valid_address(tree[2])] # + [x for x in valid_address(tree[2])]
            return x1 + x2
        if len(tree) == 5:
            return [[]]+ [[1]+x for x in valid_address(tree[1])] \
                   + [[2]+ x for x in valid_address(tree[2])] \
                   + [[3]+ x for x in valid_address(tree[3])] \
                   + [[4]+ x for x in valid_address(tree[4])]


def get_subtree(tree, route):
    if not route:
        return tree
    else:
        return get_subtree(tree[route[0]], route[1:])

def select_route(l):
    if not l:
        return []
    else:
        f_l = [1/(len(x) + 1) if x else 1/100 for x in l]
        s = sum(f_l)
        if s == 0: return []
        else:
            new_fl = [x/s for x in f_l]
            current = 0
            pick = random.uniform(0, 1)
            for i in range(0, len(new_fl)):
                current = current + new_fl[i]
                if pick < current:
                    return l[i]
            return l[len(l)-1]

def cross(pop, f):
    p1, p2 = get_parents(pop, f)
    copy_1 = copy.deepcopy(p1)
    copy_2 = copy.deepcopy(p2)

    # get all possible routes for p1 and p2, select one of them and the pick one
    routes1 = valid_address(copy_1)
    routes1.sort(key = lambda s: len(s))
    r1 = select_route(routes1)
    sub1 = copy.deepcopy(get_subtree(copy_1, r1))


    routes2 = valid_address(copy_2)
    routes2.sort(key=lambda s: len(s))
    r2 = select_route(routes2)
    sub2 = copy.deepcopy(get_subtree(copy_2, r2))


    offspring1 = replace(copy_1, sub2, r1)
    offspring2 = replace(copy_2, sub1, r2)

    offspring1 = mutation(offspring1, 0.5)
    offspring2 = mutation(offspring2, 0.5)

    return offspring1, offspring2



testing()


parser = argparse.ArgumentParser()

parser.add_argument("-question", help="questionnum", type=int)
#the dimension of input vector
parser.add_argument("-n", help="length of n", type=int)
#the size of the trainning data
parser.add_argument("-m", help="size of data", type=int)
#input vector it is string not list
parser.add_argument("-x", help="vector", type=str)
#should input an expression
parser.add_argument("-expr", help="expression", type=str)
#input the file name
parser.add_argument("-data", help="file name", type=str)
#input pop size
parser.add_argument("-lambdainput", help="should input pop size", type=int)
#the time budget
parser.add_argument("-time_budget", help="should input the time budget", type=float)

args = parser.parse_args()

if args.question==1 :
    get_vector=args.x
    get_result_1 = question1(args.expr, args.n, get_vector)
    print(get_result_1)

if args.question==2:
    #get_data=readFile(args.data)
    get_result_2 = fitness(args.expr, args.n, args.m, args.data)
    print (get_result_2)

if args.question==3:
    get_result_3_epxr = genetic(args.lambdainput, args.n, args.m, args.data, args.time_budget)
    print (dumps(get_result_3_epxr))
    #print("time cost:",get_result_3_time,"\n \t best expression:",get_result_3_expr,"\t fitness:",get_result_3_fitness)

