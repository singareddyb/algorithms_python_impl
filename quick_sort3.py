#!/usr/bin/python
import sys
import pdb


def generate_3way_partition_indices(lst,begin,end):
  ''' Pick left-most element as pivot element 
   Example - The very first time this function is called, the below happens
   begin - 
      low starts at begin
      high starts at end
      i = begin
      pivot = 6
      6 7 2 6 3 5 6  i=0, low = 0, high = 6 
      6 7 2 6 3 5 6  i=1, low = 0, high = 6
      6 6 2 6 3 5 6  i=1, low = 0, high = 5
      6 6 2 6 3 5 6  i=2, low = 0, high = 5
      2 6 6 6 3 5 6  i=3, low = 1, high = 5
      2 6 6 6 3 5 6  i=4, low = 1, high = 5
      2 3 6 6 6 5 6  i=5, low = 2, high = 5
      2 3 5 6 6 6 6  i=6, low = 3, high = 5
    stop
    return low,high
  '''
  pivot = lst[begin]
  low = begin
  high = end
  i = begin
  while i <= high:
    if lst[i] < pivot:
      temp = lst[low]
      lst[low] = lst[i]
      lst[i] = temp
      low = low+1
      i = i+1
    elif lst[i] > pivot:
      temp = lst[high]
      lst[high] = lst[i]
      lst[i] = temp
      high = high-1
    else:
      i = i+1
  return low,high

def quicksort(lst,begin,end):

  if end == begin:
    return lst

  low,high = generate_3way_partition_indices(lst,begin,end)
  ''' Can't go lower than the lowest index in each recursive step '''
  if low-1 >= begin:
    quicksort(lst,begin,low-1)
  ''' Can't go higher than the highest index in each recursive step '''
  if high+1 <= end:
    quicksort(lst,high+1,end)
  return lst

if __name__ == '__main__':
  line = sys.stdin.read()
  lst = [int(x) for x in line.split()]
  result = list()
  result = quicksort(lst,0,len(lst)-1)

  print(result)
 
