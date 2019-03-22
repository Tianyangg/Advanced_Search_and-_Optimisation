from sexpdata import *

import random
import io
import math
import fire
from pathlib import Path
import numpy as np
import csv
import main

# define the function dictionary:
func = {'add', 'sub', 'mul', 'div', 'pow', 'sqrt', 'log', 'exp', 'max', 'ifleq', 'data', 'diff', 'avg'}
terminate = {'var', 'const'}

# return the fitness  value of a given expresssioon
def fitness(expr, n, m, data):
    path = '/Users/tianyangsun/Documents/Uob_Y3_S2/02 Search and Optimisation/labs/08_Time_series_prediction/' + data
    print("evaluating fitness")
    # read files here: replace later
    X, Y = main.readdata(path, n)
    # sum of squares
    mse = [math.pow((yy - main.niso_lab3(1, n, xx, expr)), 2) for (xx, yy) in zip(X, Y)]
    #devide m
    f = sum(mse)/m
    return f

# select a random subtree
# crossover
# muation
# raw_fitness
# penalty
# create sibling
# create children
# parameter: initial population, max_inital_depth(idepth)
def initialization(size, maxdepth):
    return [full(maxdepth) for i in range (0, size)]

def full(maxdepth):
    if maxdepth == 0:
        leaf = random.choice(tuple(terminate))
        if leaf == 'var':
            return 'var'
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
def ramped_half(maxdepth):
    # DO THIS LATER
    print("ramped half and half")

def get_parents(pop):
    p = 0.4 # the parameter should it be in the function
    for i in range(0, len(pop)):
        if random.uniform(0, 1) <  p * math.pow((1 - p), i):
            return pop[i]

# return the number of nodes, used in mutation
def number_of_nodes(tree):
    if isinstance(tree, str) or isinstance(tree, int):
        return 1
    if len(tree) == 2:
        if isinstance(tree[1], str):
            return 2
        else:
            return 1 + number_of_nodes(tree[1])
    if len(tree) == 3:
        if isinstance(tree[1], str) and isinstance(tree[2], str):
            return 3
        if isinstance(tree[1], str) and not isinstance(tree[2], str):
            return 2 + number_of_nodes(tree[2])
        if not isinstance(tree[1], str) and isinstance(tree[2], str):
            return 2 + number_of_nodes(tree[1])
        else:
            return 1 + number_of_nodes(tree[1]) + number_of_nodes(tree[2])
    else:
        return 1 + number_of_nodes(tree[1]) + number_of_nodes(tree[2]) + number_of_nodes(tree[3]) + number_of_nodes(tree[4])

# return crossover point
# input the tree and the number of nodes
def point(tree, n):
    index = ''
    if isinstance(tree, str) or isinstance(tree, int):
        index = index + '0'
        return tree, index
    else:
        if random.uniform(0, 1) < 1/n:
            return tree, index
        else:
            tree_len = len(tree)
            if tree_len == 2:
                index = index + '1'
                return point(tree[1], n), index
            else:
                rand = random.uniform(0, 1)
                print(rand)
                for i in range(0, tree_len - 1):
                    if rand < i*1/(tree_len - 1):
                        index = index + str(i)
                        return point(tree[i], n), index
                index = index + str(tree_len)
                return point(tree[tree_len - 1], n), index

def crossover(pop):
    pop_copy = pop[:]
    p1 = get_parents(pop_copy)
    pop_copy.remove(p1)
    p2 = get_parents(pop_copy)
    # we want different parents
    n_p1 = number_of_nodes(p1)
    n_p2 = number_of_nodes(p2)


    print('crossover')

population = initialization(4, 3)
print(population[2])
nn = number_of_nodes(population[2])
print(nn)
print(point(population[2], nn))