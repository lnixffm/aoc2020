#!/usr/bin/python
#import numpy as np
#import matplotlib.pyplot as plt


# day 11: seats on ship

# Read Data
input_list = []
fobj = open("input_day11_01.txt", "r")
lines = fobj.readlines() 
line_lst = []
for line in lines:
    line_lst = []
    line = line.replace('\n','')
    for seat in line:
        line_lst.append(seat)
    input_list.append(line_lst)
    
#seat_matrix = np.array(input_list[0])
#for line in input_list[1::]:
#    seat_matrix = np.vstack([seat_matrix, line])


def place_star1(input_list):
    seat_list = []
    ln = 0
    for line in input_list:
        st = 0
        seat_list_line = []
        for seat in line:
            seat_symbol = seat

            if seat == "L" or seat == "#":
                neighbor = 0

                #links
                if st > 0:
                    if line[st-1] == "#":
                        neighbor += 1
                #rechts
                if st < len(line)-1:
                    if line[st+1] == "#":
                        neighbor += 1

                # reihe vorne
                if ln > 0:
                    if st > 0:
                        if input_list[ln-1][st-1] == "#":
                            neighbor += 1
                    if input_list[ln-1][st] == "#":
                        neighbor += 1
                    if st < len(line)-1:
                        if input_list[ln-1][st+1] == "#":
                            neighbor += 1

                # reihe hinten
                if ln < len(input_list)-1:
                    if st > 0:
                        if input_list[ln+1][st-1] == "#":
                            neighbor += 1
                    if input_list[ln+1][st] == "#":
                        neighbor += 1
                    if st < len(line)-1:
                        if input_list[ln+1][st+1] == "#":
                            neighbor += 1
                
                if seat == "L":
                    if neighbor == 0:
                        seat_symbol = "#"
                if seat == "#":
                    if neighbor >= 4:
                        seat_symbol = "L"
            seat_list_line.append(seat_symbol)
            st += 1
        seat_list.append(seat_list_line)       
        ln += 1
    return seat_list


def check_seat(matrix,line_index,seat_index,direction):
    while True:
        if direction == "left":
            line_indicator = 0
            seat_indicator = -1
            if not seat_index > 0:
                return 0
        elif direction == "right":
            line_indicator = 0
            seat_indicator = 1
            if not seat_index < len(matrix[line_index])-1:
                return 0
        elif direction == "top":
            line_indicator = -1
            seat_indicator = 0
            if not line_index > 0:
                return 0
        elif direction == "bottom":
            line_indicator = 1
            seat_indicator = 0
            if not line_index < len(matrix)-1:
                return 0
        if matrix[line_index+line_indicator][seat_index+seat_indicator] == "#":
            return 1
        if matrix[line_index+line_indicator][seat_index+seat_indicator] == "L":
            return 0
        seat_index += seat_indicator
        line_index += line_indicator


def place_star2(input_list):
    seat_list = []
    ln = 0
    for line in input_list:
        st = 0
        seat_list_line = []
        for seat in line:
            seat_symbol = seat

            if seat == "L" or seat == "#":
                neighbor = 0

                #left
                neighbor += int(check_seat(input_list,ln,st,"left"))

                #right
                neighbor += int(check_seat(input_list,ln,st,"right"))

                #top
                neighbor += int(check_seat(input_list,ln,st,"top"))

                #bottom
                neighbor += int(check_seat(input_list,ln,st,"bottom"))

                #top_left
                #neighbor += int(check_seat(input_list,ln,st,"top_left"))
                temp_st = st
                temp_ln = ln
                while True:
                    if temp_st > 0:
                        if temp_ln > 0:
                            if input_list[temp_ln-1][temp_st-1] == "#":
                                neighbor += 1
                                break
                            if input_list[temp_ln-1][temp_st-1] == "L":
                                break
                            temp_ln -= 1
                            temp_st -= 1
                        else:
                            break
                    else:
                        break

                # vorne rechts
                temp_st = st
                temp_ln = ln
                while True:
                    if temp_st < len(line)-1:
                        if temp_ln > 0:
                            if input_list[temp_ln-1][temp_st+1] == "#":
                                neighbor += 1
                                break
                            if input_list[temp_ln-1][temp_st+1] == "L":
                                break
                            temp_ln -= 1
                            temp_st += 1
                        else:
                            break
                    else:
                        break


                # hinten links
                temp_st = st
                temp_ln = ln
                while True:
                    if temp_st > 0:
                        if temp_ln < len(input_list)-1:
                            if input_list[temp_ln+1][temp_st-1] == "#":
                                neighbor += 1
                                break
                            if input_list[temp_ln+1][temp_st-1] == "L":
                                break
                            temp_ln += 1
                            temp_st -= 1
                        else:
                            break
                    else:
                        break

                # hinten rechts
                temp_st = st
                temp_ln = ln
                while True:
                    if temp_st < len(line)-1:
                        if temp_ln < len(input_list)-1:
                            if input_list[temp_ln+1][temp_st+1] == "#":
                                neighbor += 1
                                break
                            if input_list[temp_ln+1][temp_st+1] == "L":
                                break
                            temp_ln += 1
                            temp_st += 1
                        else:
                            break
                    else:
                        break

                if seat == "L":
                    if neighbor == 0:
                        seat_symbol = "#"
                if seat == "#":
                    if neighbor >= 5:
                        seat_symbol = "L"
            seat_list_line.append(seat_symbol)
            st += 1
        seat_list.append(seat_list_line)       
        ln += 1
    return seat_list

def first_star():
    seat_list = input_list
    while True:
        if seat_list == place_star1(seat_list):
            break
        else:
            seat_list = place_star1(seat_list)
    count = 0
    for l in seat_list:
        for s in l:
            if s == "#":
                count += 1
    return count

def second_star():
    seat_list = input_list
    while True:
        if seat_list == place_star2(seat_list):
            break
        else:
            seat_list = place_star2(seat_list)
    count = 0
    for l in seat_list:
        for s in l:
            if s == "#":
                count += 1
    return count

# first star
print("First Star")
print("Answer: {}".format(first_star()))

# second star
#second_star()
print("Second Star")
print("Answer: {}".format(second_star()))