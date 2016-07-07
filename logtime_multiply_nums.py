#!/usr/bin/python
# using python2
import sys

def multiply(x,y):
  sum = 0
  if y%2 == 1:
    sum += x
  while y != 0:
    if y%2 == 1:
      sum += x
    y = y/2
    x = x*2
  return sum

if __name__ == '__main__':
  line = sys.stdin.read()
  numbers = [int(x) for x in line.split()]
  assert(len(numbers) == 2)
  s = multiply(numbers[0],numbers[1])
  print(s)
