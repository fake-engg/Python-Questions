#To find the number of steps needed to reduce a number to 0. When it is odd, then substract 1 and when it is even, divide it by 2.

num = int(input("Enter the number: "))

step = 0

while num != 0:
    if num %2 ==0:
        num = num//2
        step+=1
    else:
        num-=1
        step+=1

print(step)
