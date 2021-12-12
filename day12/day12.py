import os
import re
import copy

def get_input(file):
    f = open(f"{os.path.dirname(__file__)}\\{file}", "r")
    return f.read()

def get_adjacent(input):
    arr = input.split("\n")
    final = {}
    for line in arr:
        nodes = line.split("-")
        for i in range(len(nodes)):
            j = 1
            if i == 1:
                j = 0
            if nodes[i] in final:
                final[nodes[i]].append(nodes[j])
            else:
                final[nodes[i]] = [nodes[j]]
    return final

def dfs(graph, node, currpath, paths, part):
    if node == "end":
        #print(", ".join(currpath))
        return 1

    paths = 0
  
    for neighbour in graph[node]:
        if part == 1 and (neighbour not in currpath or re.search("^[A-Z]*$", neighbour)):  
            paths += dfs(graph, neighbour, currpath + [neighbour], paths, part)
        if part == 2:
            counter = {}
            for v in currpath:
                if re.search("^[a-z]*$", v) and v not in ["start", "end"]:
                    if v in counter :
                        counter[v] += 1
                    else:
                        counter[v] = 1
            forbiddenlower = []
            special = ""
            for v in counter:
                if counter[v] == 2:
                    special = v
                    forbiddenlower.append(special)
            for v in counter:
                if counter[v] == 1 and special != "" and v not in forbiddenlower:
                    forbiddenlower.append(v)
                

            if (neighbour in counter and neighbour not in forbiddenlower) or neighbour not in currpath or re.search("^[A-Z]*$", neighbour):
                paths += dfs(graph, neighbour, currpath + [neighbour], paths, part)
    return paths

input = get_input("day12.txt")
adjacent = get_adjacent(input)

print(f"Solution to part 1 = {dfs(adjacent, 'start', ['start'], 0, 1)}")
print(f"Solution to part 2 = {dfs(adjacent, 'start', ['start'], 0, 2)}")