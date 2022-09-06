# 10. Write a program for the following requirements:
# 1. input - a4k3b2 @ output is -- aeknbd (Add 4 to a, 3 to k, 2 to b)

# how to check uni-code of alphabets, every language support it, using inbuilt function we can find value
print("unicode value of a is ", ord('a')) # return unicode value of a
print("unicode value of A is",ord('A')) # return unicode value of A

print("unicode value of 97 is ",chr(97)) # return unicode Alphabet value i.e a
print("unicode value of 65 is ",chr(65)) # A

# Main program logic here:

input_str = "a4k3b2"
output = ""

for char in input_str:
    if char.isalpha(): # checks if char is alphabet or not .. inbuilt function of python
        output = output + char
        x = char # save current char in variable x so that can be used in making new character
    else:
        d = int(char) # casting a string to integer
        new_char = chr(ord(x) + d) # adding ordinals value and then casting to character using chr() function
        output = output + new_char
print("Following is the result of given input string", output)