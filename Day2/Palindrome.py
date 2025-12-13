num=int(input("enter number :"))
original=num
rev=0
while num > 0:
    digit=num%10
    rev=rev*10+digit
    num//=10
print("The reverse number is:",rev)
if original==rev:
    print("The number is palindrome")
else:
    print("The number is not Palindrome")

