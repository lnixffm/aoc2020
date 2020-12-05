#!/usr/bin/python

import sys
# day 5: find the right place in the plane

# Read Data
input_lst = []
fobj = open("input_day05_01.txt", "r")
lines = fobj.readlines() 
for line in lines:
    line = line.replace('\n','')
    input_lst.append(line)

def first_star():
    highest_seat_id = 0

    for seat in input_lst:
        rows = (0, 127) # from  0 to 127
        columns = (0, 7) # from 0 to 7
        #seat = "FBFBBFFRLR"
        for character in seat:
            if character == "F":
                rows = (rows[0], rows[1] - len(range(rows[0],rows[1]+1))/2)
            if character == "B":
                rows = (rows[0] + len(range(rows[0],rows[1]+1))/2, rows[1])
            if character == "L":
                columns = (columns[0], columns[1] - len(range(columns[0],columns[1]+1))/2)

            if character == "R":
                columns = (columns[0] + len(range(columns[0],columns[1]+1))/2, columns[1])
        
        seat_id = int(rows[0]) * int(8) + int(columns[0])
        if seat_id > highest_seat_id:
            highest_seat_id = seat_id
    print("First Star")
    print("Highest Seat ID: {}".format(highest_seat_id))
    return

def second_star():
    plane_lst = []
    for row in range(0, 128):
        plane_lst.append([False,False,False,False,False,False,False,False])

    for seat in input_lst:
        rows = (0, 127) # from  0 to 127
        columns = (0, 7) # from 0 to 7
        for character in seat:
            if character == "F":
                rows = (rows[0], rows[1] - len(range(rows[0],rows[1]+1))/2)
            if character == "B":
                rows = (rows[0] + len(range(rows[0],rows[1]+1))/2, rows[1])
            if character == "L":
                columns = (columns[0], columns[1] - len(range(columns[0],columns[1]+1))/2)
            if character == "R":
                columns = (columns[0] + len(range(columns[0],columns[1]+1))/2, columns[1])
        
        if plane_lst[rows[0]][columns[0]] == True:
            print "error"
            sys.exit(1)
        plane_lst[rows[0]][columns[0]] = True
    
    seat_id_lst = []
    row_count = 0
    for row in plane_lst:
        column_count = 0
        for column in row:
            if column == False:
                seat_id = int(row_count) * int(8) + int(column_count)
                seat_id_lst.append(seat_id)
                #print(seat_id)
            column_count += 1
        row_count += 1

    a = seat_id_lst[0]
    for seat in seat_id_lst[1::]:
        if not a + 1 == seat:
            print("Second Star")
            print("Santa seat is: {}".format(seat))
            sys.exit(0)
        else:
            a += 1
    return

# first star
first_star()

#second star
second_star()