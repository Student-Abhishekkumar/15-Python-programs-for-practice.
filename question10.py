'''Given the two ages of a bride and a groom, your task is to determine whether they can marry each other 
according to the Indian Marriage Act. According to the Indian marriage act the groom should be at least 21 years old 
and the bride should be at least 18 years old.

If the bride and groom are old enough to get married according to the Indian Marriage Act, they can marry each other.
If they are not old enough according to the law they can't marry each other.'''

groom=int(input("Enter the age of groom : "))
bride=int(input("Enter the age of bride : "))

if(groom>=21 and bride>=10):
    print("You can marry.")
else:
    print("Sorry you are not aged.")
