age=int(input("Enter your age : "))
if(age<=12):
    print("Price : $5")
elif age in range(13,60):
    print("Price : $10")
elif(age>=60):
    print("Price : $7")