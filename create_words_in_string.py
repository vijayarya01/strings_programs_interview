# 15. Write a program for following requirement:

str_1 = 'abcdefg'
str_2 = 'xyz'
str_3 = '12345'

#output = ax1, by2, cz3, d4, e5, f, g

i = j = k = 0 # set index of each string to 0

while i < len(str_1) or j < len(str_2) or k < len(str_3):
    output = ''
    if i < len(str_1):
        output = output + str_1[i]
        i = i+1
    if j < len(str_2):
        output = output + str_2[j]
        j = j + 1
    if k < len(str_3):
        output = output + str_3[k]
        k = k + 1
    print(output, end=',')