def reverseNum(num):
    num1 = str(num)
    reversed_num = ''
    for x in num1:
        reversed_num = x + reversed_num
    return reversed_num
    

num = int(input("Enter the integer: "))
print("Reversed of the interger is: ",reverseNum(num))

#if we want to return an integer value
#print("Reversed of the interger is: ",int(reverseNum(num)))
