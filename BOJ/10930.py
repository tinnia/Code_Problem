import hashlib

st = input().encode()
hash = hashlib.sha256(st).hexdigest()
print(hash)