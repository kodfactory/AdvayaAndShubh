# Functions: Group of statements, which we can call and reuse
# as many times as possible

# Function defination
# def getNameAndConvertToUpperCase(name):
#     # Logic / group of statements
#     print(name.lower())


# # Function call
# getNameAndConvertToUpperCase("Advaya")

# getNameAndConvertToUpperCase("Shubh")

# getNameAndConvertToUpperCase("Jayesh")


# 1. Required argument

# def greetings(firstname, lastname):
#     print("Welcome",firstname, lastname)

# greetings("Shubh", "Menon")

# 2. Keyword argument

# def greetings(age, firstname, lastname):
#     print("Firstname: ", firstname)
#     print("Lastname: ", lastname)
#     print("Age: ", age)

# greetings(lastname="Menon", firstname="Shubh", age=21)

# 3. Variable length argument

# def displayStudentNames(*names):
#     print(names[0:3])

# displayStudentNames("Shubh", "Advaya", "Jayesh", "Dhyey", "Vivaan")

# 4. Default argument

def getStudentInfo(name, age=10):
    print(f"your name is {name} and age is {age}")

getStudentInfo("Shubh", 7)

