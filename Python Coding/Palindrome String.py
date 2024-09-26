#Write a Python function to check if a string is a palindrome.

str = input("Enter the string: ")

'''
if str == str[::-1]:
    print("'{}' is a palindrome".format(str))
else:
    print("'{}' is not a palindrome".format(str))
'''

rev_str = ''

for x in str:
    rev_str = x + rev_str

print(rev_str)
if str == rev_str:
    print("'{}' is a palindrome".format(str))
else:
    print("'{}' is not a palindrome".format(str))
    
