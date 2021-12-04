
import os

# Read file
def get_input(file):
    f = open(f"{os.path.dirname(__file__)}\\{file}", "r")
    return f.read()

# Split file into list of numbers
def get_measures(file):
    strs = file.split("\n")
    return [int(str) for str in strs]

# Part 1
def part1(measures):
    return len([measures[i] for i in range(len(measures)) if i > 0 and measures[i] > measures[i - 1]])

# Part 2
def part2(measures):
    sums = []
    for i in range(len(measures)):
        if i <= len(measures) - 3:
            sums.append(measures[i] + measures[i + 1] + measures[i + 2])
        if i == len(measures) - 2:
            sums.append(measures[i] + measures[i + 1])
        if i == len(measures) - 1:
            sums.append(measures[i])

    return len([sums[i] for i in range(len(sums)) if i > 0 and sums[i] > sums[i - 1]])

input = get_input("day1.txt")
measures = get_measures(input)
print(f"Solution to part 1 = {part1(measures)}")
print(f"Solution to part 2 = {part2(measures)}")
