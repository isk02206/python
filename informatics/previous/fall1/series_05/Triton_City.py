import math

def factorial(n):
    b = math.factorial(n)
    return int(b)

def binomialCoefficient(n, k):
    if 0 <=k <= n:
        return int(math.factorial(n)/(math.factorial(k) * math.factorial(n-k)))
    elif k < 0 and k > n:
        return int(0)
    
def triangularNumber(n):
    return int((n * (n + 1) / 2))
    
def tetrahedralNumber(n):
    return int(((n * (n + 1) * (n + 2)) / 6))