import hashlib
import sys
import time

#initializing string
print '='*100 
#str = "SHA1 Clear text"
  
plain_text = ""
try:
    source = open(sys.argv[1])
    for line in source:
        plain_text += line
    source.close()
except:
    print("Cannot open source file!")
    sys.exit()

beforeEncrypt = time.time()
result = hashlib.sha1(plain_text.encode()) 
afterEncrypt = time.time()
eTime = afterEncrypt - beforeEncrypt
print("The encryption time is " + str(eTime))
  
# printing the equivalent hexadecimal value. 
print("The hexadecimal equivalent of SHA1 digest is : ")
beforeDecrypt = time.time() 
print(result.hexdigest())
afterDecrypt = time.time()
dTime = afterDecrypt - beforeDecrypt
print("The decryption time is " + str(dTime))

print("The total time is " + str(eTime + dTime))
print '='*100 
