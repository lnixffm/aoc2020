#!/usr/bin/python

from sets import Set

# day 4: check passports

# Read Data
input_lst = []
fobj = open("input_day04_01.txt", "r")
lines = fobj.readlines() 
dic_pass = {}
for line in lines:
    lst_pass = []
    line = line.replace('\n','')

    splitline = line.split(" ")
    for element in splitline:
        if ":" in element:
            dic_pass[element.split(":")[0]] = element.split(":")[1]

    # spitter for next pass
    if not ":" in line:
        input_lst.append(dic_pass)
        dic_pass = {}
    #  last pass of input
    if lines[-1] == line:
        input_lst.append(dic_pass)

#print(input_lst)


def first_star():
    count_valid = 0
    #North Pole Credentials
    count_npc = 0

    for scan in input_lst:
        
        # check all requirements without cid
        scan_requiremnts = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
        scan_requiremnts_count = 0
        for scan_requiremnt in scan_requiremnts:
            if scan_requiremnt in scan.keys():
                scan_requiremnts_count += 1

        # check all requirements with cid
        if scan_requiremnts_count == 7:
            # check cid for a valid pass or only a North Pole Credential
            if "cid" in scan.keys():
                count_valid += 1
            else:
                count_npc += 1

    # calculate all valid passes with the North Pole Credentials
    results = count_valid + count_npc

    print("FIRST STAR")
    print("Valid Passports: {}".format(count_valid))
    print("Valid North Pole Credentials: {}".format(count_valid))
    print("Valid Full Passports: {}".format(results))
    print(" ")
        
def second_star():
    count_valid = 0
    #North Pole Credentials
    count_npc = 0

    for scan in input_lst:
        
        # check all requirements without cid
        scan_requiremnts = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
        scan_requiremnts_count = 0
        for scan_requiremnt in scan_requiremnts:
            if scan_requiremnt in scan.keys():
                scan_requiremnts_count += 1

        # check now the details of all seven requirements
        scan_requiremnts_details_count = 0
        if scan_requiremnts_count == 7:
            #byr (Birth Year) - four digits; at least 1920 and at most 2002.
            if int(scan.get("byr")) >= 1920 and int(scan.get("byr")) <= 2002:
                scan_requiremnts_details_count += 1
            #iyr (Issue Year) - four digits; at least 2010 and at most 2020.
            if int(scan.get("iyr")) >= 2010 and int(scan.get("iyr")) <= 2020:
                scan_requiremnts_details_count += 1
            #eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
            if int(scan.get("eyr")) >= 2020 and int(scan.get("eyr")) <= 2030:
                scan_requiremnts_details_count += 1
            #hgt (Height) - a number followed by either cm or in:
            #If cm, the number must be at least 150 and at most 193.
            #If in, the number must be at least 59 and at most 76.
            if "cm" in scan.get("hgt"):
                if int(scan.get("hgt").replace("cm","")) >= 150 and int(scan.get("hgt").replace("cm","")) <= 193:
                    scan_requiremnts_details_count += 1
            elif "in" in scan.get("hgt"):
                if int(scan.get("hgt").replace("in","")) >= 59 and int(scan.get("hgt").replace("in","")) <= 76:
                    scan_requiremnts_details_count += 1
            #hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
            allowed_chars = Set('0123456789abcdef')
            if len(scan.get("hcl")) == 7 and scan.get("hcl").startswith('#'):
                if Set(scan.get("hcl")[1::]).issubset(allowed_chars):
                    scan_requiremnts_details_count += 1
            #ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
            eye_color_list = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            if scan.get("ecl") in eye_color_list:
                scan_requiremnts_details_count += 1
            #pid (Passport ID) - a nine-digit number, including leading zeroes.
            if len(scan.get("pid")) == 9 and int(scan.get("pid")):
                scan_requiremnts_details_count += 1

            # check all valid details
            if scan_requiremnts_details_count == 7:
                #cid (Country ID) - ignored, missing or not.
                if "cid" in scan.keys():
                    count_valid += 1
                else:
                    count_npc += 1

    # calculate all valid passes with the North Pole Credentials
    results = count_valid + count_npc

    print("SECOND STAR")
    print("Valid Passports: {}".format(count_valid))
    print("Valid North Pole Credentials: {}".format(count_valid))
    print("Valid Full Passports: {}".format(results))

        
# first star
first_star()

#second star
second_star()