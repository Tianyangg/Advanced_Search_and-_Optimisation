import functions as f
from sexpdata import *

import io
import math
import fire
from pathlib import Path
import numpy as np
import csv

def niso_lab3(question, n, x, expr):
    if question == 1:
        xnew = [float(i) for i in x.split()]
        #print(len(xnew))
        if n != len(xnew):
            #print('invalid input')
            return 0
        f.num = xnew

        f.nn = n

        r = f.parse_ev(expr)
        return r

# data: path to the text file
# n is the dimension of the input vector
def readdata(filepath, n):
    with open(filepath, 'r') as f1:
        X_data = [row[0:n] for row in csv.reader(f1, delimiter='\t')]
    with open(filepath, 'r') as f2:
        Y_data = [row[n] for row in csv.reader(f2, delimiter='\t')]

    return X_data, Y_data




#print(niso_lab3(1, 4, '1.0 2.0 3.0 5.0', '(exp (data 2))'))
#print(parse_ev("(mul (mul (data 2) (log 8)) (log 8))"))
#print(f.parse_ev("(max (data 0) (data 1))"))


#print(loads("1.0 2.0 3.0"))
#print(loads("(mul (mul (data 2) (log 8)) (log 8))"))


#if __name__ == '__main__':
#  fire.Fire()