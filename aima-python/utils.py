""" originally from aima-python (aima-python.googlecode.com)
functions not needed for our project have been removed

Provide some widely useful utilities. Safe for "from utils import *".
"""

from __future__ import generators
import operator, math, random, copy, sys, os.path, bisect

#______________________________________________________________________________
# Simple Data Structures: infinity, Dict, Struct
def update(x, **entries):
    """Update a dict; or an object with slots; according to entries.
    >>> update({'a': 1}, a=10, b=20)
    {'a': 10, 'b': 20}
    >>> update(Struct(a=1), a=10, b=20)
    Struct(a=10, b=20)
    """
    if isinstance(x, dict):
        x.update(entries)   
    else:
        x.__dict__.update(entries) 
    return x 

#______________________________________________________________________________
# Functions on Sequences (mostly inspired by Common Lisp)
# NOTE: Sequence functions (count_if, find_if, every, some) take function
# argument first (like reduce, filter, and map).

def removeall(item, seq):
    """Return a copy of seq (or string) with all occurences of item removed.
    >>> removeall(3, [1, 2, 3, 3, 2, 1, 3])
    [1, 2, 2, 1]
    >>> removeall(4, [1, 2, 3])
    [1, 2, 3]
    """
    if isinstance(seq, str):
      return seq.replace(item, '')
    else:
      return [x for x in seq if x != item]

def unique(seq):
    """Remove duplicate elements from seq. Assumes hashable elements.
    >>> unique([1, 2, 3, 2, 1])
    [1, 2, 3]
    """
    return list(set(seq))

def count_if(predicate, seq):
    """Count the number of elements of seq for which the predicate is true.
    >>> count_if(callable, [42, None, max, min])
    2
    """
    f = lambda count, x: count + (not not predicate(x))
    return reduce(f, seq, 0)
	
#______________________________________________________________________________
# Functions on sequences of numbers
# NOTE: these take the sequence argument first, like min and max,
# and like standard math notation: \sigma (i = 1..n) fn(i)
# A lot of programing is finding the best value that satisfies some condition;
# so there are three versions of argmin/argmax, depending on what you want to
# do with ties: return the first one, return them all, or pick at random.


def argmin(seq, fn):
    """Return an element with lowest fn(seq[i]) score; tie goes to first one.
    >>> argmin(['one', 'to', 'three'], len)
    'to'
    """
    best = seq[0]; best_score = fn(best)
    for x in seq:
        x_score = fn(x)
        if x_score < best_score:
            best, best_score = x, x_score
    return best

def argmax(seq, fn):
    """Return an element with highest fn(seq[i]) score; tie goes to first one.
    >>> argmax(['one', 'to', 'three'], len)
    'three'
    """
    return argmin(seq, lambda x: -fn(x))

#______________________________________________________________________________
# Statistical and mathematical functions

def log2(x):
    """Base 2 logarithm.
    >>> log2(1024)
    10.0
    """
    return math.log10(x) / math.log10(2)

def mean(values):
    """Return the arithmetic average of the values."""
    return sum(values) / float(len(values))

def num_or_str(x):
    """The argument is a string; convert to a number if possible, or strip it.
    >>> num_or_str('42')
    42
    >>> num_or_str(' 42x ')
    '42x'
    """
    if isnumber(x): return x
    try:
        return int(x) 
    except ValueError:
        try:
            return float(x) 
        except ValueError:
                return str(x).strip() 

def normalize(numbers, total=1.0):
    """Multiply each number by a constant such that the sum is 1.0 (or total).
    >>> normalize([1,2,1])
    [0.25, 0.5, 0.25]
    """
    k = total / sum(numbers)
    return [k * n for n in numbers]

#______________________________________________________________________________
# Misc Functions

def isnumber(x):
    "Is x a number? We say it is if it has a __int__ method."
    return hasattr(x, '__int__')

def print_table(table, header=None, sep=' ', numfmt='%g'):
    """Print a list of lists as a table, so that columns line up nicely.
    header, if specified, will be printed as the first row.
    numfmt is the format for all numbers; you might want e.g. '%6.2f'.
    (If you want different formats in differnt columns, don't use print_table.)
    sep is the separator between columns."""
    justs = [if_(isnumber(x), 'rjust', 'ljust') for x in table[0]]
    if header:
        table = [header] + table
    table = [[if_(isnumber(x), lambda: numfmt % x, x)  for x in row]
             for row in table]    
    maxlen = lambda seq: max(map(len, seq))
    sizes = map(maxlen, zip(*[map(str, row) for row in table]))
    for row in table:
        for (j, size, x) in zip(justs, sizes, row):
            print getattr(str(x), j)(size), sep,
        print

def AIMAFile(components, mode='r'):
    "Open a file based at the AIMA root directory."
    import utils
    dir = os.path.dirname(utils.__file__)
    return open(apply(os.path.join, [dir] + components), mode)

def DataFile(name, mode='r'):
    "Return a file in the AIMA /data directory."
    return AIMAFile(['..', 'data', name], mode)


