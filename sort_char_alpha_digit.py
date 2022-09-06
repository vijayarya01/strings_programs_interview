# 6. Write a program to sort characters of the string, first alphabet symbols followed by digits.
str = input("enter your choice of random alphanumeric ")
#input : B4A3D1
#OUTPUT - ABD134
'''
# We have sorted function in python to do this task but this returns Digits followed by Alphabets in a list. i.e 123ABC
output = sorted(str)
print("This sorted function will return in list first digits then alphabets ", output)
# we can join and convert in string the list elements using join method

output = "".join(output)
print("using join method, the output is different from previous ", output)

# But this approach does not give us the expected output.We need Alphabets followed by digits.ie. ABD134
'''

alphabets = []
digits = []

for char in str:
    if char.isalpha(): # .isalpha function helps to find Alphabets in any string
        alphabets.append(char)
    else:
        digits.append(char)
print(alphabets)
print(digits)
print("sum of two unsorted lists " , alphabets + digits)
print("sum of two sorted list will look this but it will return comma separted value " , sorted(alphabets)+ sorted(digits))
print("sum of two sorted list with join method " ,''.join(sorted(alphabets)+ sorted(digits)))

