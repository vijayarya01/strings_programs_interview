# 11. Write a program to remove duplicate characters from the given input string ?
# input - AZZBCDABBCDABBCCDDEEF  # OUTPUT - AZBCDEF NOTE: OUTPUT IS NOT SORTED. IT IS AS IT IS IN INPUT.

# APPROACH 1
input_str = "ZZBCDABBCDABBCCDDEEFEFFBBCDDA"
output = ''

for char in input_str: # loop in to check each char
    if char not in output: # if char is not present in output, which is already empty at first, then add it.
        output = output + char
print("The given input with duplicate is ", input_str)
print("After removing duplicates, output has unique characters only,", output)
print(" Note : the output is not sorted , it provides the characters as it in input string. ")

# Approach 2 - using list
my_list = []
for char in input_str: # loop in to check each char
    if char not in my_list: # if char is not present in output, which is already empty at first, then add it.
        my_list.append(char) # add the unique char in empty list above
        output_list = "".join(my_list) # join comma separated value
print("The given input with duplicate is ", input_str)
print("After removing duplicates, list has unique characters only,", output_list)
print(" Note : the output is not sorted , it provides the characters as it in input string. ")

# Approach - 3 Using sets
# well, sets only contain unique values
my_set = set(input_str) # set return unordered values , each time order will change when you run this.
output_set = "".join(my_set)
print("The given input with duplicate is ", input_str)
print("After removing duplicates, set has unique characters only but unordered,", output_set) # output 1. FZDABEC 2. AZFCEDB
