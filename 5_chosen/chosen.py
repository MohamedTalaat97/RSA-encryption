'''
The man-in-the-middle (or attacker) somehow gets the decryption of chosen ciphertexts from the receiver.
The attacker uses the decryptions and try to retrieve the original message sent.
The sender sends C = M^e mod n to the receiver.
The man-in-the-middle acquires the ciphertext C and multiplies it by a random number raised to the power e.
The cipher now is C' = C * (random_number)^e
The receiver deciphers the message to get D = (C')^d mod n
The receiver finds that this message has no meaning, and then sends back to the sender informing him that he has sent an invalid text.
The attacker acquires D and just divides it by the same random number it used to get the original message.
'''

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
    return (n, e, d)


def encrypt(key, n, text):

    cipher = [(ord(char) ** key) % n for char in text]
    return cipher


def decrypt(key, n, cipher):
    text = [chr((char ** key) % n) for char in cipher]
    return ''.join(text)


# sender
message = "Lorem Ipsum is simply dummy text"
n, e, d = initialize()
encrypted_msg = encrypt(e, n, message)


# attack
r = random.randint(1, 51)
c_dash = [i*(r**e) for i in encrypted_msg]


# reciever
decrypted = decrypt(d, n, c_dash)
if decrypt != message:
    print("recieved nonsense message")


# attack
original = [chr(int(ord(char)/r) for char in decrypted]

print(original)
