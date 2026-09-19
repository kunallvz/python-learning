"""Day 25: practice filtering values with a loop."""

numbers = list(range(1, 11))
even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print("Original numbers:", numbers)
print("Even numbers:", even_numbers)
