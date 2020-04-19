# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# def najmanjsi_deljivec(n):
#     """ Vrne najmanjše število, ki je deljivo z vsemi števili do n. """

#     stevilo = n
#     kandidati = [_ for _ in range(n, 0, -1)]
#     print(kandidati)

#     for kandidat in kandidati:
#         if stevilo % kandidat != 0:
#             stevilo *= kandidat
#             print(stevilo)
#     return stevilo 

# print(najmanjsi_deljivec(10))



def prastevilo(n):
    """ Pogleda, če je n praštevilo. """

    for i in range(2, round(n**(1/2) + 1)):
        if n % i == 0:
            return False
    return True


def prafaktorji(n):
    """ Poišče prafaktorje števila n. """

    prafaktorji = []
    for i in range(2, n + 2):
        if prastevilo(i):
            if n % i == 0:
                prafaktorji.append(i)

    return prafaktorji

print([prafaktorji(i) for i in range(1, 21)])

stevilo = 20
faktorji = prafaktorji(20)

for kandidat in range(20, 0, -1):
    if prafaktorji(kandidat) not in faktorji:
        stevilo *= 