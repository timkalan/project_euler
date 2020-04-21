# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.

def collatz(n):
    """ Vrne dolžino collatzovega zaporedja, ki
        se začne z n. """

    i = 1
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            i += 1
        else:
            n = 3 * n + 1
            i += 1
    return i

dolzine = {i: collatz(i) for i in range(1, 1000000)}
    
print(max(dolzine, key=dolzine.get))