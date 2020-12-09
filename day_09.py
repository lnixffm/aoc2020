#!/usr/bin/python

# day 9: Encoding Error

# Read Data
input_list = []
fobj = open("input_day09_01.txt", "r")
lines = fobj.readlines() 
for line in lines:
    line = line.replace('\n','')
    input_list.append(int(line))

#print(input_list)

def first_star():
    preamble = 25
    first = 0
    last = 25
    found = "no"
    for zahl in input_list[preamble::]:
        for i in input_list[first:last]:
            for k in input_list[first:last]:
                if not i == k:
                    c = i + k
                    if c == zahl:
                        found = "yes"
        if found == "no":
            return zahl
        first += 1
        last += 1
        found = "no"


def second_star(zahl):
    goal_lst = []
    for x in input_list:
        if x == zahl:
            break
        else:
            goal_lst.append(x)
    ss = 1
    for z in goal_lst:
        f_lst = [z]
        for f in goal_lst[ss::]:
            f_lst.append(f)
            z = z + f
            if z == zahl:
                return min(f_lst) + max(f_lst)
        ss += 1

# first star
first_star()
print("First Star")
print("first number: {}".format(first_star()))

# second star
print("Second Star")
print("encryption weakness: {}".format(second_star(first_star())))