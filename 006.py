# the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def vsota_kvadratov(n):
    """ Vrne vsoto kvadratov naravnih števil do n. """

    vsota = 0
    for i in range(n+1):
        vsota += i ** 2
    return vsota


def kvadrat_vsote(n):
    """ Vrne kvadrat vsote naravnih števil do n. """

    vsota = 0
    for i in range(n+1):
        vsota += i 
    return vsota ** 2

print(kvadrat_vsote(100) - vsota_kvadratov(100))

