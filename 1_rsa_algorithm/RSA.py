'''
algorithm steps

1.select to random prime numbers p,q
2.rsa mosulus n = p*q
3.totient = (p-1)(q-1)
4.select public ket --must co prime with totient --fine co primes --
5.select private key private x public  = 1 mod totient --use euclidean to solve
'''
import math
import sympy


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
    while 1:
        p = int(input("Enter large prime number P "))
        q = int(input("Enter large prime number Q "))

        if sympy.isprime(p) and sympy.isprime(q) and p != q and p > 10 and q > 10:
            break
        else:
            print("enter prime numbers not equal to each other or too small")

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


n, e, d = initialize()
message = input("Enter message ")
encrypted_msg = encrypt(e, n, message)
print("Decrypting message ", e, " . . .")
decrypted_msg = str(decrypt(d, n, encrypted_msg))
print("decrypted ->", decrypted_msg)


# 3167 4153
