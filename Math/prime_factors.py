from collections import defaultdict
import math


def prime_factors(n):
    res = defaultdict(lambda: 0)
    while n % 2 == 0:
        n //= 2
        res[2] += 1
    for i in range(3, int(math.sqrt(n)) + 2, 2):
        while n % i == 0:
            n //= i
            res[i] += 1
    if n > 2:
        res[n] += 1
    return res
