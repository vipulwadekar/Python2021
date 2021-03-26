#1)write a program to check user-entered number is palindrome or not 


# take input from the user
n=int (input("enter the number to check the given number is palindrome or not : "))
#initialize two variables
org=n
rev=0
#took out each digit from num and reverse that num
while (n<0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
#match with original number
if(rev == org):
    print("entered num is palindrome")
else:
    print("not palindrome")
