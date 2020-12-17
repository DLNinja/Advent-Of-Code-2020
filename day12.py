instructions = open('input.txt', 'r').readlines()
instructions = [[i[0], int(i.replace('\n', '')[1:])] for i in instructions]

directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]

print(instructions)

def part1():
    x = y = 0
    dirr = 3
    for letter, dist in instructions:
        if letter == "N":
            x -= dist
        elif letter == "S":
            x += dist
        elif letter == "E":
            y += dist
        elif letter == "W":
            y -= dist
        elif letter == "L":
            degree = dist//90
            dirr += degree
            dirr %= 4
        elif letter == "R":
            degree = dist//90
            dirr -= degree
            if dirr < 0:
                dirr = 4 + dirr
        else:
            x += directions[dirr][0] * dist
            y += directions[dirr][1] * dist
    return abs(x) + abs(y)


print(part1())

def part2():
    ship_x = ship_y = 0
    wp_x = -1
    wp_y = 10
    dirr = 3
    for letter, dist in instructions:
        if letter == "N":
            wp_x -= dist
        elif letter == "S":
            wp_x += dist
        elif letter == "E":
            wp_y += dist
        elif letter == "W":
            wp_y -= dist
        elif letter == "L":
            wp_x, wp_y = rotate(wp_x, wp_y, dist, "L")
        elif letter == "R":
            wp_x, wp_y = rotate(wp_x, wp_y, dist, "R")
        else:
            ship_x += wp_x * dist
            ship_y += wp_y * dist
    return abs(ship_x) + abs(ship_y)

def rotate(wp_x, wp_y, degree, direction):
    if direction == "R":
        degree = 360 - degree

    if degree == 90:
        helper = wp_x
        wp_x = -1 * wp_y
        wp_y = +1 * helper
    elif degree == 180:
        wp_x = -1 * wp_x
        wp_y = -1 * wp_y
    elif degree == 270:
        helper = wp_x
        wp_x = +1 * wp_y
        wp_y = -1 * helper

    return wp_x, wp_y


print(part2())
