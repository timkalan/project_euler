# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def prastevilo(n):
    """ Pogleda, če je n praštevilo. """

    for i in range(2, round(n**(1/2) + 1)):
        if n % i == 0:
            return False
    return True


def prafaktorji(n):
    """ Poišče prafaktorje števila n. """

    prafaktorji = []
    for i in range(2, round(n**(1/2) + 2)):
        if prastevilo(i):
            if n % i == 0:
                prafaktorji.append(i)

    return prafaktorji

print(max(prafaktorji(600851475143)))