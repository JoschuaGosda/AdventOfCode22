
with open('input/input4.txt', "r") as file:
    teams = [i for i in file.read().strip().split("\n")]

print(teams)

def cleaningArea(interval):
    start_end = interval.split("-")
    return set(range(int(start_end[0]), int(start_end[1])+1))


sum = 0
sum2 = 0

for team in teams:
    area1 = cleaningArea(team.split(",")[0])
    area2 = cleaningArea(team.split(",")[1])
    # part 1
    if area1.issuperset(area2) or area2.issuperset(area1):
        sum += 1
    # part 2
    if len(area1.intersection(area2)) > 0:
        sum2 += 1

print("Part 1) Number of identical cleaning areas within teams:", sum)
print("Part 2) Number of overlapping cleaning areas within teams:", sum2)
