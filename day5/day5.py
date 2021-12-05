import os
import re

def get_input(file):
    f = open(f"{os.path.dirname(__file__)}\\{file}", "r")
    return f.read()

def get_coords(text):
    arr = text.split("\n")
    arr = [re.findall("[\d]{2,3}", line) for line in arr]
    final = []
    for line in arr:
        final.append([int(s) for s in line])

    return final

def get_lines(coords, part):
    lines = []
    for line in coords:
        lines.append(draw_full_line(line, part))

    return [line for line in lines if not line == "diagonal" and not line == "point"]
    
def draw_full_line(nums, part):
    startx = nums[0]
    starty = nums[1]
    endx = nums[2]
    endy = nums[3]

    xsteps = abs(startx-endx)
    ysteps = abs(starty-endy)

    if xsteps == 0 and ysteps == 0:
        return nums
    elif xsteps == 0 or ysteps == 0:
        type = "straight"
    else: 
        type = "diagonal"
    
    if type == "diagonal" and part == "1":
        return "diagonal"

    currx = startx
    curry = starty

    x_increment = 0
    y_increment = 0

    if currx > endx:
        x_increment = -1
    elif currx < endx:
        x_increment = 1 
    if curry > endy:
        y_increment = -1
    elif curry < endy:
        y_increment = 1 

    line = []
    line.append([startx, starty])
    xstep_count = 0
    ystep_count = 0

    while not (xstep_count == xsteps and ystep_count == ysteps):      
        if not xstep_count == xsteps:
            currx += x_increment         
            xstep_count += 1
        
        if not ystep_count == ysteps:
            curry += y_increment         
            ystep_count += 1

        line.append([currx, curry])  

    return line

def get_crosses(lines):
    counter = {}
    for line in lines:
        for coord in line:
            s = f"{coord[0]}, {coord[1]}"
            if s not in counter.keys():
                counter[s] = 1
            elif s in counter.keys():
                counter[s] += 1
    
    return [coord for coord in counter.keys() if counter[coord] > 1]

text = get_input("day5.txt")
coords = get_coords(text)
part_1_lines = get_lines(coords, "1")
part_2_lines = get_lines(coords, "2")
crosses_part_1 = get_crosses(part_1_lines)
crosses_part_2 = get_crosses(part_2_lines)

print(f"Solution for part 1 = {len(crosses_part_1)}")
print(f"Solution for part 2 = {len(crosses_part_2)}")