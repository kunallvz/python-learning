# ============================================================
# PYTHON DAY 21
# TOPIC: CONDITIONALS, LOOPS & USER INPUT
# ============================================================

print("===== DAY 21: CONDITIONALS AND LOOPS =====\n")

# 1. if / elif / else
age = 18
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# 2. For loop
print("\nNumbers from 1 to 5:")
for i in range(1, 6):
    print(i)

# 3. While loop
print("\nCountdown:")
count = 5
while count > 0:
    print(count)
    count -= 1
print("Blast off!")

# 4. User input
name = input("Enter your name: ")
print(f"Hello, {name}! Welcome to Python learning.")

# 5. Simple grade checker
score = int(input("Enter your score: "))
if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "F"
print(f"Your grade is: {grade}")

print("\n✓ Day 21 completed!")
