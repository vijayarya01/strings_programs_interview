#2. write a program to reverse words in given string ? or WAP to reverse order of words ?

input_string = "Learning python is very easy"

#Approach 1 -

list_str = input_string.split() # this returns list
rev_words= list_str[::-1]
re = " ".join(rev_words) # this will join the words in above list and return string
print("Before reversing order of words: ",input_string)
print("After reversing order: " , re)

#3. Write a program to reverse internal content of each word ?

#Apprach -1 Using slicing on given words
input_str = "Durga Software Solutions"
print("contents of words before reversing: ",input_str )
list = input_str.split() # if we dont pass any parameter in split function, this will done by space automatically.
new_list = []
for word in list:
    new_list.append(word[::-1])
print("words after apending in new_list ",new_list)
print("Reveresed content of words: "," ".join(new_list))