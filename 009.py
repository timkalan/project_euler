# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def pitagorejski_trojcek(a, b, c):
    """ Preveri, če so a, b in c pitagorejski trojček. """
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return a ** 2 + b ** 2 == c ** 2

trojcki = [(a, b, c) 
            for a in range(600)     # 600 je na uč izbrana meja
            for b in range(a, 600)
            for c in range(b, 600)
            if pitagorejski_trojcek(a, b, c)]

izbran = ()
for trojcek in trojcki:
    if trojcek[0] + trojcek[1] + trojcek[2] == 1000:
        izbran = trojcek

print(izbran[0] * izbran[1] * izbran[2])

# malo počasen