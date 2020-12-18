#!/usr/bin/python
import numpy as np
import sys

# day 17: cubes

# Read Data
z = np.empty((0,3), str)
fobj = open("input_day17_01.txt", "r")
lines = fobj.readlines()
for line in lines:
    line = line.replace('\n','')
    e_list = []
    for e in line:
        e_list.append(e)
    z = np.append(z, np.array([e_list]), axis=0)

print z
new_list = []
for row in z:
    print row
    new_list.append(row)
print new_list

print z.ndim
sys.exit(1)

def check_active_neighbors(position,matrix):
    print position
    return


def first_star():
    for c in z:
        print c
    #check_active_neighbors((0,2),input_lst)
    return 1

def second_star():
    return 1

# first star
print("First Star")
print("Answer: {}".format(first_star()))

# second star
#print("Second Star")
#print("Answer: {}".format(second_star(first_star()[1])))