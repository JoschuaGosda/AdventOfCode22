from string import ascii_letters

with open('input/input3.txt', "r") as file:   
    data = [i for i in file.read().strip().split("\n")]

# part 1
points = 0

for rucksack in data:
    mid = len(rucksack)//2
    left = set(rucksack[:mid])
    right = set(rucksack[mid:])
    letter = left.intersection(right)

    for value, char in enumerate(ascii_letters):
        if char in letter:
            points += value+1

print("Part 1: Total number of points: " + str(points))

# part 2
sum = 0
for i in range(0, len(data), 3):
    rucksacks = data[i:i+3]
    for value, char in enumerate(ascii_letters):
        if char in rucksacks[0] and char in rucksacks[1] and char in rucksacks[2]:
            sum += value+1
    
print("Part2: Total number of points: " + str(sum))