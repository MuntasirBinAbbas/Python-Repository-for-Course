
list=list(map(int,input("ENTER NUMBERS : ").split()))
s=0
x=0
for i in list:
    if i%2==0:
        s=s+i
    if i%2==1:
        x=x+i

print(f"sum of even numbers: {s}")
print(f"sum of odd numbers: {x}")


if x>s:
    a=x-s
    print(f"Difference is :{a}")
if x<s:
    b=s-x
    print(f"Difference is :{b}")
