#generated random values for list1 and list 2, then we are trying to find the common elements between the 2 lists

from random import *

list1 = [randint(1,10) for _ in range(5)]
list2 = [randint(1,10) for _ in range(5)]

print(list1)
print(list2)

common_elements=[]
for x in list1:
    if x in list2:
        common_elements.append(x)
    else:
        continue
    
print("Common elements in the lists: ",common_elements)

# 2nd Approach: We can convert the lists into sets and then find the intersection

from random import randint

list1 = [randint(1,10) for _ in range(5)]
list2 = [randint(1,10) for _ in range(5)]

list1 = set(list1)
list2 = set(list2)

print(list1)
print(list2)

print(list1.intersection(list2))

'''Note: Here you might find that the number of elements in the lists are not same.
That is because we are generating random numbers and if the randint() generates any duplicate value, it will be truncated as we are storing them in a set'''
