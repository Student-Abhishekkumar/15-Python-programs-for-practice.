score=float(input("Enter your score : "))
if score in range(90,101):
    print("Grade A")
elif score in range(80,90):
    print("Grade B")
elif score in range(70,80):
    print("Grade C")
elif score in range(60,70):
    print("Grade D")
else:
    print("Grade F")