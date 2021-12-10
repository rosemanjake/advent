import os
import statistics

def get_input(file):
    f = open(f"{os.path.dirname(__file__)}\\{file}", "r")
    return f.read()

def get_badchars(line):
    stack = []
    for char in line:
        if char in brackets.keys():
            stack.append(char)
        if char in brackets.values():
            if char != brackets[stack[len(stack) -1]]:
                return char
            else:
                close = stack.pop()
    return stack

def part1(lines):
    badchars = []
    for line in lines:
        badchars.append(get_badchars(line))

    total = 0
    for char in [char for char in badchars if not type(char) == list]:
        if char == ")":
            total = total + 3
        if char == "]":
            total = total + 57
        if char == "}":
            total = total + 1197
        if char == ">":
            total = total + 25137
    
    return total

def part2(lines):
    incomplete = []
    for line in lines:
        incomplete.append(get_badchars(line))
    
    incomplete = [stack for stack in incomplete if type(stack) == list]

    completes = []
    for stack in incomplete:
        complete = []
        for char in stack:
            complete.append(brackets[char])
        complete.reverse()
        completes.append(complete)

    scoredict = {
        ")":1,
        "]":2,
        "}":3,
        ">":4,
    }
    
    scores = []
    for complete in completes:
        score = 0
        for char in complete:
            score = score * 5
            score = score + scoredict[char]
        scores.append(score)

    return statistics.median(scores)

brackets = {
    "(":")",
    "[":"]",
    "{":"}",
    "<":">"
}

input = get_input("day10.txt")
lines = input.split("\n")
print(f"Solution for part 1 = {part1(lines)}")
print(f"Solution for part 2 = {part2(lines)}")