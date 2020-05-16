# health management system
import  datetime
def gettime():
    return str(datetime.datetime.now())
#When Take function will get call This one for logging the values of clients
def Take(a):
    if a==1:
        D = int(input("Press 1 for exersise and 2 for food:  "))
        if D==1:
            Value= input("Type Here\n")
            with open("Harryex.txt","a") as op:
                op.write(gettime()+' ' +Value)
                print("Entered Successfully")

        elif D==2:
            Value = input("Type Here\n")
            with open("Harryfoo.txt", "a") as op:
                op.write(gettime()+' '+Value)
                print("Entered Successfully")
    elif a==2:
        D = int(input("Press 1 for exersise and 2 for food:  "))
        if D == 1:
            Value = input("Type Here\n")
            with open("Rohanex.txt", "a") as op:
                op.write(gettime()+' '+Value)
                print("Entered Successfully")

        elif D == 2:
            Value = input("Type Here\n")
            with open("Rohanfoo.txt", "a") as op:
                op.write(gettime() + ' ' + Value)
                print("Entered Successfully")
    elif a==3:
        D = int(input("Press 1 for exersise and 2 for food:  "))
        if D == 1:
            Value = input("Type Here\n")
            with open("Hammadex.txt", "a") as op:
                op.write(gettime() + ' ' + Value)
                print("Entered Successfully")

        elif D == 2:
            Value= input("Type Here\n")
            with open("Hammadfoo.txt", "a") as op:
                op.write(gettime() + ' ' + Value)
                print("Entered Successfully")
    else:
        print("Kindly enter the right choice ex(1-Harry,2-Rohan,3-Hammad): ")

#When Retrieve function will get call, This one for retrieving the values of clients
def Retrieve(b):
    if b==1:
        Value = int(input("Press 1 for exercise and 2 for food: "))
        if Value == 1:
            with open("Harryex.txt") as op:
                for content in op:
                    print(content, end="")
        elif Value == 2:
            with open("Harryfoo.txt") as op:
                for content in op:
                    print(content, end="")
    elif b==2:
        Value = int(input("Press 1 for exercise and 2 for food: "))
        if Value == 1:
            with open("Rohanex.txt") as op:
                for content in op:
                    print(content, end="")
        elif Value == 2:
            with open("Rohanfoo.txt") as op:
                for content in op:
                    print(content, end="")
    elif b==3:
        Value = int(input("Press 1 for exercise and 2 for food: "))
        if Value == 1:
            with open("Hammadex.txt") as op:
                for content in op:
                    print(content, end="")
        elif Value == 2:
            with open("Hammadfoo.txt") as op:
                for content in op:
                    print(content, end="")
    else:
        print("Kindly enter the right choice ex(1-Harry,2-Rohan,3-Hammad): ")


# Taking the input from the user
A = int(input("Press 1 for log the value and 2 for retrieve: "))
if A==1:
    B = int(input("Press 1 for Herry, 2 for Rohan, 3 for Hammad: "))
    Take(B)
else:
    C = int(input("Press 1 for Herry, 2 for Rohan, 3 for Hammad: "))
    Retrieve(C)