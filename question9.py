#slicing

s=input("Enter your word : ")
s1=s[::-1]

if(s==s1):
    print("Palindrome.",s1)
else:
    print("Not palindrome.",s1)