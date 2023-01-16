
with open('input/input10.txt', "r") as file:
    data = file.read().strip().split('\n')

cycle = 0
instr = 0
reg = 1
exec = False
mult = 20
sum = 0
string = ''

while instr < len(data):
    cycle += 1

    # Part A
    if cycle in [20, 60, 100, 140, 180, 220]:
        sum += mult*reg
        mult+= 40

    # Part B
    if (cycle-1 )%40 in [reg-1, reg, reg+1]:
        string += '#'
    else:
        string += '.'
    if (cycle % 40) == 0:
        string += '\n'

    if data[instr] == 'noop':
        instr += 1
    else:
        if  not exec:
            exec = True
        else:
            reg += int(data[instr].split(" ")[1])
            instr += 1
            exec = False

print("Part A) total sum: ", sum)
print("Part B)")
print(string)
