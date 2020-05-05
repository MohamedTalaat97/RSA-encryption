import random
import sympy
import math
import os
import time
import matplotlib.pyplot as plt


def co_prime(x, y):
    if (math.gcd(x, y) == 1):
        return True
    return False


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


def inverseMod(x, y):
    for k in range(1, y):
        if (y*k + 1) % x == 0:
            return (y*k + 1) // x
    return None


def initialize(p, q):
    n = p * q
    phi = (p-1) * (q-1)
    e = 0
    for i in range(2, phi):
        if co_prime(i, phi):
            e = i
            break

    d = inverseMod(e, phi)
    return (n, e, d)


def encrypt(key, n, text):
    cipher = [(ord(char) ** key) % n for char in text]
    return cipher


def decrypt(key, n, cipher):
    text = [chr((char ** key) % n) for char in cipher]
    return ''.join(text)


start = 10
message = "Lorem ipsum is a placeholder text"
times, n_arr = [], []
primes = [i for i in range(10, 90000) if sympy.isprime(i)]

i = 0
while 1:
    if i > (len(primes) - 2):
        break

    n, e, d_original = initialize(primes[i], primes[i+1])
    n_arr.append(n)
    encrypted_msg = encrypt(e, n, message)
    # attack##########################################
    t1 = time.time()
    prime_factors_n = prime_factors(n)
    prime_factors_n = [x for x in prime_factors_n if x < n**2 and x != 1]
    print(prime_factors_n)
    n, e, d = initialize(prime_factors_n[0], prime_factors_n[1])
    '''
    decrypted = str(decrypt(d, n, encrypted_msg))
    if decrypted == message:
        print("attack successful")
    else:
        print("attack un ")
    '''
    times.append((time.time() - t1)*1000)
    del e
    i += 2


plt.plot(times[::int(len(times)/5)], n_arr[::int(len(n_arr)/5)])
plt.xlabel('time in milliseconds')
plt.ylabel('n')
plt.title('plot')
plt.show()
