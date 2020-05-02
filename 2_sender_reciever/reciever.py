import random
import sympy
import math
import os
import time

dirname = os.path.dirname(__file__)


def file_exists(file):
    if os.path.isfile(file):
        return True
    return False


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
    print(e, n)
    f.writelines(str(e)+'\n')
    f.writelines(str(n)+'\n')
    f.close()

    return (n, e, d)


def decrypt(key, n, cipher):
    text = [chr((char ** key) % n) for char in cipher]
    print(text)
    return ''.join(text)


n, e, d = initialize()

while 1:
    message_file = os.path.join(dirname, 'message.txt')
    if file_exists(message_file):
        f = open(message_file, "r")
        lines = [int(x.strip()) for x in f.readlines()]
        message = (decrypt(d, n, lines))
        time.sleep(2)
        os.remove(message_file)
    else:
        print("waiting for sender")
    time.sleep(3)
