# 7. write a program for the following requirements ?
#1. input  = a4b3c2 #2. input  - d2u8i9 # 3. input  != 2b4d5f  ''' input 3 is invalid for this program
#ouput = aaaabbbcc

str = input("Enter the strings: ") # if your input is different from the format of this program's logic, it will error.
output = '' # empty string , will add output here
for char in str:
    if char.isalpha():
        x = char
    else:
        d = int(char)
        output = output + (x * d)
        # output = output + x * char # TypeError: can't multiply sequence by non-int of type 'str'
print("We have printed alphabets as many as times the digits were presented in input,",str)
print("We have printed alphabets as many as times the digits were presented in input, thus ouput is :",output)
print(" Note: this program is not sorting the output , check next program for the same.")

