str = input("Enter the string: ")
dict={}

for x in str:
    if x not in dict:
        dict[x] = 1 
        #dict[x] = dict.get(x,1)       --if we don't want to hardcode. this line will give 1 when the key is not present in the dict
    else:
        dict[x] = dict.get(x) + 1

print(dict)
