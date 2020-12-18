#!/usr/bin/python

import sys

# day 16: train tickets

# Read Data

myticket_lst = []
nerby_ticket_list = []
info_dic = {}
info_lst = []
sec_dic = {}
fobj = open("input_day16_01.txt", "r")
lines = fobj.readlines()
section = "information"
for line in lines:
    line = line.replace('\n','')
    if section == "myticket":
        ts = line.split(",")
        myticket_lst.append(ts)
    if section == "nearbyticket":
        ts = line.split(",")
        nerby_ticket_list.append(ts)
    if "your ticket" in line:
        section = "myticket"
    if "nearby tickets:" in line:
        section = "nearbyticket"
    if section == "information":
        key_info = line.replace(" ","_").split(":")[0]
        value_info = line.split(":")[1].split(' or ')
        info_dic[key_info] = []
        for v in value_info:
            info_dic[key_info].append((int(v.split("-")[0]),int(v.split("-")[1])))
        info_lst.append(key_info)

def first_star():
    valid_nerby_ticket_list = []
    invalid = 0
    for ticket in nerby_ticket_list:
        ticket_valid = True
        for info in ticket:
            c = False
            for i in info_dic:
                if int(info) in range(info_dic.get(i)[0][0],info_dic.get(i)[0][1]+1):
                    c = True
                    break
                if int(info) in range(info_dic.get(i)[1][0],info_dic.get(i)[1][1]+1):
                    c = True
                    break
            if not c:
                ticket_valid = False
                invalid += int(info)
        if ticket_valid:
            valid_nerby_ticket_list.append(ticket)
    return invalid,valid_nerby_ticket_list

def second_star(valid_lst):
    position_dic = {}
    position_dic_valid = {}
    for i in range(0,len(info_dic)):
        position_dic[i] = []
        position_dic_valid[i] = []
    for ticket in valid_lst:
        index = 0
        for e in ticket:
            true_list = []
            for info in info_dic:
                c = False
                if int(e) in range(info_dic.get(info)[0][0],info_dic.get(info)[0][1]+1):
                    c = True
                if int(e) in range(info_dic.get(info)[1][0],info_dic.get(info)[1][1]+1):
                   c = True  
                if c:
                    true_list.append(info)
            for info in info_dic:
                if not info in true_list:
                    position_dic[index].append(info)
            index += 1
    il = len(info_lst)
    for p in position_dic:
        c_list = []
        for c in info_lst:
            if not c in position_dic.get(p):
                position_dic_valid[p].append(c)
    v_dic = {}
    searching = []
    pp = len(info_lst)
    while pp > 0:
        for k in position_dic_valid:
            if len(position_dic_valid.get(k)) == 1:
                searching.append(position_dic_valid.get(k)[0])
                v_dic[k] = position_dic_valid.get(k)[0]
                position_dic_valid.pop(k)
                pp -= 1
                break
            elif len(position_dic_valid.get(k)) > 1:
                for e in searching:
                    if e in position_dic_valid.get(k):
                        position_dic_valid[k].remove(e)
    result = 1
    index = 0
    for t in v_dic:
        if "departure" in v_dic.get(t):
            result = result * int(myticket_lst[0][index])
        index += 1
    return result

# first star
print("First Star")
print("Answer: {}".format(first_star()[0]))

# second star
print("Second Star")
print("Answer: {}".format(second_star(first_star()[1])))