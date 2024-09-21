nterm = int(input("Enter the terms: "))

n1,n2 = 0,1
count=2           # as we have printed 2 terms beforehand

if nterm == 1:   
    print(n1)
elif nterm <=0:
    print("Enter the positive number!!")
else:
    print(n1)
    print(n2)
    while count<nterm:
        value = n1+n2
        print(value)
        n1,n2=n2,value
        count+=1
