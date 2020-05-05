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

primes = [i for i in range(10, 150) if sympy.isprime(i)]

p = random.choice(primes)
q = random.choice(primes)
n = p * q
phi = (p-1) * (q-1)
e_arr = []

for i in range(2, phi):
    if co_prime(i, phi):
        e_arr.append(i)


for e in e_arr:
    t1 = time.time()
    encrypted_msg = encrypt(e, n, message)
    times.append(time.time() - t1)


plt.plot(e_arr, times)
plt.xlabel('e')
plt.ylabel('time')
plt.title('plot')
plt.show()
