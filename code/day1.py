
food_list = []
food = 0

f = open('day1/CalorieCounting.txt', 'r')

while True:

    # Get next line from file
    line = f.readline()
    
    # if at the end of file
    if not line:
        break

    if line != '\n':
        food += int(line)
    else:
        food_list.append(food)
        food = 0

f.close()


print("Reindeer carrying the most calories: #"  + str(max(food_list)))

food_list.sort()
top3 = sum(food_list[-3:])

print("Calories of the top 3 reindeers: #" + str(top3))
