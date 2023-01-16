
import numpy as np

with open('input/input8.txt', "r") as file:
    forest = file.read().strip().split('\n')

grid = [list(map(int, list(line))) for line in forest]
grid = np.array(grid)
n, m = np.shape(grid)
print(grid)

counter = 0

for i in range(n): # rows
    for j in range(m): # cols
        tree = grid[i, j]
        # look west
        if j == 0 or np.amax(grid[i, :j]) < tree:
            counter += 1
        # look east
        elif j == m-1 or np.amax(grid[i, (j+1):]) < tree:
            counter += 1
        # look north
        elif i == 0 or np.amax(grid[:i, j]) < tree:
            counter += 1
        # look south
        elif i == n-1 or np.amax(grid[(i+1):, j]) < tree:
            counter += 1

max_score = 0
x = 0
y = 0

for i in range(1, n-1):
    for j in range(1, m-1):
        tree = grid[i, j]
        tree_score = 1
        y = 0
        while(1):
            y += 1
            if grid[i-y, j] >= tree or i-y == 0:
                tree_score *= y
                break
        y = 0
        while(1):
            y+= 1
            if grid[i+y, j] >= tree or i+y == n-1:
                tree_score *= y
                break
        x = 0
        while(1):
            x += 1
            if grid[i, j-x] >= tree or j-x == 0:
                tree_score *= x
                break
        x = 0
        while(1):
            x += 1
            if grid[i, j+x] >= tree or j+x == m-1:
                tree_score *= x
                break
        if tree_score > max_score:
            max_score = tree_score
        

            



print("Number of visible trees", counter)
print("Maximal viewing score", max_score)


