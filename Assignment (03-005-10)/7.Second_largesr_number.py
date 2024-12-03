# find second-largest number
numbers = list(map(int, input("Enter numbers: ").split()))

numbers.sort(reverse=True)

if len(numbers) > 1:
    print("The second-largest number is:", numbers[1])
else:
    print("Please enter at least two numbers.")
