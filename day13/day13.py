import os
import re
import copy
import math

def get_input(file):
    f = open(f"{os.path.dirname(__file__)}\\{file}", "r")
    text = f.read()
    lines = text.split("\n")
    instructions = []
    coords = []
    for line in lines:
        if "fold along" in line:
            instructions.append(line)
        elif line != "":
            splits = line.split(",")
            coords.append((int(splits[0]), int(splits[1])))
    return instructions, coords

def get_array(coords):
    arr = []
    xvals = [int(coords[0]) for coords in coords]
    yvals =  [int(coords[1]) for coords in coords]

    h = max(yvals)
    w = max(xvals)

    for i in range(h + 1):
        arr.append([])

    for line in arr:
        for i in range(w + 1):
            line.append(0)

    for i in range(len(xvals)):
        x = xvals[i]
        y = yvals[i]

        arr[y][x] = 1

    return arr

def get_folded(arr, instructions):
    type = ""
    axis = 0
    folded = arr
    for instruction in instructions:
        order = re.search("[yx]=[\d]{1,}",instruction)[0]
        if "y" in order:
            type = "y"
        elif "x" in order:
            type = "x"
        axis = int(re.search("[\d]{1,}",order)[0])
        print(type, axis)
        folded = fold(folded,type, axis)

        if len(folded)<30:
            for line in folded:
                strline = [str(i) for i in line]
                txt = re.sub("1","#","".join(strline))
                txt = re.sub("0","_",txt)
                print(txt)

    return folded

def fold(newarr, type, axis):

    if type == "y":
        firsthalf = []
        secondhalf = []
        looprange = range(len(newarr))
        i = 0
        while i in looprange:
            if len(newarr)%2 == 0:
                newarr.remove(newarr[axis])
                looprange = range(len(newarr))
            if i < axis and i in range(int(len(newarr) / 2)):
                firsthalf.append(newarr[i])
            elif i > axis and i in range(int(len(newarr) / 2)):
                secondhalf.append(newarr[i]) 
            i += 1
            

        final = get_table(len(firsthalf[0]), len(firsthalf))
        
        secondhalf.reverse()
        for y in range(len(final)):
            for x in range(len(final[0])):
                if firsthalf[y][x] != 0:
                    final[y][x] = 1
                if secondhalf[y][x] != 0:
                    final[y][x] = 1
    
    elif type == "x":

        # if int(((len(newarr[0]) - 1) / 2)) % 2 == 0:
        #     for line in newarr:
        #         line.remove(line[axis])
        #     final = get_table(int(((len(newarr[0])) / 2)), len(newarr))   
        # else:
        final = get_table(int(((len(newarr[0])) / 2)), len(newarr)) 

        if axis == 40:
            print("hi")

        firsthalf = copy.deepcopy(final)
        secondhalf = copy.deepcopy(final)
        for y in range(len(newarr)):
            for x in range(len(newarr[0])):
                if x < axis:
                    firsthalf[y][x] = newarr[y][x]
                elif x > axis:
                    secondhalf[y][x - (len(firsthalf[0]) + 1)] = newarr[y][x]
    
        for line in secondhalf:
            line.reverse()
        count = 0
        counted = []
        for y in range(len(final)):
            for x in range(len(final[0])):
                if firsthalf[y][x] != 0: #and (y,x) not in counted:
                    final[y][x] = 1
                    count += 1
                    #counted.append((y,x))
                if secondhalf[y][x] != 0: #and (y,x) not in counted:
                    final[y][x] = 1
                    count += 1
                    #counted.append((y,x))
    return final

def get_table(x, y):
    new = []

    for i in range(y):
        new.append([])

    for line in new:
        for i in range(x):
            line.append(0)

    return new


input = get_input("day13.txt")
arr = get_array(input[1])
folded = get_folded(arr, input[0])

