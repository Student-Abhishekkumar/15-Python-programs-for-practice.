'''You are given a number, stored in a variable with the name num
For all numbers in the range of [1, num], including num, print the output according to the following conditions
•	If the current number, is divisible by both 2 and 3. i.e. num % 2 and num % 3 == 0 print “Both” (without quotes)
•	If the number is only divisible by 2. print 'Two', without quotes
•	If the number is only divisible by 3. print 'Three’ without quotes
•	Else, if the number is not divisible by both 2 and 3. Print ‘None’ without quotes.
Print all values on a new line.'''

num=float(input("Enter your number : "))
if(num%2==0 and num%3==0):
    print("\nBoth")
elif(num%2==0):
    print("\nTwo")
elif(num%3==0):
    print("\nThree")
else:
    print("\nNone")
