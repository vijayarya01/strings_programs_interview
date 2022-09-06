# 9.  Write a program for the following requirements ?
# 1. input - aaaabbbccz # 1. output - 4a3b2c1z this does not count character if placed at random index.

input_str = "ABBACBA"


previous = input_str[0]
# print(previous)
output = ''
count = 1 # this is a counter variable which will help us to count the number of occurrences of alphabets
index = 1 # it is set to 1 because index 0 value is assigned to previous variable

while index < len(input_str): # index = 9, len of string = 10
    if input_str[index] == previous:
        count = count + 1
    else:
        output = output + str(count) + previous
        previous = input_str[index]
        count = 1
    if index == len(input_str) -1: # to add last character of string in the output
        output = output + str(count) + previous
    index = index + 1
print("The given input string is as follows:", input_str)
print("The count of alphabets in given string is as follows:", output)


