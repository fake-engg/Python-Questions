num = int(input("Enter the number: "))
factorial = 1
if num == 0 or num ==1:
    print("Factorial is: ",factorial)
else:
    for x in range(num,0,-1):
        factorial = factorial * x
    print("Factorial is: ",factorial)
