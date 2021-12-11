import os

def get_input(file):
    f = open(f"{os.path.dirname(__file__)}\\{file}", "r")
    return f.read()

def get_arr(input):
    arr = input.split("\n")
    final = []
    for line in arr:
        final.append([int(num) for num in line])
    return final

def get_neighbours(arr):
    neighbours = []
    coords = []
    # For each line
    for i in range(len(arr)):
        neighbourmap = {}
        coordmap = {}
        # For cell in line
        for j in range(len(arr[i])):
            upcell = "null"
            upleftcell = "null"
            upcell = "null"
            uprightcell = "null"
            rightcell = "null"
            downrightcell = "null"
            downcell = "null"
            downleftcell = "null"
            leftcell = "null"
            upcoord = "null"
            upleftcoord = "null"
            upcoord = "null"
            uprightcoord = "null"
            rightcoord = "null"
            downrightcoord = "null"
            downcoord = "null"
            downleftcoord = "null"
            leftcoord = "null"

            cell = arr[i][j]
            if i > 0:
                upcell = arr[i - 1][j]
                upcoord = f"{i - 1},{j}"
                if j > 0:
                    upleftcell = arr[i - 1][j - 1]
                    upleftcoord = f"{i - 1},{j - 1}"
                if j < len(arr[i]) - 1:
                    uprightcell = arr[i - 1][j + 1]
                    uprightcoord = f"{i - 1},{j + 1}"
            if i < len(arr) - 1:
                downcell = arr[i + 1][j]
                downcoord = f"{i + 1},{j}"
                if j > 0:
                    downleftcell = arr[i + 1][j - 1]
                    downleftcoord = f"{i + 1},{j - 1}"
                if j < len(arr[i]) - 1:
                    downrightcell = arr[i + 1][j + 1]
                    downrightcoord = f"{i + 1},{j + 1}"
            if j > 0:
                leftcell = arr[i][j - 1]
                leftcoord = f"{i},{j - 1}"
            if j < len(arr[i]) - 1:
                rightcell = arr[i][j + 1]
                rightcoord = f"{i},{j + 1}"
            neighbourmap[f"{i},{j}"] = [upleftcell, upcell, uprightcell, rightcell, downrightcell, downcell, downleftcell, leftcell]
            mycoords = [upleftcoord, upcoord, uprightcoord, rightcoord, downrightcoord, downcoord, downleftcoord, leftcoord]
            coordmap[f"{i},{j}"] = [coord for coord in mycoords if not coord == "null"]
            if i == 50 and j == 20:
                print("hi")
        neighbours.append(neighbourmap)
        coords.append(coordmap)

    finalcoords = {}
    for line in coords:
        for cell in line:
            finalcoords[cell] = line[cell]

    return neighbours, finalcoords

globalflash = []

def flash(neighbours, arr, flashed):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            make_flash(arr, i, j, neighbours, flashed)
    return

def make_flash(arr, i , j, neighbours, flashed):
    if f"{i},{j}" not in flashed:
        arr[i][j] += 1
        if arr[i][j] > 9:
            arr[i][j] = 0
            flashed.append(f"{i},{j}")
            globalflash.append(1)
            for neighbour in neighbours[f"{i},{j}"]:
                splits = neighbour.split(",")
                y = int(splits[0])
                x = int(splits[1])
                if neighbour not in flashed:
                    make_flash(arr, y, x, neighbours, flashed)

def check_sync(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] != 0:
                return False
    return True

def flash_cycle(neighbours, arr, cycles):
    firstsync = "not found"
    for i in range(cycles):
        flashed = []
        flash(neighbours, arr, flashed)
        if check_sync(arr) and firstsync == "not found":
            firstsync = i + 1
    return len(globalflash), firstsync

input = get_input("day11.txt")
arr = get_arr(input)
content = get_neighbours(arr)
neighbours = content[1]
result = flash_cycle(neighbours, arr, 300)

print(f"solution to part 1 = {result[0]}")
print(f"solution to part 2 = {result[1]}")