#!/usr/bin/python

import sys
# day 7: packages

# Read Data
input_dic = {}
fobj = open("input_day07_01.txt", "r")
lines = fobj.readlines() 
for line in lines:
    line = line.replace('\n','')
    key = line.split("contain")[0].replace(" ","_").replace("_bags_","")
    input_dic[key] = []
    for contain in line.split("contain")[1].split(","):
        count = contain.split(" ")[1]
        if "no" in count:
            count = 0
        bg = contain.split(" ")[2] + "_" + contain.split(" ")[3]
        input_dic[key].append((bg, count))

#print(input_dic)

def inbag(bag):
    inbag_lst = []
    for bag_type in input_dic:
        for contain in input_dic.get(bag_type):
            if bag in contain:
                inbag_lst.append(bag_type)
    return inbag_lst


def first_star(search_bag):
    bag_lst = []
    bags = inbag(search_bag)
    bagss = []
    while len(bags) != 0:
        for bag in bags:
            if not bag in bag_lst:
                bag_lst.append(bag)
                bags.append(bag)
                for c in inbag(bag):
                    bags.append(c)
            else:
                bags.remove(bag)
    return len(bag_lst)

def second_star(search_bag):
    counter = 0
    searching_lst = []

    for bag in input_dic.get(search_bag):
        counter += int(bag[1])
        for i in range(int(bag[1])):
            searching_lst.append(bag[0])

    while len(searching_lst) != 0:
        for searching_bag in searching_lst:      
            for bag in input_dic.get(searching_bag):
                counter += int(bag[1])
                for i in range(int(bag[1])):
                    searching_lst.append(bag[0])
            searching_lst.remove(searching_bag)
    return counter


# first star
print("First Star")
print("Total: {}".format(first_star("shiny_gold")))

# second star
print("Second Star")
print("Total: {}".format(second_star("shiny_gold")))
