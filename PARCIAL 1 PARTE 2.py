def mcd(a, b):
    if b == 0:
        return a
    return mcd(b, a % b)

def repetir(c, n):
    if n <= 0:
        return ""
    return c + repetir(c, n - 1)
