import itertools

lines = open('2/input.txt').read().splitlines()
# Part 1
twos = 0
threes = 0

def check_2s_and_3s(line):
    has_twos = False
    has_threes = False
    for char in set(line): # for each unique character
        occurrences = line.count(char)
        if occurrences == 2:
            has_twos = True
        elif occurrences == 3:
            has_threes = True
    return (has_twos, has_threes)

for line in lines:
    has_twos, has_threes = check_2s_and_3s(line)
    if has_twos:
        twos += 1
    if has_threes:
        threes += 1

print(twos * threes)

# Part 2
def number_of_differences(line_a, line_b):
    differences = 0
    for idx, letter in enumerate(line_a):
        if letter != line_b[idx]:
            differences += 1
    return differences

def find_similar_lines(lines):
    for a, b in itertools.combinations(lines, 2):
        if number_of_differences(a, b) == 1:
            return (a,b)

line_a, line_b = find_similar_lines(lines)

word = ""
for idx, letter in enumerate(line_a):
    if line_b[idx] == letter:
        word = word + letter

print(word)