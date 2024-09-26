# Remove duplicate elements from a list while maintaining the order

def noDups(list):
    no_duplicate = []
    for x in list:
        if x in no_duplicate:
            continue
        else:
            no_duplicate.append(x)
    return no_duplicate
    
list = eval(input("Enter the list: "))

print("List without duplicates: ")
print(noDups(list))
