mat = open('input.txt', 'r').readlines()
mat = [[j for j in i.replace('\n', '')] for i in mat]

direction = [[1, 1], [-1, -1], [1, -1], [-1, 1], [0, 1], [0, -1], [1, 0], [-1, 0]]

def in_bound(i, j):
    if 0 <= i < len(mat) and 0 <= j < len(mat[0]):
        return True
    return False


def part1(table):
    matt = table
    while True:
        new = []
        for i in range(0, len(matt)):
            line = []
            for j in range(0, len(matt[i])):
                if matt[i][j] == ".":
                    line.append(".")
                    continue
                count = 0
                for x, y in direction:
                    if in_bound(i+x, j+y):
                        if matt[i+x][j+y] == "#":
                            count += 1
                if matt[i][j] == "L" and count == 0:
                    line.append("#")
                elif matt[i][j] == "#" and count >= 4:
                    line.append("L")
                else:
                    line.append(matt[i][j])
            new.append(line)
        if new == matt:
            return sum(i.count("#") for i in new)
        matt = new

def part2(table):
    matt = table
    while True:
        new = []
        for i in range(0, len(matt)):
            line = []
            for j in range(0, len(matt[i])):
                if matt[i][j] == ".":
                    line.append(".")
                    continue
                count = visible_seats(matt, i, j)
                if matt[i][j] == "L" and count == 0:
                    line.append("#")
                elif matt[i][j] == "#" and count >= 5:
                    line.append("L")
                else:
                    line.append(matt[i][j])
            new.append(line)
        if new == matt:
            return sum(i.count("#") for i in new)
        matt = new

def visible_seats(table, i, j):
    cnt = 0
    for x, y in direction:
        k = 1
        while in_bound(i + k*x, j + k*y):
            if table[i + k*x][j + k*y] != ".":
                if table[i + k*x][j + k*y] == "#":
                    cnt += 1
                break
            k += 1

    return cnt


print(part2(mat))
