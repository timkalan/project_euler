# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

def prastevilo(n):
    """ Pogleda, če je n praštevilo. """
    if n <= 1:
        return False
    for i in range(2, round(n**(1/2) + 1)):
        if n % i == 0:
            return False
    return True

prastevila = [i for i in range(2000000) if prastevilo(i)]

print(sum(prastevila))