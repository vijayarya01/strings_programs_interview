# 13. WAP to find the number of occurrence  of each vowel present in the given string ?
# input - 'DURGASOFTWARE' # output - A-2, E-1,O - 1, U - 1

input_str = "DURGASOFTWAREInfosysteMs"
vowel = {'a','e','i','o','u','A','E','I','O','U'}  # created a set of vowels in small and capital letter
dict = {}
for char in input_str:
    if char in vowel:
        dict[char] = dict.get(char,0) + 1 # main logic
print("number of occurrence  of each vowel present in the given string",dict)

for k, v in sorted(dict.items()):
    print("{} occurs {} times".format(k,v))