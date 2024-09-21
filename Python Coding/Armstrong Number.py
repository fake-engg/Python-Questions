from math import pow
num = int(input("Enter the number: "))
strr = str(num)
power = len(strr)

def armstrong(num):
    value = 0
    while num!=0:
        rem = num%10
        value += int(pow(rem,power))
        num = num//10
        
    return value    
  
if num == armstrong(num):
    print("{} is an Armstrong number".format(num))
else:
    print("{} is not Armstrong number".format(num))



