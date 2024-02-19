'''You're writing a program for a cinema that calculates the ticket price based on the age of the customer.
For customers aged 12 or below, the ticket price is $5. For customers aged between 13 and 59, the ticket price is $10. 
For customers aged 60 and above, the ticket price is $7. 
Write the code to calculate the ticket price based on the age entered by the user.'''

age=int(input("Enter your age : "))
if(age<=12):
    print("Price : $5")
elif age in range(13,60):
    print("Price : $10")
elif(age>=60):
    print("Price : $7")
