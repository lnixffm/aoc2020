#!/usr/bin/python

# day 2: check valid passwords

# Read Data
input_lst = []
fobj = open("input_day02_01.txt", "r")
for item_raw in fobj:
    dic_ob = {}
    dic_ob["range"] = item_raw.split(" ")[0]
    dic_ob["sub"] = item_raw.split(" ")[1].split(":")[0]
    dic_ob["pw"] = item_raw.split(" ")[-1].replace('\n','')
    input_lst.append(dic_ob)

def first_star():
    valid_pw_count = 0
    for item in input_lst:
        sub_count = item.get("pw").count(item.get("sub"))
        range_start = item.get("range").split("-")[0]
        range_end = item.get("range").split("-")[1]
        if int(sub_count) >=  int(range_start):
            if int(sub_count) <= int(range_end):
                valid_pw_count = valid_pw_count + 1
    print("First Star:{}".format(valid_pw_count))
    return

def second_star():
    valid_pw_count = 0
    for item in input_lst:
        sub = item.get("sub")
        position_1 = int(item.get("range").split("-")[0]) - 1
        position_2 = int(item.get("range").split("-")[1]) - 1
        if item.get("pw")[position_1] == sub:
            if not item.get("pw")[position_2] == sub:
                valid_pw_count = valid_pw_count + 1
        else:
            if item.get("pw")[position_2] == sub:
                valid_pw_count = valid_pw_count + 1
    print("Second Star:{}".format(valid_pw_count))
    return

first_star()
second_star()