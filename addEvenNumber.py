def addEvenNumber(*x):
    
    print("we concluded that x is tuple : ",x)
    sum=0
    print("Even No : ",end="")
    for i in x:
        if i%2==0:
            sum=sum+i
            print(i,end=" ")
    return sum
#main program
total=addEvenNumber(1,2,3,4,5,6,7,8,9,10)
print("\n",type(total))
print(total)
