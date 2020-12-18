nums = open('input.txt', 'r').readlines()
bus = int([i.replace('\n', '') for i in nums][0])
nums = [i.replace('\n', '').split(',')for i in nums][1]

# part 2
buses = []
t = 0
for i in nums:
    if i != "x":
        buses.append([int(i), t])
    t += 1

print(buses)

nums = [int(i) for i in nums if i != "x"] # part 1


def part1():
    number = 0
    diff = 1000000000
    for i in nums:
        mod = bus % i
        if i - mod < diff:
            diff = i-mod
            number = i
    print(number*diff)


#part1()

def part2():
    t = 0
    step = 1
    for x, y in buses:
        while (t + y) % x != 0:
            t += step
        step *= x
    return t


print(part2())
