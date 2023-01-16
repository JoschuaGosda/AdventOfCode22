
f = open('day2/input.txt', "r")
lines = f.readlines()

rounds = []


for x in lines:
    rounds.append(x.split('\n')[0])

f.close()


# A-B-C / X-Y-Z = rock, paper, scissors
outcomes = {
    "A X": 4, "A Y": 8, "A Z": 3,
    "B X": 1, "B Y": 5, "B Z": 9,
    "C X": 7, "C Y": 2, "C Z": 6
}

desired_outcomes = {
    "A X": 3, "A Y": 4, "A Z": 8,
    "B X": 1, "B Y": 5, "B Z": 9,
    "C X": 2, "C Y": 6, "C Z": 7
} 


total_score = 0
total_score2 = 0

for round in rounds:
    total_score += outcomes[round]
    total_score2 += desired_outcomes[round]




print("1) total number of points " + str(total_score))
print("2) total number of points " + str(total_score2))
