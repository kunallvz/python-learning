"""Day 26: practice list comprehension to build a square list."""

numbers = list(range(1, 11))
squares = [n ** 2 for n in numbers]

print("Numbers:", numbers)
print("Squares:", squares)
