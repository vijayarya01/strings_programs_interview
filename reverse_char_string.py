#. 1 Write a program to reverse given string ?
given_string = "reverseMe" # you can use input method as well to take real strings.

# Approach 1 - Using Slicing

reversed_string = given_string[::-1]
print("given string before revering is, ",given_string)
print("given string after revering is, ",reversed_string)

# Approach 2 - reversed method

reversed_string_2 = reversed(given_string)

print("reveresed() method return this, ", reversed_string_2) #returns object location in memory
# we need to use join to get the expected output of reversed string
output = "".join(reversed_string_2) # join without space.
print("given string after revering using reversed method is , ",output)

#approach 3- (while -loop)
input_strin = input("Enter your strings which you want to reverse: ")
output_while = "" # created empty string
i = len(input_strin) -1
while i>=0:
    output_while = output_while + input_strin[i]
    i = i-1
print("using while loop reversed string is ",output_while)
