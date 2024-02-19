'''1.	You're writing a program to provide clothing suggestions based on the temperature entered by the user.<br> 
   If the temperature is below 10 degrees Celsius, the program should suggest wearing a coat. \n 
   If it's between 10 and 20 degrees Celsius, it should suggest a sweater. Otherwise, it should suggest a T-shirt. \n
   Write the Python code for this scenario.'''

t=int(input("Enter your temperature : "))
if(t<10):
    print("Wear a coat.")
elif(t>=10 and t<20):
    print("wear a sweater.")
else:
    print("Wear a t-shirt.")
