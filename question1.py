'''yor're writing to provide clothing suggestion based on the temperatured entered by user.
if the temperature is below 10 degrees celcius, the program should suggest wearing a coat.'''

t=int(input("Enter your temperature : "))
if(t<10):
    print("Wear a coat.")
elif(t>=10 and t<20):
    print("wear a sweater.")
else:
    print("Wear a t-shirt.")