import hashlib
import string
import random
import time
import math

global fresult
global end
global str2hash
global attempt

# answer should be the MD5 hash you make- this one is "test"
answer = "1158f5f8d240a731d28068742adea0fd"
hash = input("MD5 Hash: ")
hashlength = int(input("Hash length: "))


def premutation_count():
    count = 230843697339241380472092742683027581083278564571807941132288000000000000 / math.factorial(54 - hashlength)

    print("POSSIBLE PREMUTATIONS: " + str(count))
    print("SOLVING...")


premutation_count()

start = time.time()


def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))


while fresult != answer:
    str2hash = random_char(hashlength)
    result = hashlib.md5(str2hash.encode())
    fresult = result.hexdigest()
    attempt = attempt + 1

while fresult == answer:
    end = time.time()
    elapsed = round(end - start, 2)
    hashrate2 = round(attempt / elapsed, 2)
    print("HASH SOLVED...")
    print("DECODED HASH: " + str2hash)
    print("SECONDS ELAPSED: " + str(elapsed))
    print("HASHES PER SECOND (APROX): " + "{:,}".format(hashrate2))
    print("ATTEMPTED HASHES: " + "{:,}".format(attempt))
    quit()

result = hashlib.md5(str2hash.encode())
