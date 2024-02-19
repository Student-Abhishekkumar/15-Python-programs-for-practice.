'''Write a program that takes a student's score as input and prints out their corresponding grade. 
If the score is above or equal to 90, the grade is an 'A'. If it's between 80 and 89, the grade is 'B'. 
If it's between 70 and 79, the grade is 'C'. If it's between 60 and 69, the grade is 'D'. 
Otherwise, the grade is 'F'.'''

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
