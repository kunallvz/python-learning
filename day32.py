# Day 32 - Python learning
# Practice file handling and a small mini-project

# Writing to a file
with open("notes.txt", "w") as file:
    file.write("Python learning notes\n")
    file.write("Today I practiced file handling and strings.\n")
    file.write("This is a good exercise for daily learning.\n")

# Reading back the file
with open("notes.txt", "r") as file:
    content = file.read()
    print("File content:\n", content)

# Mini-project: count words in the file
with open("notes.txt", "r") as file:
    words = file.read().split()
    print("Total words:", len(words))

# Another example: append data
with open("notes.txt", "a") as file:
    file.write("Keep practicing every day!\n")

# Final read
with open("notes.txt", "r") as file:
    final_text = file.read()
    print("Updated file:\n", final_text)
