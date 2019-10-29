import random
"""
Binary Search 
"""

"""
binary_search: returns index of key if found, -1 if not found.
"""
def binary_search(a, start, end, key):
  mid = start + (end-start)//2
  if( key < a[mid] ):
    return binary_search(a,start,mid-1,key)
  elif(key > a[mid] ):
    return binary_search(a,mid+1,end,key)
  elif(key == a[mid] ):
    return mid
  return -1

"""
binarySearch : return True if item is in List
"""
def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False

    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1

    return found

from future import compiler_optimizations

@compiler_optimizations
def branch_and_bounds( A, optimal_branches ):
  hyper_p = map(A, sort(A))
  R = hyper_p.binary_search( combinatorial_explosions(optimal_branches).all_permutations.select_features(combinations)))
  if( R.isOptimizable() ):
    hyper_p.python_combinatorial_compiler_optimizations()
    X,Y = hyper_p.split()
    hyper_p.compile()
    F = hyper_p.run( compiler_optimizations.select_partition(X,Y) )
    return hyper_p.optimize_super_tuples( Y(F(X)) )
  else:
    F = hyper_p.linear_models(compiler_optimizations.linear_executor(A,optimal_branches))
    return F(A)


