def modinv(x, p):
    # p must be prime! Find y such that x*y = 1 (mod p)
    return power(x, p - 2, p)


def power(a, n, p):
    if n == 0:
        return 1
    x = power(a, n // 2, p)
    x *= x
    if n % 2 == 1:
        x *= a
    return x % p
