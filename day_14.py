#!/usr/bin/python

import sys

# day 14: Docking Data

# Read Data
mask = ""
input_list = []
input_dic = {}
fobj = open("input_day14_01.txt", "r")
lines = fobj.readlines() 
for line in lines:
    mem = {}
    line = line.replace('\n','')
    if "mask" in line:
        mask = line.split(" ")[-1]
    else:
        mem["mask"] = mask
        adress = line.replace("mem[","").split("]")[0]
        mem["adress"] = adress
        mem["value"] = line.split(" ")[-1]
        input_list.append(mem)

def decimalToBinary(n):  
    return bin(int(n)).replace("0b", "")  

def BinaryTodecimal(n):
    return int(str(n), 2)

def first_star():
    mem_dic = {}
    for mem in input_list:
        adress = mem.get('adress')
        value = decimalToBinary(mem.get('value'))
        mask = mem.get('mask')
        result = ""
        index = -1
        for m in mask[::-1]:
            if len(value) >= index * -1:
                if m == "X":
                    result = result + value[index]
                else:
                    result = result + m
            else:
                if m != "X":
                    result = result + m
                else:
                    result = result + "0"
            index -= 1
        mem_dic[adress] = BinaryTodecimal(result[::-1])
    mem_sum = 0
    for mem_adress in mem_dic:
        mem_sum += int(mem_dic.get(mem_adress))
    return mem_sum

def second_star():
    mem_summ = 0
    mem_dic = {}
    for mem in input_list:
        value = mem.get('value')
        mask = mem.get('mask')
        address_bin = decimalToBinary(mem.get('adress'))
        adress_result = ""
        index = -1
        for m in mask[::-1]:
            if len(address_bin) >= index * -1:
                if m == "0":

                    adress_result = adress_result + address_bin[index]
                else:
                    adress_result = adress_result + m
            else:
                adress_result = adress_result + m
            index -= 1
        
        adress_lst = [adress_result[::-1]]
        while len(adress_lst) < 2 ** adress_result.count("X"):
            for adr in adress_lst:
                if "X" in adr:
                    adress_lst.append(adr.replace("X", "0",1))
                    adress_lst.append(adr.replace("X", "1",1))
                    adress_lst.remove(adr)

        for adr in adress_lst:
            mem_dic[BinaryTodecimal(adr)] = value

    mem_sum = 0
    for mem_adress in mem_dic:
        mem_sum += int(mem_dic.get(mem_adress))
    return mem_sum

# first star
print("First Star")
print("Answer: {}".format(first_star()))

# second star
print("Second Star")
print("Answer: {}".format(second_star()))