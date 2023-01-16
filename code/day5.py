
with open('input/input5.txt', "r") as file:
    data = [i for i in file.read().strip().split("\n")]

stacks = []
for i in range(9):
    stacks.append([])


def move(stacks, pop_from, push_to, num):
    stack_size = len(stacks[pop_from])
    for _ in range(num):
        # part A
        #item = stacks[pop_from].pop()
        # part B
        item = stacks[pop_from].pop(stack_size-num) 
        stacks[push_to].append(item)
    return stacks


for line in range(7, -1, -1):
    elements_line = data[line]
    for i in range(9):
        position = 1 + i*4
        if elements_line[position] != " ":
            stacks[i].append(elements_line[position])

for instruction in data[10:]:
    num, pop_from, push_to = [int(s) for s in instruction.split() if s.isdigit()]
    stacks = move(stacks, pop_from-1, push_to-1, num)

for stack in stacks:
    print(stack)