num=float(input("Enter your number : "))
if(num%2==0 and num%3==0):
    print("\nBoth")
elif(num%2==0):
    print("\nTwo")
elif(num%3==0):
    print("\nThree")
else:
    print("\nNone")