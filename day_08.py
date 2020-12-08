#!/usr/bin/python

# day 8: Accumulator

# Read Data
input_list = []
fobj = open("input_day08_01.txt", "r")
lines = fobj.readlines() 
for line in lines:
    line = line.replace('\n','')
    input_list.append((line.split(" ")[0], (line.split(" ")[1])))

#print(input_list)

def first_star():
    accumulator = 0
    position = 0
    lst_positions = []

    while not position in lst_positions:
        program_step = input_list[position]
        lst_positions.append(position)

        #print program_step

        if program_step[0] == 'nop':
            position += 1
        elif program_step[0] == 'acc':
            position += 1
            accumulator = accumulator + int(program_step[1].replace("+",""))
        elif program_step[0] == 'jmp':
            position = position + int(program_step[1].replace("+",""))

    return accumulator


def second_star():

    repaired_lst = input_list

    index_lst = []
    while True:

        accumulator = 0
        position = 0
        lst_positions = []
        while not position in lst_positions:
            program_step = repaired_lst[position]
            lst_positions.append(position)

            #print program_step
            if program_step[0] == 'nop':
                position += 1
            elif program_step[0] == 'acc':
                position += 1
                accumulator = accumulator + int(program_step[1].replace("+",""))
            elif program_step[0] == 'jmp':
                position = position + int(program_step[1].replace("+",""))

            if position == len(repaired_lst):
                return accumulator
        
        index = 0
        schalter = "on"
        repaired_lst = []
        for step in input_list:
            if schalter == "on":
                if not index in index_lst:
                    if step[0] == "jmp":
                        step = ("nop",step[1])
                        schalter = "off"
                index_lst.append(index)
                index += 1
            repaired_lst.append(step)

        if input_list == repaired_lst:
            return

# first star
first_star()
print("First Star")
print("Total Accumulator: {}".format(first_star()))

# second star
print("Second Star")
print("Total Accumulator: {}".format(second_star()))
