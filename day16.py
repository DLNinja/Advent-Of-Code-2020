nums = open('input.txt', 'r').readlines()
nums = [i.replace('\n', '') for i in nums]

# Data preprocessing
myticket = ""
parameters = []
tickets = []

for i in nums:
    if i == "":
        nums.remove(i)

mod = 1
for i in nums:
    if i == "your ticket:":
        mod = 2
        continue
    if i == "nearby tickets:":
        mod = 3
        continue
    if mod == 1:
        line = i.split(': ')[1]
        line = line.split(" or ")[0] + "-" + line.split(" or ")[1]
        line = [int(x) for x in line.split("-")]
        line.append(i.split(': ')[0])
        parameters.append(line)
    elif mod == 2:
        myticket = [int(x) for x in i.split(',')]
        print(myticket)
    else:
        tickets.append([int(x) for x in i.split(',')])


def part1(array):
    sum = 0
    for i in array:
        for x in i:
            cnt = 0
            if valid(x):
                cnt = 1
            if cnt == 0:
                sum += x
    return sum

def valid(x):
    return any(j[0] <= x <= j[1] or j[2] <= x <= j[3] for j in parameters)


print("Part 1:", part1(tickets))
#print("Part 2:", part2())

