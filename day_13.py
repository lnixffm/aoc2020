#!/usr/bin/python
import sys
# day 12: Rain Risk

# Read Data
input_list = []
input_list_contest = []
fobj = open("input_day13_01.txt", "r")
lines = fobj.readlines() 
for line in lines:
    line = line.replace('\n','')
    for element in line.split(","):
        if element != "x":
            input_list.append(element)
        input_list_contest.append(element)

def first_star():
    time = int(input_list[0])
    while True:
        for bus in input_list[1::]:
            if (float(time)/float(bus)).is_integer():
                return((int(time) - int(input_list[0])) * int(bus))
        time += 1


def second_star():

    # create pattern
    pattern_list = []
    t = 0
    for bus in input_list_contest[1::]:
        #print bus
        pattern_dic = {}
        if bus != "x":
            #pattern_list.append((bus, t))
            pattern_dic["id"] = bus
            pattern_dic["time"] = [int(bus)]
            pattern_dic["t"] = t
            pattern_list.append(pattern_dic)
            print pattern_dic
        a = 2 % float(bus)
        print a




# first star
print("First Star")
print("Answer: {}".format(first_star()))

# second star
print("Second Star")
print("Answer: {}".format(second_star()))

