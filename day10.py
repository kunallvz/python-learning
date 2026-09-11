fruits = {'banana', 'orange', 'mango', 'lemon'}
print(fruits)
fruits = {'banana', 'orange', 'mango', 'lemon'}
print(len(fruits))

# ===== SETS =====
print("\n===== SETS =====")

# Creating sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(f"Set 1: {set1}")
print(f"Set 2: {set2}")

# Set methods
set1.add(6)
print(f"After adding 6: {set1}")

set1.remove(2)
print(f"After removing 2: {set1}")

# Set operations
union = set1.union(set2)
print(f"Union: {union}")

intersection = set1.intersection(set2)
print(f"Intersection: {intersection}")

difference = set1.difference(set2)
print(f"Difference: {difference}")

# Check membership
print(f"Is 5 in set1? {5 in set1}")

# ===== TUPLES =====
print("\n===== TUPLES =====")

# Creating tuples
tuple1 = (1, 2, 3, 4, 5)
tuple2 = ('apple', 'banana', 'cherry')
mixed_tuple = (1, 'hello', 3.14, True)
print(f"Tuple 1: {tuple1}")
print(f"Tuple 2: {tuple2}")
print(f"Mixed Tuple: {mixed_tuple}")

# Accessing tuple elements
print(f"First element of tuple1: {tuple1[0]}")
print(f"Last element of tuple2: {tuple2[-1]}")

# Tuple slicing
print(f"Slice [1:3]: {tuple1[1:3]}")

# Tuple unpacking
a, b, c = (10, 20, 30)
print(f"Unpacked values: a={a}, b={b}, c={c}")

# Tuple length
print(f"Length of tuple1: {len(tuple1)}")

# Tuple methods
print(f"Count of 2 in tuple1: {tuple1.count(2)}")
print(f"Index of 3 in tuple1: {tuple1.index(3)}")

# Nested tuple
nested_tuple = (1, (2, 3), (4, 5, 6))
print(f"Nested tuple: {nested_tuple}")
print(f"Second element of nested_tuple: {nested_tuple[1]}")

# Tuple immutability
try:
    tuple1[0] = 100  # This will raise an error
except TypeError as e:
    print(f"Error: {e} - Tuples are immutable!")

# Converting between sets and tuples
print(f"\nConverting set to tuple: {tuple(set1)}")
print(f"Converting tuple to set: {set(tuple1)}")
