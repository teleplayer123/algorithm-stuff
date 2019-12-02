import sys
import os
import glob
import functools

def get_files():
    file_list = []
    for path in sys.argv[1:]:
        for root, _ , files in os.walk(path):
            for filename in files:
                fullname = os.path.join(root, filename)
                file_list.append(fullname)
    return file_list

def get_files_global():
    file_list = []
    for path in sys.argv[1:]:
        for filename in glob.iglob(path):
            if not os.path.isfile(filename):
                continue
            file_list.append(filename)
    return file_list   

def memo(func):
    cache = {}
    @functools.wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap

def mean(seq):
    return sum(seq) / len(seq)

def variance(values):
    return sum([i - mean(values)**2 for i in values])

def covariance(x, y):
    covar = 0.0
    for i in range(len(x)):
        covar += (x[i] - mean(x)) * (y[i] - mean(y))
    return covar

def transpose(matrix):
    size = len(matrix) 
    res = [[matrix[y][x] for y in range(size)] for x in range(size)]
    return res

