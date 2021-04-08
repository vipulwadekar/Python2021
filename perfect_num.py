import math 
def perfect_no():
    c=0
#outer loop for input 
    for num in range(1,10001):
        x=int(num/2)
        sum=0
        
        #inner loop for factor
        for i in range(1, x+1):
            #finding factor
            if (num % i) == 0:
                sum+=i;
        if sum==num:
            c=c+1;
            print(num,"is perfect number",)

    print("Total perfect no in this range is : ",c)       

#main program
perfect_no()
    
