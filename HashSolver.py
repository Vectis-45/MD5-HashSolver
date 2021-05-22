import hashlib
import string
import random
import time

global fresult
global end
global str2hash
global attempt
fresult = "null"
str2hash = "null"
attempt = 0
end = 1

# answer should be the MD5 hash you make- this one is "test"
answer = "098f6bcd4621d373cade4e832627b4f6"

start = time.time()


def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))


while fresult != answer:
    str2hash = random_char(4)
    result = hashlib.md5(str2hash.encode())
    fresult = result.hexdigest()
    attempt = attempt + 1
    end = time.time()
    print("ATTEMPT:", attempt, "NOT SOLVED:", fresult, str2hash)

while fresult == answer:
    end = time.time()
    elapsed = round(end - start, 2)
    hashrate2 = round(attempt / elapsed, 2)
    print("HASH SOLVED")
    print("DECODED HASH:", str2hash)
    print("SECONDS ELAPSED:", str(elapsed))
    print("HASHES PER SECOND", hashrate2)
    exit()

result = hashlib.md5(str2hash.encode())