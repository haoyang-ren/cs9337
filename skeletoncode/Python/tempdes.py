
from Crypto.Cipher import DES
from Crypto import Random
import sys
import time
import binascii

text = ""
try:
    cbc_key = binascii.unhexlify(sys.argv[2])
    iv = binascii.unhexlify(sys.argv[1])
except:
    print("Invalid Input!")
    sys.exit()

des1 = DES.new(cbc_key, DES.MODE_CBC, iv)
#des2 = DES.new(cbc_key, DES.MODE_CBC, iv)

try:
    source = open(sys.argv[3])
    for line in source:
        text += line
    source.close()
except:
    print("Cannot open source file!")
    sys.exit()

#beforeEncrypt = time.time()
while len(text) % 8 != 0:
    text += '\x00'
cypher = des1.encrypt(text)
'''afterEncrypt = time.time()
eTime = afterEncrypt - beforeEncrypt
print("The encryption time is " + str(eTime))

beforeDecrypt = time.time()
decipher = des2.decrypt(text)
afterDecrypt = time.time()
dTime = afterDecrypt - beforeDecrypt
print("The decryption time is " + str(dTime))

print("The total time is " + str(eTime + dTime))'''
try:
    destination = open(sys.argv[4], "wb")
    destination.write(cypher)
    destination.close()
except:
    print("Cannot open destination file!")
    sys.exit()
