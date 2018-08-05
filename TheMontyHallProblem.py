import random

# A program that simulate the solution of The Monty Hall Problem

sampleSize = input("Sample Size = ")    # set sample size
count = 0

while (not sampleSize.isdigit() or int(sampleSize) <= 0):   # check if the sample size is an integer and larger than 0
    print("Sample Size must be an integer and larger than 0")
    sampleSize = input("Sample Size = ")

for x in range(int(sampleSize)):
    door = []
    carPosition = random.randint(0,2)   # determine the door that hidden a car
    playerChoice = random.randint(0,2)  # determine the door that players choose

    for y in range(3):                  # place objects into the door
        if y == carPosition:
            door.append("Car")
        else:
            door.append("Goat")

    hostOpen = [0, 1, 2]                # initialize host's options
    hostOpen.remove(playerChoice)       # remove the door that player choose from host's option
    for y in range(2):
        if door[hostOpen[y]] == "Car":  # remove the door that hidden a car from host's option
            hostOpen.remove(hostOpen[y])
            break
    playerChoice = 3 - playerChoice - hostOpen[0]   # players change their choice
    if playerChoice == carPosition:     # count the amount of players win the car
        count += 1

print("Win rate of changing choice: " + str(count/int(sampleSize)*100))        # calculate the win rate and print it