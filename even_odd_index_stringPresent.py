# 5. Print Characters present at even and odd index separately for given string.
#Approach -1 _using while loop
str = "Durgasoft"
new_str_atEven = ''
new_str_atOdd = ''

i=0
print("Character present at even index ")# this return in new line all items
while i < len(str):
    # print(str[i])
    output = new_str_atEven + str[i]
    # print(output,end=' ')
    i = i +2
    # output = ''.join(output)
    print(output,end='')

i = 1
print("Character present at Odd index ") # this return in  new line
while i < len(str):
    print(str[i])
    i = i + 2

# Approach 2 - Using slicing operator

print("Character present at even index ", str[::2]) # this method return in Horizontal line



print("Character present at Odd index " , str[1::2])# this method return in Horizontal line
