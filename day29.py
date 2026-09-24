# Day 29 - Python learning
# Practice with list operations and list comprehensions

numbers = [3, 8, 12, 5, 20, 7]
print("Original list:", numbers)

# 1. Add element at the end
numbers.append(15)
print("After append:", numbers)

# 2. Remove the first occurrence of a value
numbers.remove(12)
print("After remove:", numbers)

# 3. Sort numbers
numbers.sort()
print("Sorted list:", numbers)

# 4. Find even numbers with list comprehension
even_numbers = [n for n in numbers if n % 2 == 0]
print("Even numbers:", even_numbers)

# 5. Square each number
squares = [n * n for n in numbers]
print("Squares:", squares)

# 6. Find the largest number
largest = max(numbers)
print("Largest number:", largest)

# 7. Copy a list
copied_list = numbers.copy()
print("Copied list:", copied_list)
