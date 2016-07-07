#!/usr/bin/python
import sys

def generate_pivot_index(lst,begin,end):
  ''' Pick left-most element as pivot element '''
  pivot = lst[begin]
  k = begin
  for j in range(begin+1,end+1):
    if lst[j] <= pivot:
      k += 1
      temp = lst[k]
      lst[k] = lst[j]
      lst[j] = temp
  temp = lst[begin]
  lst[begin] = lst[k]
  lst[k] = temp
  return k

def quicksort(lst,begin,end):

  if end == begin:
    return lst

  pivot_index = generate_pivot_index(lst,begin,end)
  if pivot_index-1 >= begin:
    lst = quicksort(lst,begin,pivot_index-1)
  if pivot_index+1 <= end:
    lst = quicksort(lst,pivot_index+1,end)
  
  return lst

if __name__ == '__main__':
  line = sys.stdin.read()
  lst = [int(x) for x in line.split()]
  result = list()
  result = quicksort(lst,0,len(lst)-1)

  print(result)
 
