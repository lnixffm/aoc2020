#!/usr/bin/python

import sys
# day 6: questions

# Read Data
input_lst = []
group_list = []
fobj = open("input_day06_01.txt", "r")
lines = fobj.readlines() 
for line in lines:
    #print len(line)
    line = line.replace('\n','')
    if len(line) == 0:
        input_lst.append(group_list)
        group_list = []
    else:
        line = line.replace('\n','')
        group_list.append(line)

def first_star():
    questions_yes_count = []
    for group in input_lst:
        question_yes_list = []
        group_answer_yes_count_list = 0
        for person in group:
            for each_answer in person:
                if not each_answer in question_yes_list:
                    group_answer_yes_count_list += 1
                    question_yes_list.append(each_answer)
        questions_yes_count.append(group_answer_yes_count_list)
    
    total_yes = 0
    for groupanswer in questions_yes_count:
        total_yes = total_yes + groupanswer
    print("First Star")
    print("Total Yes: {}".format(total_yes))


def second_star():
    questions_yes_count = []
    for group in input_lst:
        #print group
        question_yes_list = []
        group_answer_yes_count_list = 0
        set_answer  = []
        for each_answer in group[0]:
            set_answer.append(each_answer)

        for person in group:
            #print person
            for each_answer in set_answer:
                #print set_answer
                if not each_answer in person:
                    set_answer.remove(each_answer)

        #print set_answer
        questions_yes_count.append(len(set_answer))

    total_yes = 0
    for groupanswer in questions_yes_count:
        total_yes = total_yes + groupanswer
    print("Second Star")
    print("Total Yes: {}".format(total_yes))


# first star
first_star()

#second star (3125)
second_star()
