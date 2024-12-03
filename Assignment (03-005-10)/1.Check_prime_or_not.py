# Check prime or Not prime.
def is_prime(number):
    if number <=1:
        return (f"{number} is not a prime number")
    else:
        for n in range(2,int(number**0.5)+1):
            if number % n == 0:
                return (f"{number} is not a prime number")
        return f"{number} is a prime number"

Number=int(input("Enter a number: "))
Prime_number=is_prime(Number)
print(Prime_number)