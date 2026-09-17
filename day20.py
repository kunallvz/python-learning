#Day 20 practice daay 
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


print(is_prime(7))   # True
print(is_prime(10))  # False
print(is_prime(1))   # False
