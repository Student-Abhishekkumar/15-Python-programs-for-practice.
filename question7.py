'''You are given five numbers, stored in the variables with the following names
one, two, three, four, five
Find the value of sum1 and sum2, such that
sum1 = one + two
sum2 =  three +  four
If the value of both sum1 and sum2 is greater than the value stored in variable five, print Yes, else print No.'''

one=int(input("Enter your number one : "))
two=int(input("Enter your number two : "))
three=int(input("Enter your number three: "))
four=int(input("Enter your number four: "))

def menu():
    print("\n......Menu.....")
    print("\n\t1. Sum1")
    print("\t2. Sum2")
    print("\t3. Exit")

while True:
    try:
        menu()
        choice=int(input("Enter your choice : "))
        if(choice==1):
            print(one+two)
        elif(choice==2):
            print(three+four)
        elif(choice==3):
            break
        else:
            print("INVALD CHOICE")
    except:
        print("INVALD CHOICE")
        
