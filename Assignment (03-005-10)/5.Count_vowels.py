input_string=input('Enter a word: ')
v_count=0
vowels='aeiou'
for n in input_string:
    if n in vowels:
        v_count+=1
print("Number of vowels :",v_count)