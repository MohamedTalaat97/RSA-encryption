import random
import sympy
import math
import os
import time


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def co_prime(x, y):
    if (math.gcd(x, y) == 1):
        return True
    return False


def inverseMod(x, y):
    for k in range(1, y):
        if (y*k + 1) % x == 0:
            return (y*k + 1) // x
    return None


def initialize():
    primes = [i for i in range(10, 100) if sympy.isprime(i)]
    p = random.choice(primes)
    q = random.choice(primes)

    print(p, q)
    n = p * q
    phi = (p-1) * (q-1)

    for e in range(2, phi):
        if co_prime(e, phi):
            break

    d = inverseMod(e, phi)
    return (n, e, d)


def encrypt(key, n, text):

    cipher = [(ord(char) ** key) % n for char in text]
    return cipher


def decrypt(key, n, cipher):
    text = [chr((char ** key) % n) for char in cipher]
    return ''.join(text)


message = "Lorem Ipsum is simply dummy text"
n, e, d_origianl = initialize()
encrypted_msg = encrypt(e, n, message)

prime_factors_n = prime_factors(n)
prime_factors_n = [x for x in prime_factors_n if x < n**2 and x != 1]
print(prime_factors_n)
n, e, d = initialize(prime_factors_n[0], prime_factors_n[1])
