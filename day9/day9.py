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
                #if j > 0:
                    #upleftcell = arr[i - 1][j - 1]
                    #upleftcoord = f"{i - 1},{j - 1}"
                #if j < len(arr[i]) - 1:
                    #uprightcell = arr[i - 1][j + 1]
                    #uprightcoord = f"{i - 1},{j + 1}"
            if i < len(arr) - 1:
                downcell = arr[i + 1][j]
                downcoord = f"{i + 1},{j}"
                #if j > 0:
                    #downleftcell = arr[i + 1][j - 1]
                    #downleftcoord = f"{i + 1},{j - 1}"
                #if j < len(arr[i]) - 1:
                    #downrightcell = arr[i + 1][j + 1]
                    #downrightcoord = f"{i + 1},{j + 1}"
            if j > 0:
                leftcell = arr[i][j - 1]
                leftcoord = f"{i},{j - 1}"
            if j < len(arr[i]) - 1:
                rightcell = arr[i][j + 1]
                rightcoord = f"{i},{j + 1}"
            neighbourmap[f"{i},{j}"] = [cell, upleftcell, upcell, uprightcell, rightcell, downrightcell, downcell, downleftcell, leftcell]
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

def get_low_points(neighbours):
    lowpoints = []
    for line in neighbours:
        for cell in line.keys():
            height = line[cell][0]
            line[cell].pop(0)
            nums = [num for num in line[cell] if not num == "null"]
            if min(nums) > height:
                lowpoints.append(cell)
    return lowpoints

def get_risk(lowpoints, arr):
    risklevels = []
    for point in lowpoints:
        coords = point.split(",")
        height = arr[int(coords[0])][int(coords[1])]
        risk = height + 1
        risklevels.append(risk)
    return sum(risklevels)      

visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


def dfs_basin(visited, graph, node, allnodes):
    basinmap = {}
    if node not in visited:
        visited.add(node)
        for neighbour in graph[node]:
            currcoords = node.split(",")
            currheight = arr[int(currcoords[0])][int(currcoords[1])]
            neighcoords = neighbour.split(",")
            neighheight = arr[int(neighcoords[0])][int(neighcoords[1])]
            #basinmap[node] = [node]
            allnodes.append(node)
            if neighheight >= currheight and not neighheight == 9:
                allnodes.append(neighbour)
                if node in basinmap.keys():
                    basinmap[node].append(neighbour)
                else:
                    basinmap[node] = [neighbour]
                dfs_basin(visited, graph, neighbour, allnodes)
    return list(set(allnodes))
           

def get_basins(low_points, coords):
    basins = {}
    for low in low_points:
        basins[low] = dfs_basin(visited, coords, low, [])
    
    finals = [len(val) for val in basins.values()]
    finalfinal = sorted((finals), reverse=True)[:3]
    result = 1
    for x in finalfinal:
        result = result * x

    return result

input = get_input("day9.txt")
arr = get_arr(input)
neighbours_and_coords = get_neighbours(arr)
neighbours = neighbours_and_coords[0]
coords = neighbours_and_coords[1]
low_points = get_low_points(neighbours)
risk = get_risk(low_points, arr)

print(f"solution to part 1 = {risk}")
print(f"solution to part 2 = {get_basins(low_points,coords)}")