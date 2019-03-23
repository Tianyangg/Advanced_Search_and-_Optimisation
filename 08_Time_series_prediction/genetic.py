from sexpdata import *

import random
import io
import math
import fire
from pathlib import Path
import numpy as np
import csv
import main
import sys

sys.setrecursionlimit(15000)

# define the function dictionary:
func = {'add', 'sub', 'mul', 'div', 'pow', 'sqrt', 'log', 'exp', 'max', 'ifleq', 'data', 'diff', 'avg'}
terminate = {'var', 'const'}

# select a random subtree
# crossover
# mutation
# raw_fitness
# penalty
# parameter: initial population, max_inital_depth(idepth)

# return the fitness  value of a given expresssioon
def fitness(expr, n, m, data):
    path = '/Users/tianyangsun/Documents/Uob_Y3_S2/02 Search and Optimisation/labs/08_Time_series_prediction/' + data
    # read files here: replace later
    x, y = main.readdata(path, n)

    mse = []
    for i in range(0, m):
        m = main.niso_lab3(1, n, ' '.join(x[i]), expr)
        try:
            m = math.pow((float(y[i]) - float(m)), 2)
        except OverflowError:
            m = 0.001
        mse = mse + [m]

    #mse = [math.pow((y[i] - main.niso_lab3(1, n, ' '.join(x[i]), expr)), 2) for i in range(0, len(y))]

    f = sum(mse)/m
    return f

def initialization(size, maxdepth):
    p = [full(maxdepth)]
    for i in range(1, size):
        individual = full(maxdepth)
        while initialization in p:
            individual = full(maxdepth)
        p = p + [individual]
    return [full(maxdepth) for i in range (0, size)]

def full(maxdepth):
    if maxdepth == 0:
        leaf = random.choice(tuple(terminate))
        if leaf == 'var':
            return [Symbol('data'), random.randint(0, 8)]
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

def get_parents(pop):
    p = 0.4 # the parameter should it be in the function
    rand = random.uniform(0, 1)
    for i in range(0, len(pop)):
        if rand <  p * math.pow((1 - p), i):
            return pop[i]
    return pop[len(pop) - 1]


# return the number of nodes, used in mutation
def number_of_nodes(tree):
    return sum(number_of_nodes(tree) if isinstance(el, list) else 1 for el in tree)

# return crossover point
# input the tree and the number of nodes
def point(tree, n, index):
    if len(tree) == 2 and isinstance(tree[1], int):
        index = index + [0]
        return tree, index
    if len(tree) == 3 and (isinstance(tree[1], int) or isinstance(tree[2], int)):
        index = index + [0]
        return tree, index
    if len(tree) == 5 and (
            isinstance(tree[1], int) or isinstance(tree[2], int) or isinstance(tree[3], int) or isinstance(tree[4],
                                                                                                           int)):
        index = index + [0]
        return tree, index
    else:
        if random.uniform(0, 1) < 1/n:
            index = index + [0]
            return tree, index
        else:
            tree_len = len(tree)

            if tree_len == 2:
                index = index + [1]
                return point(tree[1], n, index)
            else:
                rand = random.uniform(0, 1)
                for i in range(1, tree_len - 1):
                    if rand < i * 1/tree_len:
                        index = index + [i]
                        return point(tree[i], n, index)
                index = index + [tree_len - 1]
                return point(tree[tree_len - 1], n, index)

def replace(tree, subtree, r):
    temp = tree
    if len(r) == 1: # the case [0]
        return subtree
    if len(r) == 2:
        temp[r[0]] = subtree
        return tree
    else:
        for i in r:
            temp = temp[i]
    return tree


def crossover(pop):
    pop_copy = pop[:]
    p1 = get_parents(pop_copy)
    pop_copy.remove(p1)
    p2 = get_parents(pop_copy)

    offspring1 = p1[:]
    # we want different parents
    #n_p1 = number_of_nodes(p1)
    #n_p2 = number_of_nodes(p2)
    n_p1 = 20
    n_p2 = 20
    (stree1, route1) = point(p1, n_p1, [])
    (stree2, route2) = point(p2, n_p2, [])

    while abs(tree_depth(stree1) - tree_depth(stree2)) > 2 or stree2 == stree1:

        (stree1, route1) = point(p1, n_p1, [])
        (stree2, route2) = point(p2, n_p2, [])

    #print('before crossover: ', offspring1)
    #print('to replace: ', stree1, route1)
    #print('repalce with: ', stree2, route2)
    offspring1 = replace(offspring1, stree2, route1)
    #print('after crossover: ', offspring1, tree_depth(offspring1))
    #print('----------')
    return offspring1

def tree_depth(tree):
    if not tree:
        return 0
    if isinstance(tree, list):
        #print ('recursive', tree)
        return 1 + max(tree_depth(item) for item in tree)
    else:
        return 0

def mysorting(population, fit, p):
    if len(population) != len(fit):
        print('invaf length in mysorting')
    # sort based on fitness small to large!!!!!
    for i1 in range(0, len(fit) - 2):
        for j in range(i1, len(fit) - 2):
            if fit[i1] > fit[j] and random.uniform(0,1) < p:
                temp = population[i1]
                population[i1] = population[j]
                population[j] = temp

                temp = fit[i1]
                fit[i1] = fit[j]
                fit[j] = temp

# lambda, n, m, data, time_budget
def genetic():
    print('genetic')
    population = initialization(100, 6)
    p_operate = population[:]
    ## check
    f = [fitness(dumps(i), 8, 500, 'small_housing.txt') for i in population]
    mysorting(p_operate, f, 0.8)
    print('initial sorting done', f)
    # select parents for popultion: (50 each time)
    for g in range(1, 10):
        print('generation:', g)
        for i in range (0, 20):
            o1 = crossover(p_operate)
            while tree_depth(o1) > 10 or o1 in population:
                o1 = crossover(p_operate)


            population.append(o1)
            print(len(population))

        f = []
        for i in population:
            f = f + [fitness(dumps(i), 8, 100, 'small_housing.txt')]
        print('fitness', 'ge', f)
        mysorting(population, f, 0.8)
        population = population[0:100]
        f = f[0:100]

    mysorting(population, f, 1)
    return population[0:20]

def testing():
    result = genetic()
    #print(result[0])
    f = []
    for i in result:
        f = f + [fitness(dumps(i), 8, 100, 'testing.txt')]
    mysorting(result, f, 1)
    print(f[0:3])
    for i in range(0, 3):
        print(result)


testing()