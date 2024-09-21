"""Q. Given an array of integers, return indices of the two numbers such that they add up to a specific target.
Input: nums = [5, 2, 3], target = 8 Output: [0, 2]"""

l = eval(input("Enter the list: "))

#taking an empty list to store the indices values
listOfIndices = []
target = int(input("Enter the target: "))

#Logic implementation
for i in range(len(l)):
    for j in range(i,len(l)):
        if l[i]+l[j]==target:
            #tuple packing concept
            indices = i,j  
            # adding the tuples to the empty list
            listOfIndices.append(indices)

print(listOfIndices)

