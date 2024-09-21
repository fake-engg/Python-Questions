#Using reverse and join methods

str = input("Enter the string: ")

#converting string into a list
stringList = list(str)

#reverse the list elements
stringList.reverse()
print(stringList)

# join the list elements to form a string
reverseString = ''.join(stringList)
print(reverseString)


#Using concatenation

def reverse(s):
  str = ''
#logic to reverse a string using concatenation method
  for i in s:
    str = i + str
  return str

s = input("Enter the String: ")
reverseStr = reverse(s)

print("Reverse of the String: ",reverseStr)


#Using Recursion

#recursive function to reverse the string
def reverse(s):
  if len(s)==0:
    return s
  else:
    return reverse(s[1:]) + s{[0]

s = input("Original String: ")
print("Reverse of the String is: ",reverse(s))
                              
                            
                            
                              
