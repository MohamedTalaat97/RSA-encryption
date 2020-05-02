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


def encrypt(key, n, text):
    cipher = [(ord(char) ** key) % n for char in text]
    return cipher


message = "Lorem Ipsum is simply dummy text of the printing and typesetting industry"
public_file = os.path.join(dirname, 'public.txt')
message_file = os.path.join(dirname, 'message.txt')

while(1):
    message = input("enter message to send")
    if file_exists(public_file):
        f = open(public_file, "r")
        e = int(f.readline().strip())
        n = int(f.readline().strip())
        f.close()
        encrypted_msg = encrypt(e, n, message)
        if not file_exists(message_file):
            f = open(message_file, 'w')
            for m in encrypted_msg:
                f.write(str(m) + '\n')
            f.close()
            time.sleep(3)
    time.sleep(2)
    else:
        print("waiting for public file")
