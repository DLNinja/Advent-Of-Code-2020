coms = open('input.txt', 'r').readlines()
coms = [i.replace('\n', '') for i in coms]

coms = [i.split(' ') for i in coms]

commands = []

for _, x in coms:
    if x[0] == '+':
        x = int(x.replace('+', ''))
    elif x[0] == '-':
        x = -int(x.replace('-', ''))
    commands.append([_, x])


#print(coms)
#print(commands)

def part1():
    adapter = 0
    cnt = 0
    appeared = [0 for i in range(0, len(coms))]

    while appeared[cnt] == 0:
        appeared[cnt] = 1
        if commands[cnt][0] == "acc":
            adapter += commands[cnt][1]
            cnt += 1
        elif commands[cnt][0] == "jmp":
            cnt += commands[cnt][1]
        else:
            cnt += 1
        if cnt == len(commands):
            print("Part 2:", adapter)
            break

    return adapter


def part2():
    for x in range(0, len(commands)):
        if commands[x][0] == "acc":
            continue
        if commands[x][0] == "nop":
            commands[x][0] = "jmp"
            c = part1()
            commands[x][0] = "nop"
        else:
            commands[x][0] = "nop"
            c = part1()
            commands[x][0] = "jmp"


print("Part 1:", part1())
part2()