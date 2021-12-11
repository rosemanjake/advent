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

globalflash = []

def flash(arr, flashed):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            make_flash(arr, i, j, flashed)
    return

# We go clockwise
xoffsets = [-1, -1, 0, 1, 1, 1, 0, -1]
yoffsets = [0, 1, 1, 1, 0, -1, -1, -1]

def make_flash(arr, i , j, flashed):
    if (i,j) not in flashed:
        arr[i][j] += 1
        if arr[i][j] > 9:
            arr[i][j] = 0
            flashed.append((i,j))
            globalflash.append(1)
            # Loop around adjacent numbers
            for x in range(8):
                # Going clockwise, if each numer between 0 and the height/width of the overall 2d array
                if 0 <= i+yoffsets[x] < len(arr) and 0 <= j+xoffsets[x] < len(arr[i]):
                    if ([i+yoffsets[x]],{j+xoffsets[x]}) not in flashed:
                        make_flash(arr, i+yoffsets[x], j+xoffsets[x], flashed)

def check_sync(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] != 0:
                return False
    return True

def flash_cycle(arr, cycles):
    firstsync = "not found"
    for i in range(cycles):
        flashed = []
        flash(arr, flashed)
        if check_sync(arr) and firstsync == "not found":
            firstsync = i + 1
    return len(globalflash), firstsync

input = get_input("day11.txt")
arr = get_arr(input)
result = flash_cycle(arr, 300)

print(f"solution to part 1 = {result[0]}")
print(f"solution to part 2 = {result[1]}")