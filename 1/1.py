lines = open('1/input.txt').readlines() 
# Part 1
print(sum(int(i) for i in lines))

# Part 2
seen = set()
ints = [int(i) for i in lines]
def step2(nums):
    sum = 0
    while True:
        for i in ints:
            sum += i
            if sum in seen:
                return sum
            else:
                seen.add(sum)

print(step2(ints))