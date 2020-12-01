#!/usr/bin/python

# expense report

# Read Data
input_lst = []
fobj = open("input_day01_01.txt", "r")
for inputnumber_raw in fobj:
    input_lst.append(int(inputnumber_raw.replace('\n','')))

# Example
# input_lst = [ 1721, 979, 366, 299, 675, 1456]

def first_star():
    for item in input_lst:
        for item_2 in input_lst:
            if not item == item_2:
                summ = item + item_2
                if summ == 2020:
                    result = item * item_2
                    print("First Star:{}".format(result))
                    return

def second_star():
    for item in input_lst:
        for item_2 in input_lst:
            for item_3 in input_lst:
                if not item == item_2 and not item == item_3 and not item_2 == item_3:
                    summ = item + item_2 + item_3
                    if summ == 2020:
                        result = item * item_2 * item_3
                        print("Second Star:{}".format(result))
                        return

first_star()
second_star()