# program to print pattern when input is given i.e 4, 5, 10 any of number. print as many  * as input entered.
user_input = int(input("enter how many times you want to print :"))

print("single line for * is as follows: ")
for x in range(0,user_input): # no need to use len functioni on user_input, because its already casted to integer.
    # x = "*"
    #print(x)

    print("*" ,end =" ") # lines 4,5 are also right.

# print square pattern with * symbols

print(f"\nprint square pattern with * symbols as many user input given {user_input}".format(user_input))
for i in range(0,user_input):
    print("* " * user_input) # we can multiply string with integer and it will mutiply and display output


# print square pattern with provided fixed digit.
print(f"\nprint square pattern with provided fixed digit as many user input given {user_input}".format(user_input))

for i in range(0,user_input):
    print((str(user_input) + " ") * user_input ) # first casted input integer to string and adding space then multiply.

# print square pattern with provided fixed digit in every row.
print(f"\nprint square pattern with provided fixed digit in each row with input given {user_input}".format(user_input))

for i in range(1,user_input+1):
    print((str(i) + " ") * user_input)

# print square pattern with provided fixed alphabet in every row.
print(f"\nprint square pattern with provided fixed alphabet in each row with input given {user_input}".format(user_input))
for i in range(user_input):
    print('A '* user_input)

# print square pattern with provided dynamic alphabet in every row.
print(f"\nprint square pattern with provided dynamic alphabet in each row with input given {user_input}".format(user_input))
for i in range(user_input):
    print((chr(65+ i) + ' ') * user_input) # we should know ordinal value of A based on unicode i.e 65, casted to char.

# print square pattern with provided dynamic digits in every row.
print(f"\nprint square pattern with provided dynamic digits in each row with input given {user_input}".format(user_input))
for i in range(user_input): # 0,1,2
    for j in range(user_input): # 0,1,2
        print(str(j+1),end=" ")
    print() # to create space we needed this print

# print square pattern with alphabets symbols in dictionary order
print(f"\nprint square pattern with alphabets symbols in dictionary order in each row with input given {user_input}".format(user_input))
for i in range(user_input): # 0,1,2
    for j in range(user_input): # 0,1,2
        print(chr(65+j),end=" ")
    print() # to create space we needed this print

# print square pattern with static digits in descending order
print(f"\nprint square pattern with static digits  in descending order in each row with input given {user_input}".format(user_input))

for i in range(user_input): # each row has content fixed, no need for second loop
    # user_input = 3, i = 0
    print((str(user_input-i) + " ") * user_input)

# print square pattern with alphabets in reverse of dictionary order
print(f"\nprint square pattern with alphabets in reverse of dictionary order in each row with input given {user_input}".format(user_input))

for i in range(user_input):
    # A = 65, B= 66, C= 67
    # 64 + n -i -- 67--> C
    print((chr(64+ user_input-i) + " ") * user_input)

# print square pattern with dyamic digits in descending order
print(f"\nprint square pattern with dynamic digits in descending order in each row with input given {user_input}".format(user_input))

for i in range(user_input):
    for j in range(user_input): # number changing in each row
        print(user_input - j, end=" ")
    print()

# print square pattern with dyanmic alphabets in reverse of dictionary order
print(f"\nprint square pattern with dynamic alphabets in reverse of dictionary order in each row with input given {user_input}".format(user_input))

for i in range(user_input):
    for j in range(user_input):
        print(chr(64 + user_input - j), end=" ")
    print()
# print right angle traingle pattern with * symbols
print(f"\nprint right angle traingle pattern with * symbols with input given {user_input}".format(user_input))

# We can do it two ways..
for i in range(user_input):  #my approach
    i = i +1 # * symbol increases by 1 in each row
    print("* " * i)
for i in range(user_input): # second approach
    for j in range(i+1):
        print("*" , end= " ")
    print()

# print right angle triangle pattern with fixed digit in each row
print(f"\nprint right angle traingle pattern with fixed digit in each row with input given {user_input}".format(user_input))
for i in range(user_input): # 0,1,2,3
    for j in range(i +1):
        print(i +1 , end=' ')
    print()
# approach 2-
print("Approach -2 using string mulitplier")
for i in range(user_input):
    print((str(i+1) + " ")* (i+1))

# print right angle triangle pattern with fixed alphabet in each row
print(f"\nprint right angle traingle pattern with fixed digit in each row with input given {user_input}".format(user_input))

# content fixed in each row , so no second loop is required.
for i in range(user_input):
    print((chr(65 +i) + " ")* (i +1)) # i+1 used in multiplier so that each time alphabets can be printed in sync with it.

## print right angle triangle pattern with ascending digit in each row
print(f"\nprint right angle traingle pattern with ascending digit in each row with input given {user_input}".format(user_input))

# content changing in each row , so  second loop is required.
for i in  range(user_input):
    for j in range(i+1):
        print(j+1 , end=" ")
    print()

#To print right angle triangle pattern with ascending alphabet symbols in dictionary order in every row
print(f"\nright angle triangle pattern with alphabet symbols in dictionary order with input given {user_input}".format(user_input))
for i in range(user_input):
    for j in range(i+1):
        print((chr(65 + j)), end=" ")
    print()

#To print right angle triangle pattern with descending digit \ in dictionary order in every row
print(f"\nRight angle triangle pattern with descending digit \ in dictionary order with input given {user_input}".format(user_input))
for i in range(user_input):
    for j in range(i+1):
        print((user_input- j), end= ' ')
    print()

##To print right angle triangle pattern with reverse  alphabet order in dictionary order in every row
print(f"\nright angle triangle pattern with reverse alphabet symbols in dictionary order with input given {user_input}".format(user_input))
for i in range(user_input):
    for j in range(i+1):
        print(chr(64+ user_input -j), end= " ")
    print()

#To print INVERT right angle triangle pattern with * symbols in  in every row
print(f"\nINVERT right angle triangle pattern with * symbols in every row with input given {user_input}".format(user_input))
for i in range(user_input):
    #user_input = user_input -i
    print("* " * (user_input-i))

# print right INVERT angle triangle pattern with fixed digit in each row
print(f"\nprint  INVERT right angle traingle pattern with fixed digit in each row with input given {user_input}".format(user_input))

# content fixed in each row , so no second loop is required.
for i in range(user_input):
    print((str(i+1) + " ") * (user_input-i))


# print right INVERT angle triangle pattern with fixed alphabet in each row
print(f"\nprint  INVERT right angle traingle pattern with fixed alphabets in each row with input given {user_input}".format(user_input))

# content fixed in each row , so no second loop is required.
for i in range(user_input):
    print((chr(65 + i) + " ")* (user_input-i))

# print right INVERT angle triangle pattern with fixed digit descending in each row
print(f"\nprint  INVERT right angle traingle pattern with fixed digit descending in each row with input given {user_input}".format(user_input))

# content fixed in each row , so no second loop is required.
for i in range(user_input):
    print((str(user_input-i) + " ")* (user_input-i))

#24.  print right INVERT angle triangle pattern with fixed alphabet descending in each row
print(f"\nprint  INVERT right angle traingle pattern with fixed alphabet descending in each row with input given {user_input}".format(user_input))

# content fixed in each row , so no second loop is required.
for i in range(user_input):
    print((chr(64+user_input-i) + " ")* (user_input-i))

# print right INVERT angle triangle pattern with  digit  in ascending order in each row
print(f"\nprint  INVERT right angle traingle pattern with digit in ascending order each row with input given {user_input}".format(user_input))

# content not fixed in each row , so second loop is required.
for i in range(user_input): # 0,1,2,3
    for j in range(user_input-i):
        print((j+1) , end=" ")
    print() # this bring to next line, empty space. else the output be like: 0 1 2 3 4 1 2 3 4 2 3 4 3 4 4

#To print Invert right angle triangle pattern with descending digit \ in dictionary order in every row
print(f"\n Invert Right angle triangle pattern with alphabets in dictionary order with input given {user_input}".format(user_input))
for i in range(user_input): # number of elements  = userinput-i
    for j in range(user_input - i):
        print(chr(65 + j) , end= " ") # j increases by 1, such as A B C D E
    print()

#27. print right INVERT angle triangle pattern with  digit  in descending order in each row
print(f"\nprint  INVERT right angle traingle pattern with digit in descending order each row with input given {user_input}".format(user_input))

# content no fixed in each row , so second loop is required.
for i in range(user_input):
    for j in range(user_input - i): # no of elements
        print(user_input -j , end= " ")
    print()

#28  print right INVERT angle triangle pattern with alphabets  reverse  in dictionary order in each row
print(f"\nprint  INVERT right angle traingle pattern with alphabets  reverse  in dictionary order each row with input given {user_input}".format(user_input))

# content not fixed in each row , so second loop is required.
for i in range(user_input):
    for j in range(user_input-i):
        print(chr(64+user_input-j) , end= ' ')
    print()
# print pyramid pattern with * symbols