def cal_sum(x,y):
    return x+y
def cal_sub(x,y):
    return x-y
def cal_mul(x,y):
    return x*y
def cal_div(x,y):
    return x/y
def cal_pow(x,y):
    return x**y

while True:
    

    print(''' 1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Nth Power of number\n6.Exit''')
    
    ch=int (input("Enter your wish number : "))
    
    if ch>=1 and ch<=5:
        x,y=[int(x) for x in (input("Enter the two value  sperated by space : ")).split(' ')]
        if ch==1:
            print(cal_sum(x,y))
        elif ch==2:
            print(cal_sub(x,y))
        elif ch==3:
            print(cal_mul(x,y))
        elif ch==4:
            print(cal_div(x,y))
        elif ch==5:
            print(cal_pow(x,y))
    elif ch<=0 or ch >=6 :
        str=input("Please confirm are you want to exit (YES/NO) : ")
        str=str.lower()
        if str=='yes':
            break #exit from loop
        else:
            continue
