# ===== DAY 15: FILE HANDLING =====
print("===== DAY 15: FILE HANDLING =====\n")

# Writing to a file
print("Writing to file...")
with open('sample.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is Day 15 - File Handling\n")
    file.write("Python makes file operations easy!")

print("File written successfully!\n")

# Reading from a file
print("Reading from file...")
with open('sample.txt', 'r') as file:
    content = file.read()
    print("File content:")
    print(content)

# Reading line by line
print("\nReading line by line:")
with open('sample.txt', 'r') as file:
    for line in file:
        print(f"  {line.strip()}")

# Appending to a file
print("\nAppending to file...")
with open('sample.txt', 'a') as file:
    file.write("\nAppended line added!")

# Checking if file exists
import os
print(f"\nDoes 'sample.txt' exist? {os.path.exists('sample.txt')}")

# Getting file information
if os.path.exists('sample.txt'):
    file_size = os.path.getsize('sample.txt')
    print(f"File size: {file_size} bytes")

# Reading specific number of characters
print("\nReading first 50 characters:")
with open('sample.txt', 'r') as file:
    first_50 = file.read(50)
    print(f"'{first_50}'")

# Working with file paths
print(f"\nAbsolute path: {os.path.abspath('sample.txt')}")
print(f"File name: {os.path.basename('sample.txt')}")
print(f"Directory: {os.path.dirname(os.path.abspath('sample.txt'))}")

# Writing multiple lines
print("\nWriting to a data file...")
data = ['Name,Age,City\n', 'John,25,New York\n', 'Alice,30,London\n', 'Bob,28,Paris\n']
with open('data.csv', 'w') as file:
    file.writelines(data)

# Reading as lines
print("Reading CSV file:")
with open('data.csv', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(f"  {line.strip()}")

# File operations with context manager (best practice)
print("\nUsing context manager (best practice):")
try:
    with open('sample.txt', 'r') as file:
        word_count = len(file.read().split())
    print(f"Word count in sample.txt: {word_count}")
except FileNotFoundError:
    print("File not found!")

print("\n✓ File handling operations completed!")
