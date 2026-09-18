"""Day 25: practice filtering values with a loop."""

numbers = range(1, 11)
even_numbers = [number for number in numbers if number % 2 == 0]
print("Even numbers:", even_numbers)
