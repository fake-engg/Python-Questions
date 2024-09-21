#check prime number

num = int(input("Enter the number: "))
factor =[]

if num ==1:
    print("{} is not a prime number".format(num))
elif num>1:
    for i in range(1,num+1):
        if num%i ==0:
            factor.append(i)
        
            
    if len(factor)>2:
        print("{} is not a prime number".format(num))
    else:
        print("{} is a prime number".format(num))
