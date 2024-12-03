# Count total digit.
S=str(input('Enter a string: '))
digits="0123456789"
Count_digit=0
for n in S:
    if n  in digits:
        Count_digit+=1

print("Total digits are: ",Count_digit)
