
from Crypto.Cipher import AES
from Crypto import Random
import sys
import time
import binascii

#cbc_key = Random.get_random_bytes(16)
cbc_key = ""
iv = ""

try:
    input_key = open(sys.argv[2])
    for line in input_key:
        cbc_key += line
    input_key.close()
except:
    print("Cannot open key file!")
    sys.exit()

try:
    input_iv = open(sys.argv[1])
    for line in input_iv:
        iv += line
    input_iv.close()
except:
    print("Cannot open iv file!")
    sys.exit()



try:
    cbc_key = binascii.unhexlify(cbc_key.hex())
    iv = binascii.unhexlify(iv.hex())
except:
    print("Invalid Input!")
    sys.exit()

print ('='*100)                    
print ('Key used: ', [x for x in cbc_key])

#iv = Random.get_random_bytes(16)
print ("IV used: ",[x for x in iv])
print ('='*100)                   
aes1 = AES.new(cbc_key, AES.MODE_CBC, iv)
aes2 = AES.new(cbc_key, AES.MODE_CBC, iv)

plain_text = 'hello world 1234' # <- 16 bytes
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
