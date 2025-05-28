import random

# with open("./practice.txt", "r") as file:
    # for line in file:
        # print(line.strip())
        # test = [line.strip()]

    # print('list')
    # print(test[0])
    # print(test[1])
    # print(test[2])

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