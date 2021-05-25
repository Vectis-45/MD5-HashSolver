import hashlib


str2hash = input('Enter string to hash: ')
str2hash_length = len(str2hash)

result = hashlib.md5(str2hash.encode())


print("The hexadecimal equivalent of hash is : " + result.hexdigest())
print("Hash length: " + str(str2hash_length))
if str2hash_length > 6:
    print("WARNING: Your hash is over 6 characters long and may take a while to solve")
