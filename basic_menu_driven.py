#! /usr/bin/python

"""
Menu driven program to perform following operations
1. Detect if a number is positive, negative or zero
2. Display a string characterwise
3. Get a tuple/list from user and print the sum of numbers
4. Get a tuple/list from user and print the average of numbers
5. Get a number between 1 to 100
6. Quit 
"""
def pnz():
    mynum = int(raw_input("Please enter a number:"))
    if(mynum == 0):
        print "ZERO"
    elif (mynum > 0):
        print "positive"
    else:
        print "negative"

def strchar():
    mystr = str(raw_input("Please enter your name :"))
    length = mystr.__len__()
    for i in range(length):
        print mystr[i]

def sum_tuple():
    nume_list = [0] * 5
    print "Enter few numbers: "
    count = 0
    sum = 0
    while(count < 5):
        nume_list[count] = int(raw_input("Next num: "))
        sum = sum + nume_list[count]
        count += 1
    print "Sum : %d" % (sum)

def ave_list():
    nume_list = [0] * 5
    print "Enter few numbers: "
    count = 0
    sum = 0
    while(count < 5):
        nume_list[count] = int(raw_input("Next num: "))
        sum = sum + nume_list[count]
        count += 1
    print "Average: %d" % float(sum/count)

def between():
    mynum = int(raw_input("Please Enter a num between 1 and 100:"))
    if(mynum > 1 and mynum < 100):
        print "Number between 1 and 100"
    else:
        print " Invalid Number"

if __name__ == '__main__':
    choice = 0
    while(choice != 6):
        choice = int(raw_input("Please enter a choice:"))
        if choice == 1:
                pnz()
        elif choice == 2:
            strchar()
            continue
        elif choice == 3:
            sum_tuple()
            continue
        elif choice == 4:
            ave_list()
            continue
        elif choice == 5:
            between()
            continue
        elif choice == 6:
            print "Bye Bye!"
            break






    
