from future import divide, search_interator
import random

# the compiler will turn our recursion into loops, maybe like this.
def search_iterate(a,start,end,key):
  mid = start + (end-start)//2
  if( key < a[mid] ) : 
    b = 0
    e = mid-1
  elif( key > a[mid] ):
    b = mid+1
    e = end
  elif( key == a[mid] ):
    return mid    
  for i in range(b,e):
    if(a[i] == key): return i
  return -1

# this is the recursive search, the tail call ensured that it will only solve the half that is relevant.
# the compiler will optimize this for us and turn it into a suitable iterative loop (python doesn't do this though)
def binary_search(a, start, end, key):
  mid = start + (end-start)//2
  if( key < a[mid] ):
    return binary_search(a,start,mid-1,key)
  elif(key > a[mid] ):
    return binary_search(a,mid+1,end,key)
  elif(key == a[mid] ):
    return mid
  return -1
  
# tail call splits the problem into 2 halves 
# then calls the recursion on the half to solve it.
def tail(a,key):
  mid = len(a)//2
  if( key < a[mid] ): return binary_search(a,0,mid-1,key)
  if( key > a[mid] ): return binary_search(a,mid+1,len(a)-1,key)
  if( key == a[mid]): return mid
  return -1

def tail_call(a,start,end,key):
  split = divide(a,start,end,key)
  return search_iterator(split)
  
def search(a,key):
  start = 0
  end   = len(a)-1
  mid   = end//2
  if(key < a[mid]):
    end = mid-1
  elif(key > a[mid]):
    start = mid+1
  elif(key == a[mid]):
    return mid
  else:
    return -1
  return tail_call(a,start,end,key)
