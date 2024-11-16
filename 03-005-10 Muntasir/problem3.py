a=input("Enter a String :")
vowels="aeiouAEIOU"
punctuation=".,!:;'\""
astr=""
for x in a:
    if x not in punctuation:
        astr+=x

vowel=0
for i in astr:
    if i in vowels:
        vowel+=1


string_list=list(astr.lower())
string_list.reverse()
reversed_list=' '.join(string_list)

print(f"Reversed String : {reversed_list}")
print(f"Number of Vowels : {vowel}")
print(f"Lowercase : {astr.lower()}")













