import os

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

def part1(input):
    lines = input.split("\n")

    badchars = []
    for line in lines:
        badchars.append(get_badchars(line))

    total = 0
    for char in [char for char in badchars if not None]:
        if char == ")":
            total = total + 3
        if char == "]":
            total = total + 57
        if char == "}":
            total = total + 1197
        if char == ">":
            total = total + 25137
    
    return total

brackets = {
    "(":")",
    "[":"]",
    "{":"}",
    "<":">"
}

input = get_input("day10.txt")
score = part1(input)
print(score)