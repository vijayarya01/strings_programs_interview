#4. Write a program to reverse internal content of every second word present in the given string ?

input_str = "one two three four five six"
print("content before reversing is: ", input_str)

lis = input_str.split() # it will return in list data type
print("using split function without any parameter this returns ",lis)
new_list = []   # empty list, will add modified words here
i= 0
while i < len(lis):
    if i%2 == 0:
        new_list.append(lis[i])
    else:
        new_list.append(lis[i][::-1])
    i = i+1
output = " ".join(new_list)
print("content after reversing and using join, is: ",output)