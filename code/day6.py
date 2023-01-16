

with open('input/input6.txt', "r") as file:
    data = file.read().strip().split("\n")[0]


list = []
position = 0

for counter, char in enumerate(data):
    if char not in list:
        list.append(char)
    else:
        for i in range(len(list)):
            if char == list[i]:
                for j in range(i+1):
                    list.pop(0)
                list.append(char)
                break
    if len(list) == 14: #Part A: 4, Part B: 14
        position = counter+1
        break

print("Position of different consecutive letters: ", position)
