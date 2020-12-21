nums = open('input.txt', 'r').readlines()
nums = [i.replace('\n', ' ') for i in nums]

mask = ""

def part1():
    memory = {}
    for i in nums:
        if "mask" in i:
            mask = i.split(" = ")[1]
        else:
            index = int((i.split('[')[1].split(']'))[0])
            number = int(i.split(' = ')[1])
            number = bin(number)[2:]
            while len(number) + 1 < len(mask):
                number = "0" + number
            nr = ""
            for j in range(0, len(mask)):
                if mask[j] == "X":
                    nr += number[j]
                else:
                    nr += mask[j]
            memory[index] = int(nr, 2)
    return sum(memory[y] for y in memory)


#print(part1())

# def adresses(index, s, nr):
#     if index < len(nr):
#         line = []
#         if nr[index] == "X":
#             f
#             line.append(s+"0")
#             line.append(s+)
#         else:

def part2():
    memory = {}
    for i in nums:
        if "mask" in i:
            mask = i.split(" = ")[1]
            mask = mask[:-1]
        else:
            index = int((i.split('[')[1].split(']'))[0])
            number = int(i.split(' = ')[1])
            adress = int(i.split(' = ')[1])
            number = bin(index)[2:]
            while len(number) != len(mask):
                number = "0" + number
            nr = ""
            for j in range(0, len(number)):
                if mask[j] == "X":
                    nr += "X"
                else:
                    a = max(mask[j], number[j])
                    nr += str(a)
            strings = [""]
            for j in range(0, len(nr)):
                line = []
                for s in strings:
                    if nr[j] == "X":
                        line.append(s+"0")
                        line.append(s+"1")
                    else:
                        line.append(s+nr[j])
                strings = line

            for j in strings:
                memory[int(j, 2)] = adress

    return sum(memory[y] for y in memory)


print("Part 1:", part1())
print("Part 2:", part2())
