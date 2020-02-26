import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast
import sys
import time

random_generator = Random.new().read
key = RSA.generate(1024, random_generator) #generate pub and priv key

publickey = key.publickey() # pub key export for exchange

print '='*100                    
#plain_text = 'abcdefghijklmnopqrst'
plain_text = ""
try:
    source = open(sys.argv[1])
    for line in source:
        plain_text += line
    source.close()
except:
    print("Cannot open source file!")
    sys.exit()

while len(plain_text) % 32 != 0:
    plain_text += '\x00'
print "Plaintext is: ", plain_text

beforeEncrypt = time.time()
cipher_text = publickey.encrypt(plain_text, 32)#message to encrypt is in the above line 'encrypt this message'
print 'Plaintext encrypted using Public Key is:', cipher_text
afterEncrypt = time.time()
eTime = afterEncrypt - beforeEncrypt
print("The encryption time is " + str(eTime))

#decrypted code below
beforeDecrypt = time.time()
decrypted = key.decrypt(ast.literal_eval(str(cipher_text)))
afterDecrypt = time.time()
dTime = afterDecrypt - beforeDecrypt
print("The decryption time is " + str(dTime))

print("The total time is " + str(eTime + dTime))
print ('Ciphertext decrypted with Private key is', decrypted)
print '='*100



