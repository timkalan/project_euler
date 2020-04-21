# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def deli_vse(n):
    for i in range(2,21):
        if n % i != 0:
            return False
    return True

n = 20
while True:
    if deli_vse(n):
        break
    else:
        n += 1
print(n)