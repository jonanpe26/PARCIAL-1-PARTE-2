def mcd(a, b):
    if b == 0:
        return a
    return mcd(b, a % b)

def repetir(c, n):

