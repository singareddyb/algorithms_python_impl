#!/usr/bin/python
import sys

def zero_one_non_repeating_knapsack(total_weight,weight_of_items,T):
  for i,row in enumerate(T):
    if i > 0:
      for j,column in enumerate(row):
        local_weight = j+1 - weight_of_items[i]
        if local_weight < 0:
          T[i][j] = T[i-1][j]
        elif local_weight > 0:
          if j+1 >= weight_of_items[i]+T[i-1][local_weight-1]:
            T[i][j] = weight_of_items[i] + T[i-1][local_weight-1]
          else:
            T[i][j] = weight_of_items[i]
        else:
          T[i][j] = weight_of_items[i]
        '''print(T)'''

if __name__ == '__main__':
  lines = sys.stdin.readlines()
  assert(len(lines) == 2)
  for index,line in enumerate(lines):
    if index == 0:
      total_weight,num_of_items = [int(x) for x in line.split()]
    else:
      assert(len(line.split()) == num_of_items)
      weight_of_items = [int(x) for x in line.split()]
      weight_of_items = [0] + weight_of_items
  T = [[0 for x in range(0,total_weight)] for y in range(0,len(weight_of_items))]
  zero_one_non_repeating_knapsack(total_weight,weight_of_items,T)
  print(T[num_of_items][total_weight-1])
