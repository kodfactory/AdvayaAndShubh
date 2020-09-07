# marks

# Grade A : If the marks are greater then 80
# Grade B : If marks are between 60 & 80
# Grade C : If marks are between 35 & 60
# Fail : If marks are less then 35

# Python is interpreted language

def getGradesBasedOnMarks(mymarks):
    if mymarks >= 80:
        print ("A Grade")

    elif 60 <= mymarks < 80:
        print ("B Grade")

    elif 35 <= mymarks < 60:
        print ("C Grade")

    else:
        print ("Failed")

mymarks = int(input("Enter your marks: "))

getGradesBasedOnMarks(mymarks)



    
