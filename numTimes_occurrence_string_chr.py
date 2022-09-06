#12. write a program to count the occurrences of each character in a given string ?
# input - ABBCABDCCC - output - a-2,b-3,c-4,D-1

# Approach -1 using list
input_str = "ABXXEeBCABDCCC"
my_list = []

for char in input_str:
    if char not  in my_list:
        my_list.append(char)

# for char in my_list:  # this return unsorted list in output
#     print('{} occurs {} times'.format(char,input_str.count(char))) # using count method here to count number of char in string
#

for char in sorted(my_list):  # this return unsorted list in output
    print('{} occurs {} times'.format(char,input_str.count(char))) # using count method here to count number of char in string


# Approach -2 using set

input_str_set = "bEaEAABBXTT"
my_set = set(input_str_set)

for char in sorted(my_set):
    print('{} occurs {} times'.format(char, input_str_set.count(char))) # using count method here to count number of char in string


# Approach - 3 using loops and without inbuilt -count method of python -- We can use Dictionary to count the occurrences
#Concept
dict = {} # empty dictionary
dict['A'] = 100 # first value of key- A
dict['P'] = 200 # first value of key - B
dict['A']  = 300 # update value of key- A, this will replace when we print dict.
print(dict)
print(dict.get('A')) # this will fetch the value of existing key- A i.e 300
print(dict.get('Z',0)) # we  specified a default value for a key whose value was not in dictionary, this return 0

dict["A"] = dict.get("A",0) + 100  # first it checked whether key- A exits or not, if yes, it will get that value and
# add further to it. now updated value of key- A becomes 400, and when you print it, this returns 400 ie updated value
print(dict['A'])

dict['K'] = 500
print(dict) # updated dic has items in it.

for key, value in dict.items(): # you can add sorted(dict.items()), this returns the sorted dictionary when you print.
    print("The unsorted dictionary :", key, value)

for key, value in sorted(dict.items()): # you can add sorted(dict.items()), this returns the sorted dictionary when you print.
    print("The sorted dictionary :", key,value)

# main program using dictionary

input_string = "AABBCDDD"
diction = {}

for char in input_string:
    diction[char] = diction.get(char,0) + 1
print("The count of characters in string using dictionary is ",diction)

print(" Note:Displayed values without showing dictionary below,which were shown above with it")

output_digit_alpha = '' # putting no of occurrence in a string
output_alpha_digit = ''

for key, value in sorted(diction.items()):  #used sorted function to get output in sorted manner
    print("{} occurs {} times ".format(key,value))
    output_digit_alpha = output_digit_alpha + str(value) + key
    output_alpha_digit = output_alpha_digit + key + str(value)
print("The count of characters in string using dictionary in the string format(digit_alphabet) is like this ", output_digit_alpha)
print("The count of characters in string using dictionary in the string format(alphabet_digit) is like this ", output_alpha_digit)
