# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

def prastevilo(n):
    """ Pogleda, če je n praštevilo. """
    if n <= 1:
        return False
    for i in range(2, round(n**(1/2) + 1)):
        if n % i == 0:
            return False
    return True

prastevila = []
i = 1
while len(prastevila) < 10001:
    if prastevilo(i):
        prastevila.append(i)
    i += 1

print(prastevila[-1])
