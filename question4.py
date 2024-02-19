age=int(input("Enter your age : "))
if age in range(0,13):
    print("Child")
elif age in range(13,20):
    print("Teenager")
elif age in range(20,60):
    print("Adult")
elif(age>=60):
    print("Senior")