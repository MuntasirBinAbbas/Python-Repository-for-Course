def gcd(aa, bb):
    small = min(aa, bb)

    for i in range(small, 0, -1):
        if aa % i == 0 and bb % i == 0:
            return i


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

result = gcd(a, b)
print(f"GCD of {a} and {b} is: {result}")
