#WAP to find the first non-repeating character in a string and also return its index

str = input("Enter the string: ")

for i in range(len(str)+1):
    if str[i] not in str[i+1:]:
        print("First non-repeating character is:",str[i])
        print("Index of non-repeating character is:",i)
        break
    else:
        continue
