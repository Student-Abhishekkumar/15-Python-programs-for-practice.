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
        