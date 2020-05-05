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


def inverseMod(x, y):
    for k in range(1, y):
        if (y*k + 1) % x == 0:
            return (y*k + 1) // x
    return None


def initialize(p, q):
    print(p, q)
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


message = "Lorem ipsum is a placeholder text"
times, e_arr = [], []
print(len(message))

primes = [i for i in range(10, 1000) if sympy.isprime(i)]

i = 0
n_arr = []
e_arr = []
while i < len(primes) - 2:

    p = primes[i]
    q = primes[i+1]
    print(p, q)
    n = p * q
    phi = (p-1) * (q-1)
    n_arr.append(n)
    for k in range(2, phi):
        if co_prime(k, phi):
            e_arr.append(k)

    e = e_arr[-1]

    t1 = time.time()
    encrypted_msg = encrypt(e, n, message)
    times.append((time.time() - t1)*1000)
    i += 2


plt.plot(times[::int(len(times)/50)], n_arr[::int(len(n_arr)/50)])
plt.xlabel('time in milliseconds')
plt.ylabel('n')
plt.title('plot')
plt.show()
