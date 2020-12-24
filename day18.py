ecuations = [line.replace('\n', '') for line in open("input.txt").readlines()]
ecuations = [line.replace(' ', '') for line in ecuations]
ans = 0

# Part 1: Recursively

def solve(ecuation, index):
    if ecuation[index] == '(':
        result, index = solve(ecuation, index+1)
    else:
        result = int(ecuation[index])
    index += 1
    while index < len(ecuation):
        if ecuation[index] == ')':
            break
        operator = ecuation[index]
        index += 1
        #print(ecuation[index])
        if ecuation[index] == '(':
            nr, index = solve(ecuation, index+1)
        else:
            nr = int(ecuation[index])
        if operator == "*":
            result *= nr
        else:
            result += nr
        index += 1
    return result, index


for ec in ecuations:
    res, _ = solve(ec, 0)
    ans += res

print(ans)

