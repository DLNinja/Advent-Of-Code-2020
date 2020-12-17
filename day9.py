nums = open('input.txt', 'r').readlines()
nums = [int(i.replace('\n', '')) for i in nums]

print(nums)

def part1():
    for k in range(25, len(nums)):
        x = nums[k]
        has = 0
        for i in range(1, 26):
            for j in range(0, 26):
                if x - nums[k-i] == nums[k-j]:
                    has = 1

        if has == 0:
            return x

    return 0


ans1 = part1()
print(ans1)

def part2():
    for i in range(0, len(nums)):
        if nums[i] != ans1:
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                if sum > ans1:
                    break
                elif sum == ans1:
                    return (i, j)


first, last = part2()
print(first, last)
mi = 1000000000000
ma = 0
for i in range(first, last+1):
    ma = max(ma, nums[i])
    mi = min(mi, nums[i])

print(mi + ma)

