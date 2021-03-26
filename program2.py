#write a program to print number between 1 to 100 divide by 3 and 7
#take range from user
n=int (input("Enter the range "))
#using for loop
print("using for loop")
for i in range(1,(n+1)):#start =1 ,stop=(n+1) - 1 =(101-1=100),step=inc by 1
    if(i%3==0 and i%7==0):
        print("{} is perfeclty divisble by 3 and 7".format(i))

#using while loop
print("using while loop")
i=1
while i<=n:#start =1 till 100
    if(i%3==0 and i%7==0):
        print("{} is perfeclty divisble by 3 and 7".format(i))
    i+=1    
