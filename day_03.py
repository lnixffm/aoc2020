#!/usr/bin/python

# day 3: check trees

# Read Data
input_lst = []
fobj = open("input_day03_01.txt", "r")
lines = fobj.readlines() 
for line in lines:
    line = line.replace('\n','')
    position_lst = []
    for eachposition in line:
        position_lst.append(eachposition)
    input_lst.append(position_lst)

def star(slope_right,slote_down):
    tree_count = 0

    position_slope_right = slope_right
    position_slote_down = slote_down

    while int(position_slote_down) < int(len(input_lst)):

        # check tree
        if '#' in input_lst[position_slote_down][position_slope_right]:
            tree_count += 1

        # go right
        position_slope_right += slope_right
        if int(position_slope_right) >= int(len(input_lst[position_slote_down])):
            position_slope_right = position_slope_right - len(input_lst[position_slote_down])

        # go down
        position_slote_down += slote_down

    return(tree_count)


# first star
trees = star(3,1)
print("First Star:{}".format(trees))

#second star
slope_lst = [(1,1),(3,1),(5,1),(7,1),(1,2)]
all_trees = 1
for slope in slope_lst:
    trees = star(slope[0],slope[1])
    all_trees = trees * all_trees
print("Second Star:{}".format(all_trees))