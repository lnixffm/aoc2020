#!/usr/bin/python
import sys

# day 18: homework

# Read Data
input_data = []
fobj = open("input_day18_01.txt", "r")
lines = fobj.readlines()
for line in lines:
    line = line.replace(' ','').replace('\n','')
    e_list = []
    for e in line:
        e_list.append(e)
    input_data.append(e_list)


def calculate_in_clip(c_list):
    result = int(c_list[0])
    operator = ""
    for n in c_list[1::]:
        if n == "+":
            operator = "plus"
        elif n == "*":
            operator = "multi"
        else:
            if operator == "plus":
                result = result + int(n)
            elif operator == "multi":
                result = result * int(n)
            else:
                print("ERROR")
                sys.exit(1)
    return result

def first_star():
    result = 0
    for task in input_data:
        while len(task) != 1:
            clip = None
            clip_lst = []
            new_lst = []
            index_open = 0
            index_close = 0
            index = 0
            for e in task:
                if e == ")":
                    clip_sum = calculate_in_clip(clip_lst)
                    index_close = index
                    clip = "close"
                    index = 0
                    for p in task:
                        if index == index_open:
                            new_lst.append(clip_sum)
                        elif index > index_open:
                            if index > index_close:
                                new_lst.append(p)
                            else:
                                a = ""
                        else:
                            new_lst.append(p)
                        index += 1
                    task = new_lst
                    break
                if clip == "open":
                    clip_lst.append(e)
                if e == "(":
                    index_open = index
                    clip = "open"
                    clip_lst = []
                index += 1
            if clip == None:
                task = [ calculate_in_clip(task) ]
        result += int(task[0])
    return result

def calculate_in_clip_and_plus(c_list):
    while "+" in c_list:
        new_list = []
        index = 0
        for n in c_list:
            if n == "+":
                summ = int(c_list[index-1]) + int(c_list[index+1])
                new_index = 0
                for c in c_list:
                    if new_index == index-1:
                        new_list.append(summ)
                    elif new_index >= index:
                        if new_index > index+1:
                            new_list.append(c)
                    else:
                        new_list.append(c)
                    new_index += 1
                c_list = new_list
                break
                new_list = []
            index += 1
    return calculate_in_clip(c_list)

def second_star():
    result = 0
    for task in input_data:
        while len(task) != 1:
            clip = None
            clip_lst = []
            new_lst = []
            index_open = 0
            index_close = 0
            index = 0
            #print task
            for e in task:
                if e == ")":
                    clip_sum = calculate_in_clip_and_plus(clip_lst)
                    index_close = index
                    clip = "close"
                    index = 0
                    for p in task:
                        if index == index_open:
                            new_lst.append(clip_sum)
                        elif index > index_open:
                            if index > index_close:
                                new_lst.append(p)
                            else:
                                a = ""
                        else:
                            new_lst.append(p)
                        index += 1
                    task = new_lst
                    #print task
                    break
                    #print clip_lst
                if clip == "open":
                    clip_lst.append(e)
                if e == "(":
                    index_open = index
                    clip = "open"
                    clip_lst = []
                index += 1
            if clip == None:
                #print "halt Stop"
                task = [ calculate_in_clip_and_plus(task) ]
        result += int(task[0])
    return result

# first star
print("First Star")
print("Answer: {}".format(first_star()))

# second star
print("Second Star")
print("Answer: {}".format(second_star()))