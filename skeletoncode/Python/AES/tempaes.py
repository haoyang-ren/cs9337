from Crypto.Cipher import AES
from Crypto import Random
import sys
import time
import binascii

cbc_key = Random.get_random_bytes(16)
iv = Random.get_random_bytes(16)

print ('='*100)                    
print ('Key used: ', [x for x in cbc_key])

cbc_key = Random.get_random_bytes(16)
iv = Random.get_random_bytes(16)
print ("IV used: ",[x for x in iv])
print ('='*100)                   

aes1 = AES.new(cbc_key, AES.MODE_CBC, iv)
aes2 = AES.new(cbc_key, AES.MODE_CBC, iv)

#plain_text = 'hello world 1234' # <- 16 bytes

plain_text = ""
try:
    source = open(sys.argv[1])
    for line in source:
        plain_text += line
    source.close()
except:
    print("Cannot open source file!")
    sys.exit()

while len(plain_text) % 16 != 0:
    plain_text += '\x00'

print ("Plaintext is: ", plain_text)

beforeEncrypt = time.time()
cipher_text = aes1.encrypt(plain_text)
print ("Ciphertext is: ",cipher_text)
afterEncrypt = time.time()
eTime = afterEncrypt - beforeEncrypt
print("The encryption time is " + str(eTime))

beforeDecrypt = time.time()
msg=aes2.decrypt(cipher_text)
print("Decrypted message: ", msg)
afterDecrypt = time.time()
dTime = afterDecrypt - beforeDecrypt
print("The decryption time is " + str(dTime))

print("The total time is " + str(eTime + dTime))

print ('='*100)                    
