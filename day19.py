# ============================================================
# PYTHON DAY 19
# TOPIC: DATETIME, TIME & RANDOMIZED PROGRAMS
# ============================================================

print("===== DAY 19: DATETIME, TIME & RANDOM =====\n")

from datetime import date, datetime, timedelta
import random
import time

# ============================================================
# 1. CURRENT DATE AND TIME
# ============================================================

print("--- 1. CURRENT DATE AND TIME ---")

now = datetime.now()
today = date.today()

print(f"Date: {today}")
print(f"Date and time: {now}")
print(f"Hour: {now.hour}, Minute: {now.minute}")

print()

# ============================================================
# 2. FORMATTING DATES
# ============================================================

print("--- 2. FORMATTING DATES ---")

print(now.strftime("%Y-%m-%d"))
print(now.strftime("%d %B %Y"))
print(now.strftime("%A, %d %B %Y at %I:%M %p"))

# Common format codes:
# %Y year, %m month, %d day, %H hour, %M minute, %S second

print()

# ============================================================
# 3. PARSING DATE TEXT
# ============================================================

print("--- 3. PARSING DATE TEXT ---")

birthday_text = "2005-08-15"
birthday = datetime.strptime(birthday_text, "%Y-%m-%d").date()
print(f"Parsed birthday: {birthday}")
print(f"Birthday month: {birthday.strftime('%B')}")

print()

# ============================================================
# 4. DATE ARITHMETIC
# ============================================================

print("--- 4. DATE ARITHMETIC ---")

future_date = today + timedelta(days=30)
past_date = today - timedelta(days=7)
print(f"30 days from today: {future_date}")
print(f"7 days ago: {past_date}")

project_start = date(2026, 1, 1)
days_since_start = (today - project_start).days
print(f"Days since project start: {days_since_start}")

print()

# ============================================================
# 5. COMPARING DATES
# ============================================================

print("--- 5. COMPARING DATES ---")

deadline = today + timedelta(days=10)
if deadline > today:
    print(f"The deadline is {deadline} and is still ahead.")
else:
    print("The deadline has passed.")

print()

# ============================================================
# 6. MEASURING EXECUTION TIME
# ============================================================

print("--- 6. MEASURING EXECUTION TIME ---")

start = time.perf_counter()
total = sum(range(1_000_000))
end = time.perf_counter()

print(f"Total: {total}")
print(f"Execution time: {end - start:.6f} seconds")

# time.sleep pauses a program. A short delay keeps this example quick.
print("Waiting for a very short moment...")
time.sleep(0.05)
print("Finished waiting.")

print()

# ============================================================
# 7. RANDOM NUMBERS AND CHOICES
# ============================================================

print("--- 7. RANDOM NUMBERS AND CHOICES ---")

random.seed(19)
print(f"Random integer: {random.randint(1, 100)}")
print(f"Random decimal: {random.random():.3f}")
print(f"Random choice: {random.choice(['Python', 'JavaScript', 'Go'])}")

print()

# ============================================================
# 8. PRACTICAL EXAMPLE: PASSWORD GENERATOR
# ============================================================

print("--- 8. PRACTICAL EXAMPLE: PASSWORD GENERATOR ---")

import string


def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length must be at least 4")
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(characters) for _ in range(length))


print(f"Generated password: {generate_password(12)}")

print()

# ============================================================
# 9. PRACTICAL EXAMPLE: COUNTDOWN
# ============================================================

print("--- 9. PRACTICAL EXAMPLE: COUNTDOWN ---")


def countdown(seconds):
    if seconds < 0:
        raise ValueError("Seconds cannot be negative")
    for remaining in range(seconds, 0, -1):
        print(f"{remaining}...", end=" ")
        time.sleep(0.05)
    print("Go!")


countdown(3)

# ============================================================
# 10. PRACTICAL EXAMPLE: AGE CALCULATOR
# ============================================================

print("--- 10. PRACTICAL EXAMPLE: AGE CALCULATOR ---")


def calculate_age(birth_date, on_date=None):
    """Calculate age while correctly handling whether the birthday passed."""
    on_date = on_date or date.today()
    age = on_date.year - birth_date.year
    birthday_this_year = birth_date.replace(year=on_date.year)
    if on_date < birthday_this_year:
        age -= 1
    return age


sample_birth_date = date(2005, 8, 15)
print(f"Age on {today}: {calculate_age(sample_birth_date, today)}")

print()

# ============================================================
# 11. PRACTICAL EXAMPLE: RANDOM QUIZ
# ============================================================

print("--- 11. PRACTICAL EXAMPLE: RANDOM QUIZ ---")

questions = [
    {"question": "What keyword defines a function?", "answer": "def"},
    {"question": "What type stores key-value pairs?", "answer": "dictionary"},
    {"question": "What symbol starts a comment?", "answer": "#"},
]

random.shuffle(questions)
score = 0
for item in questions:
    # A fixed demonstration answer makes this file non-interactive.
    print(f"Question: {item['question']}")
    print(f"Answer key: {item['answer']}")
    score += 1

print(f"Quiz questions reviewed: {score}")

print()

# ============================================================
# DAY 19 CHALLENGES
# ============================================================

# Challenge 1: Build a countdown timer using time.sleep().
# Challenge 2: Create a date difference calculator.
# Challenge 3: Generate secure-looking passwords of different lengths.
# Challenge 4: Build a random dice-rolling simulator.
# Challenge 5: Create a birthday reminder program.
# Challenge 6: Measure and compare two sorting algorithms.
# Challenge 7: Build a random multiple-choice quiz.
# Challenge 8: Create a stopwatch with start, pause, and reset operations.

print("✓ Day 19 completed!")
