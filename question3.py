'''Write a program to check if a given year is a leap year or not. 
A year is a leap year if it is divisible by 4 but not divisible by 100 unless it is also divisible by 400. 
Display an appropriate message based on whether the given year is a leap year or not.'''

y=int(input("Enter year : "))
if(y%4==0 and y%100!=0 or y%400==0):
    print("Year is a leap year.")
else:
    print("Year is not a leap year.")
