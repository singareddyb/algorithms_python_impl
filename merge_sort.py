#!/usr/bin/python

import sys
''' Worst-case complexity is O(n log(n)) 
    Each divide steps increases problem size by a power of 2. So, there are log(n) such levels. At the log(n) level, there are n-problems of size=1.
    Conquer step happens in linear-time.
'''

def mergesort(lst,begin,end):
  ''' Divide and Conquer'''
  ''' Divide step 
      Divide from 1-problem all the way down to n sub-problems each of which returns an list of length=1. The problem size is log(n).
      Maintain lower half of the division and the upper half of the division at each step.
      Only at the log(n) level, there will not be a need for lowHalf and highHalf lists. We directly return a list of length = 1.
      Then proceed to conquer step at each level
  '''
  lowHalf = list()
  highHalf = list()
  result = list()
  diff = end-begin
  half = diff/2
  if diff == 0:
    result.append(lst[begin])
    return result
  lowHalf = mergesort(lst,begin,begin+half)
  highHalf = mergesort(lst,begin+half+1,end)
  ''' Conquer step 
      At p-th level, (2^p) sub-problems to conquer. n/(2^p) elements to sort in each sub-problem. 
      Let k be the constant factor of comparisions+appending_to_list etc.,
      So, p-th level, can be solved in - (2^p) * k * (n/(2^p)) = k*n 
      Since there are log(n) such levels of sub-problems, the complete complexity is k*n*log(n) = O(n*log(n))
  '''
  i = begin
  j = begin+half+1
  while (i <= begin+half) and (j <= end) :
    if lowHalf[i-begin] < highHalf[j-begin-half-1]:
      result.append(lowHalf[i-begin])
      i += 1
    else:
      result.append(highHalf[j-begin-half-1])
      j += 1
  if j <= end:
    while j <= end:
      result.append(highHalf[j-begin-half-1])
      j += 1
  if i <= begin+half:
    while i <= begin+half:
      result.append(lowHalf[i-begin])
      i += 1
 
  return result


if __name__ == '__main__':
  line = sys.stdin.read()
  lst = [int(x) for x in line.split()]
  result = list()
  result = mergesort(lst,0,len(lst)-1)

  print(result)
