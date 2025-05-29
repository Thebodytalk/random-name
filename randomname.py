import random

# Create lists for appending
first = []
last = []
firstSub = []
lastSub = []


choice = input("Would you like to select your initials? Type YES or NO: ")

with open("./firstname.txt", "r") as fileFirst:
    for line in fileFirst:
        first.append(line.strip())
        

with open("./lastname.txt", "r") as fileLast:
    for line in fileLast:
        last.append(line.strip())

if choice == 'NO' or choice == 'No' or choice == 'no':
    print(random.choice(first))
    print(random.choice(last))

elif choice == 'YES' or choice == 'Yes' or choice == 'yes':
    inputFirst = input("Initial of first name: ")
    inputLast = input("Initial of second name: ")

    for firsts in first:
        if firsts[0] == inputFirst:
            firstSub.append(firsts)

    for lasts in last:
        if lasts[0] == inputLast:
            lastSub.append(lasts)
            
    print(random.choice(firstSub))
    print(random.choice(lastSub))

else:
    print("Please restart program and make sure to type 'Yes' or 'NO'")



# i want to create maybe a sublist of items in the list that start with whichever letter the user inputs
# i guess i would check the first letter each string for each index and if it == true then add it to a secondary list.
# the only issue i see with this is having to iterate over the entire file which would be fine for this project
# but not the greatest for a bigger project

# 1. get input from user
# 2. read file and create list for first and last names
# 3. iterate through each list to check first letter to match user input
# 4. if user input == string[0] then append to listSub
# 5. random.choice via each subList and print solution