'''Write a program that categorizes a person's age into different groups: "Child" (0-12 years), "Teenager" (13-19 years), 
"Adult" (20-59 years), and "Senior" (60 years and above). Ask the user to input their age and print the corresponding category.'''

age=int(input("Enter your age : "))
if age in range(0,13):
    print("Child")
elif age in range(13,20):
    print("Teenager")
elif age in range(20,60):
    print("Adult")
elif(age>=60):
    print("Senior")
