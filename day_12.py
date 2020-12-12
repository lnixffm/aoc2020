#!/usr/bin/python
#import numpy as np
#import matplotlib.pyplot as plt
import sys

# day 12: Rain Risk

# Read Data
input_list = []
fobj = open("input_day12_01.txt", "r")
lines = fobj.readlines() 
for line in lines:
    line = line.replace('\n','')
    input_list.append((line[0],line[1::]))

#print input_list
    
#seat_matrix = np.array(input_list[0])
#for line in input_list[1::]:
#    seat_matrix = np.vstack([seat_matrix, line])

def first_star(facing,instruction_list):
    n = 0
    e = 0
    w = 0
    s = 0
    for step in instruction_list:
        
        if step[0] == "N":
            n += int(step[1])
        
        if step[0] == "E":
            e += int(step[1])

        if step[0] == "W":
            w += int(step[1])

        if step[0] == "S":
            s += int(step[1])

        if step[0] == "F":
            if facing == "north":
                n += int(step[1])
            if facing == "east":
                e += int(step[1])
            if facing == "west":
                w += int(step[1])
            if facing == "south":
                s += int(step[1])

        if step[0] == "R":
            rotation = int(step[1]) / 90
            while rotation >= 1:
                if facing == "north":
                    facing = "east"
                elif facing == "east":
                    facing = "south"
                elif facing == "west":
                    facing = "north"
                elif facing == "south":
                    facing = "west"
                rotation -= 1
        
        if step[0] == "L":
            rotation = int(step[1]) / 90
            while rotation >= 1:
                if facing == "north":
                    facing = "west"
                elif facing == "east":
                    facing = "north"
                elif facing == "west":
                    facing = "south"
                elif facing == "south":
                    facing = "east"
                rotation -= 1

    ns = (n - s) * -1
    we = (e - w) * -1
    if ns < 0:
        ns = ns * - 1
    if we < 0:
        we = we * - 1
    manhattan_distance = (ns + we)

    return manhattan_distance

def second_star(instruction_list):
    
    waypoint_n = 1
    waypoint_e = 10
    waypoint_w = 0
    waypoint_s = 0

    n = 0
    e = 0
    s = 0
    w = 0

    for step in instruction_list:

        if step[0] == "N":
            waypoint_n += int(step[1])
        if step[0] == "E":
            waypoint_e += int(step[1])
        if step[0] == "W":
            waypoint_w += int(step[1])
        if step[0] == "S":
            waypoint_s += int(step[1])
            
        if step[0] == "F":
            if waypoint_n > 0:
                n = n + waypoint_n * int(step[1])
            if waypoint_e > 0:
                e = e + waypoint_e * int(step[1])
            if waypoint_w > 0:
                w = w + waypoint_w * int(step[1])
            if waypoint_s > 0:
                s = s + waypoint_s * int(step[1])

        if step[0] == "R":
            dis = int(step[1]) / 90
            while dis >= 1:
                temp_n = waypoint_n
                temp_e = waypoint_e
                temp_w = waypoint_w
                temp_s = waypoint_s
                waypoint_n = temp_w
                waypoint_e = temp_n
                waypoint_s = temp_e
                waypoint_w = temp_s
                dis -= 1

        if step[0] == "L":
            dis = int(step[1]) / 90
            while dis >= 1:
                temp_n = waypoint_n
                temp_e = waypoint_e
                temp_w = waypoint_w
                temp_s = waypoint_s
                waypoint_n = temp_e
                waypoint_e = temp_s
                waypoint_s = temp_w
                waypoint_w = temp_n
                dis -= 1

        waypoint_n = waypoint_n - waypoint_s
        if waypoint_n < 0:
            waypoint_s = waypoint_n * -1
            waypoint_n = 0
        else:
            waypoint_s = 0
        waypoint_e = waypoint_e - waypoint_w
        if waypoint_e < 0:
            waypoint_w = waypoint_e * -1
            waypoint_e = 0
        else:
            waypoint_w = 0

    ns = (n - s) * -1
    we = (e - w) * -1
    if ns < 0:
        ns = ns * - 1
    if we < 0:
        we = we * - 1
    manhattan_distance = (ns + we)
    return manhattan_distance

# first star
print("First Star")
print("Answer: {}".format(first_star("east",input_list)))

# second star (too low 45017)
print("Second Star")
print("Answer: {}".format(second_star(input_list)))