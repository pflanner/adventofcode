import hashlib


def f():
    secret_key = 'bgvyzdsv'
    i = 1

    while True:
        digest = hashlib.md5(bytes(secret_key + str(i), encoding='UTF-8')).hexdigest()
        if digest.startswith('000000'):
            return i
        i += 1


print(f())
