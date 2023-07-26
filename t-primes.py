import math

def sieve_of_eratosthenes(n):
    primes = [False, False] + [True] * (n-1)
    p = 2
    while p * p <= n:
        if primes[p] == True:
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1
    return primes

def is_t_prime(n, primes):
    sqr = math.sqrt(n)
    return sqr == int(sqr) and primes[int(sqr)]

# Generate all primes up to sqrt(10^12)
primes = sieve_of_eratosthenes(int(math.sqrt(10**12)))

n = int(input())
numbers = list(map(int, input().split()))

for number in numbers:
    if is_t_prime(number, primes):
        print("YES")
    else:
        print("NO")
