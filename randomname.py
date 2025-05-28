import random

first = []
last = []

with open("./firstname.txt", "r") as fileFirst:
    for line in fileFirst:
        first.append(line.strip())
        
    print(random.choice(first))

with open("./lastname.txt", "r") as fileLast:
    for line in fileLast:
        last.append(line.strip())

    print(random.choice(last))