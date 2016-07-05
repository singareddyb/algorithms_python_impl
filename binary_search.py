#!/usr/bin/python
# using python2
import sys

def binary_search(list_of_input, num, from_index, to_index):

  half_of_length_input_list = (from_index+to_index+1)/2 - from_index
  if half_of_length_input_list == 0:
    if list_of_input[from_index] == num:
      return from_index
    else:
      return -1

  if list_of_input[from_index + half_of_length_input_list-1] == num:
    return from_index + half_of_length_input_list - 1

  if num < list_of_input[from_index + half_of_length_input_list - 1]:
    return binary_search(list_of_input,num, 0, from_index + half_of_length_input_list - 1)       
  elif num > list_of_input[from_index + half_of_length_input_list - 1]:  
    return binary_search(list_of_input,num,from_index + half_of_length_input_list, to_index)

if __name__ == '__main__':
  inputs = sys.stdin.readlines()
  assert(len(inputs) == 2)
  for idx,line in enumerate(inputs):
    if idx == 0:
      print(line)
      list_of_input = [int(x) for x in line.split()]
      assert(list_of_input[0] == len(list_of_input[1:]))
      list_of_input = list_of_input[1:]
      print(list_of_input)
    if idx == 1:
      print(line)
      list_of_search_numbers = [int(x) for x in line.split()]
      assert(list_of_search_numbers[0] == len(list_of_search_numbers[1:]))  
      list_of_search_numbers = list_of_search_numbers[1:]
      print(list_of_search_numbers)
  index = -3
  for search_num in list_of_search_numbers:
    index = binary_search(list_of_input, search_num,0,len(list_of_input)-1)
    print(index)
