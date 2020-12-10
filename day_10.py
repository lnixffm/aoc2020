#!/usr/bin/python
import sys
# day 10: 

# Read Data
input_list = []
fobj = open("input_day10_01.txt", "r")
lines = fobj.readlines() 
for line in lines:
    line = line.replace('\n','')
    input_list.append(int(line))
input_list.append(max(input_list) +3 )
print sorted(input_list)
cache = {}

def first_star():
    maindic = {}
    joltage = 0

    for step in sorted(input_list):
        difference = step - joltage
        if difference in maindic:
            maindic[difference] += 1
        else:
            maindic[difference] = 1
        joltage = step

    result = 1
    for dif in maindic:
        result = result * maindic.get(dif)
    return result

def second_star():
    dic = {}
    total = 1
    input_list.append(0)
    position = 1
    for step in sorted(input_list):
        step_lst = []
        for d in sorted(input_list)[position::]:
            if d > step + 3:
                break
            step_lst.append(d)
        position += 1

        dic[step] = step_lst
    cache = {}
    return(calculate(sorted(input_list)[0], dic))

def calculate(n, dic):
    if not dic[n]:
        return 1
    if n in cache.keys():
        return cache[n]
    total = 0
    for x in dic[n]:
        iteratie = calculate(x, dic)
        cache[x] = iteratie
        total += iteratie
    return total

# first star
print("First Star")
print("Answer: {}".format(first_star()))

# second star
second_star()
print("Second Star")
print("Answer: {}".format(second_star()))