#!/usr/bin/python
import sys
# day 15: Game

input_list = [19,20,14,0,9,1]

def find_n(game_list):
    sn = game_list[-1]
    f = 0
    c = 1
    for n in game_list[::-1]:
        if n == sn:
            f += 1
        if f == 2:
            a = len(game_list) - c + 1
            return a
        c += 1


def first_star():
    game_list = input_list
    while len(game_list) != 2020:
        last_number = game_list[-1]
        if game_list.count(last_number) == 1:
            spoken = 0
            game_list.append(spoken)
        else:
            spoken = int(len(game_list)) - int(find_n(game_list))
            game_list.append(spoken)   
    return game_list[-1]   

def second_star():
    input_list = [19,20,14,0,9,1]
    dict = {}
    for x in input_list:
        dict[x] = input_list.index(x) + 1

    turn = len(input_list)
    last_number = input_list[-1]

    while turn < 30000000:
        if last_number not in dict.keys():
            spoken = 0
        else:
            spoken = turn - dict[last_number]
        dict[last_number] = turn
        turn += 1
        last_number = spoken

    return spoken



# first star
print("First Star")
print("Answer: {}".format(first_star()))

# second star
print("Second Star")
print("Answer: {}".format(second_star()))

