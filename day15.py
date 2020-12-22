nums = open('input.txt', 'r').readlines()

turn = []

for i in nums:
    for j in i.split(','):
        turn.append(int(j))

print(turn)

memory = {}

def solve(number):
    index = len(turn)-1
    for i in range(0, len(turn)-1):
        memory[turn[i]] = i
    while True:
        nr = turn[index]
        if nr not in memory:
            turn.append(0)
        else:
            turn.append(index-memory[nr])
        memory[nr] = index
        index += 1
        if index == number-1:
            return turn[index]


print("Part 1:", solve(2020))
print("Part 2:", solve(30000000)) # takes a bit more, 20-30s
