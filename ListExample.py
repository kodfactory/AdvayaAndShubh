# 4. Types of collections

# 1. List
# 2. Tuple
# 3. Set
# 4. Dictionary

########################################
#            List Collection           #
########################################

# listA = [1,2,3,4,5,6]

# for i in listA:
#     print(i)

# if 4 in listA:
#     print("Number exist")
# else:
#     print("Number does not exist")

# listA[0:4] = ["Jayesh", "Advaya", "Shubh", "Vivaan"]


# print(listA)

#print(type(listA))

# add/append new item into existing list
# remove the existing item from the list
# change / update existing item into list
# find the length of the list
# indexing / slicing in list
# check item is exist or not

# listA.append(10)

# listA.remove(3)

# listA[3] = "New value"

# print(len(listA))

# print(listA)

# print(listA[0:3])

# Merge the 2 list

# listA = [1,2,3]
# listB = [4,5,6]

# print(listA + listB)

listA = [1,2,3,3,3,4,4,4,4,4,5,5,5,5,5,6,6,7,7,8,8,8,9,9,9,9]

listB = []

for i in listA:
    if i not in listB:
        listB.append(i)
    
print(listB)

# Write a program to find the score of String

# What is score?
# If the total number of vowels in string are even then score = 2
# If the total number of vowels in string are odd then score = 1

# Jayesh - total 2 vowels -> Score 2
# Shubh - total 1 vowel -> Score 1
# Advaya - total 3 vowels -> Score 1

# ['a', 'e','i', 'o', 'u']

