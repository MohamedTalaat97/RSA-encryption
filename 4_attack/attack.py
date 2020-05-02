import random
import sympy
import math
import os
import time


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

    public_file = os.path.join(dirname, 'public.txt')
    f = open(public_file, "w")
    f.writelines(str(e)+'\n')
    f.writelines(str(n)+'\n')
    f.close()

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


for d in range(1, n):
    decrypted = str(decrypt(d, n, encrypted_msg))
    if decrypted == message:
        print("d found", d)
        print(decrypted)
        break
