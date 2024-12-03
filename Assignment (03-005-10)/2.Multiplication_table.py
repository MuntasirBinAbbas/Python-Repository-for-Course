# Multiplication table from user input
Num=int(input("Enter a number for multiplication table: "))

for i in range(1,11):
    m= i*Num
    print(f"{Num}*{i}={m}")
    i += 1
