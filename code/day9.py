import numpy as np
from copy import deepcopy

with open('input/input9.txt', "r") as file:
    data = file.read().strip().split('\n')


map = {'U': 0, 'R': 1, 'D': 2, 'L': 3}
move = np.array([[1, 0], [0,1], [-1, 0], [0, -1]]) # up, right, down, left

head = np.array([0, 0]) # y,x
tail = np.array([0, 0])
count = 1
hist = [np.array([0, 0])]



for line in data:
    c, n = line.split(' ')
    i = map[c]
    for j in range(int(n)):
        head += move[i]
        dif = head-tail
        if np.amax(np.abs(dif)) > 1: 
            # tail must follow
            
            if np.amin(np.abs(dif)) == 0:
                # straight up, right, down or left
                tail += move[i]
            else:
                # diagonal movement
                if dif[0] > 0 and dif[1] > 0: # upper right
                    tail += move[map['U']] + move[map['R']]
                elif dif[0] < 0 and dif[1] > 0: # bottom right
                    tail += move[map['D']] + move[map['R']]
                elif dif[0] < 0 and dif[1] < 0: # bottom left
                    tail += move[map['D']] + move[map['L']]
                else:   # top left
                    tail += move[map['U']] + move[map['L']]

            if not np.any(np.all(tail == hist, axis=1)):
                hist.append(deepcopy(tail))
                count += 1

print("Number of position that tail vistited at least once", count)

################################################################
""" map = {'U': 0, 'R': 1, 'D': 2, 'L': 3}
m = np.array([[1, 0], [0,1], [-1, 0], [0, -1]]) # up, right, down, left

head = np.array([0, 0]) # y,x
tail = np.array([0, 0])
count = 1
hist = [np.array([0, 0])]
positions = [np.array([0, 0]) for _ in range(10)]

def move(head, tail, c, i):
    global map, m
    dif = head-tail
    if np.amax(np.abs(dif)) > 1: 
        # tail must follow
        if np.amin(np.abs(dif)) == 0:
            # straight up, right, down or left
            tail += m[i]
        else:
            # diagonal movement
            if dif[0] > 0 and dif[1] > 0: # upper right
                tail += m[map['U']] + m[map['R']]
            elif dif[0] < 0 and dif[1] > 0: # bottom right
                tail += m[map['D']] + m[map['R']]
            elif dif[0] < 0 and dif[1] < 0: # bottom left
                tail += m[map['D']] + m[map['L']]
            else:   # top left
                tail += m[map['U']] + m[map['L']]
    return tail

for line in data:
    c, n = line.split(' ')
    i = map[c]
    for j in range(int(n)):
        head += m[i]
        positions[0] = head
        for p in range(1, len(positions)):
            positions[p] = move(positions[p-1], positions[p], c, i)
        
        tail = positions[-1]
        if not np.any(np.all(tail == hist, axis=1)):
            hist.append(deepcopy(tail))
            count += 1

for position in positions:
    print(position)
print("Number of position that tail vistited at least once", count) """





def solve(v):
    visited = {(0, 0)}
    rope = numpy.zeros((v, 2))

    for move in data:
        d, length = move.split()

        for _ in range(int(length)):
            # move head
            rope[0] += {
                'L': (0, -1), 'R': (0, 1),
                'U': (1, 0), 'D': (-1, 0)
            }[d]

            # move tail
            for i in range(1, len(rope)):
                diff = rope[i - 1] - rope[i]

                if numpy.linalg.norm(diff) >= 2:
                    rope[i] += numpy.sign(diff)

            visited.add(tuple(rope[len(rope) - 1]))

    return len(visited)


print('Part 1:', solve(2))
print('Part 2:', solve(10))