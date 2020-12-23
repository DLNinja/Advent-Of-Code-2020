with open("input.txt") as file:
    data = file.readlines()
    data = [line.strip() for line in data]

def get_initial_active_points(dimension):
    active = set()
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "#":
                if dimension == 3:
                    active.add((i, j, 0))
                else:
                    active.add((i, j, 0, 0))
    return active

# Part 1:


activePoints = get_initial_active_points(3)

for r in range(6):
    newActive = set()
    for x in range(-10-r, 10+r):
        for y in range(-10-r, 10+r):
            for z in range(-2-r, r+2):
                activeCnt = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        for k in range(-1, 2):
                            if not(i == 0 and k == 0 and j == 0):
                                if (x+i, y+j, z+k) in activePoints:
                                    activeCnt += 1
                if (x, y, z) in activePoints and 2 <= activeCnt <= 3:
                    newActive.add((x, y, z))
                if (x, y, z) not in activePoints and activeCnt == 3:
                    newActive.add((x, y, z))
    activePoints = newActive

print(len(activePoints))

# Part 2:

activePoints = get_initial_active_points(4) # fourth dimension, yayy

for r in range(6):
    newActive = set()
    for x in range(-10-r, 10+r):
        for y in range(-10-r, 10+r):
            for z in range(-2-r, r+2):
                for w in range(-2 - r, r + 2):
                    activeCnt = 0
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            for k in range(-1, 2):
                                for l in range(-1, 2):
                                    if not(i == 0 and j == 0 and k == 0 and l == 0):
                                        if (x+i, y+j, z+k, w+l) in activePoints:
                                            activeCnt += 1
                    if (x, y, z, w) in activePoints and 2 <= activeCnt <= 3:
                        newActive.add((x, y, z, w))
                    if (x, y, z, w) not in activePoints and activeCnt == 3:
                        newActive.add((x, y, z, w))
    activePoints = newActive

print(len(activePoints))

