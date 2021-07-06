"""
By using list comprehension, please write a program to print the list after
removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].
https://github.com/eunki7/Python-Programs/blob/master/removing_the_values_at_index.py
"""

lists= [12,24,35,70,88,120,155]
lists= [x for (i,x) in enumerate(lists) if i not in (1,3,9)]



print(lists)  # [24, 35, 70, 155]
