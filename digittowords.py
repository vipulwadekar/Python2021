#enter a any number like : 456  o/p: Four Five Six
def numberTostring(no):
    switcher={
        0:"Zero",
        1:"One",
        2:"Two",
        3:"Three",
        4:"Four",
        5:"Five",
        6:"Six",
        7:"Seven",
        8:"Eight",
        9:"Nine", }
    return switcher.get(no,False)

#break number into single digit
def singleDigit(arg):
    rev=0
    rem=0
    list=[]
    while arg>0:
        rem=arg%10
        #after breaking number into single digit passing number to convert it into words
        #after getting in the form of words,i added that words into list
        if numberTostring(rem) ==False:
            pass
        else:
            list.append(numberTostring(rem))
        arg=arg//10
        #finding length here of list
    length=(len(list))
        #i used pop method and print 
    for i in range(1,length+1):
        print(list.pop(),end=" ")
         
#main program
#ask user for input
arg=int(input("Enter any number : "))

#passing argument as interget  to function singleDigit
singleDigit(arg)


