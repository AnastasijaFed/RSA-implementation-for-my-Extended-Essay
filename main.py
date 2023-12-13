import rsa
from time import time
t = 0
with open('encryption_text.txt', mode='r') as f:
    message = f.read().encode('utf8')
    t = time()
    (pubkey, privkey) = rsa.newkeys(len(message)*8+11*8, accurate= True)
    print(time() - t)
    t = time()
    crypto = rsa.encrypt(message, pubkey)
    print(time() - t)
    t = time()
    decrypto = rsa.decrypt(crypto, privkey).decode("utf8")
    print(time() - t)

with open('decrypted_text.txt', mode='w') as f:
    f.write(decrypto)

