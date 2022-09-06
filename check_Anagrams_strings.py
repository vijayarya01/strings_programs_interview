# 14. write a program to check if the given string is Anagram or not ?

# example of anagrams words are-- lazy - zaly, silent - listen , traingle -intergral

first_string = input("Enter first string to check anagram ")
second_string = input("Enter second string to check anagram ")

if sorted(first_string) == sorted(second_string):
    print("Anagram it is")
else:
    print("Not Anagram")