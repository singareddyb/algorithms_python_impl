#!/usr/bin/python
# using python2

from __future__ import division
import sys

'''
Determine the value/weight ratio of each provided item.
Insert item into knapsack that has the highest value/weight ratio to the point where either the total_weight of knapsack is accounted for (or)
to the point where the entire weight of item is accounted for.

Similarly continue down the list for the next n lines.

'''

def fractional_knapsack(value_weight,total_weight):
  value_to_weight = list()
  for i in value_weight:
    value_to_weight.append(i[0]/i[1])
  value_to_weight,value_weight = insertion_sort(value_to_weight, value_weight)

  value_added = 0
  weight_remaining = total_weight
  for idx,v_to_w in enumerate(value_to_weight):

    if weight_remaining > 0:

      if value_weight[idx][1] > weight_remaining:
        value_added += (value_weight[idx][0]*weight_remaining)/value_weight[idx][1]
      else:
        value_added += value_weight[idx][0]

      weight_remaining -= value_weight[idx][1]
  return value_added
     
'''
  InsertionSort/SelectionSort/QuickSort/MergeSort .. sort!!
'''
def insertion_sort(seq1, seq2):
  temp1 = 0
  temp2 = 0
  for i in range(len(seq1)):
    for j in range(0,len(seq1)-i):
      if (j < len(seq1)-1) and seq1[j] < seq1[j+1]:
        temp1 = seq1[j]
        seq1[j] = seq1[j+1]
        seq1[j+1] = temp1
        temp2 = seq2[j]
        seq2[j] = seq2[j+1]
        seq2[j+1] = temp2
  return seq1,seq2

if __name__ == '__main__':
  lines = sys.stdin.readlines()
  value_weight = list()
  temp = list()
  '''
   Input - 
     First line -- (items_that_are_provided_in_next_n-lines, knapsack_max_weight)
     Second line --  (value_item-2, weight_item-2)
     ...
     ...
     i-th line --    (value_item-i, weight_item-i)
     n-th line --  (value_item-n, weight_item-n) 
  '''
  max_items = 0
  knapsack_max_weight = 0
  for idx,line in enumerate(lines):
    if idx == 0:
      input_properties = lines[0]
      properties = [int(x) for x in input_properties.split()]
      max_items = properties[0]
      knapsack_max_weight = properties[1]
    else:
      temp = [int(x) for x in line.split()]
      value_weight.append(temp)
  assert(len(value_weight) == max_items)
  max_value = fractional_knapsack(value_weight, knapsack_max_weight)
  print(max_value)
  
