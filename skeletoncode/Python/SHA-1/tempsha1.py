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

beforeDigest = time.time()
result = hashlib.sha1(plain_text.encode()) 
afterDigest = time.time()
eTime = afterDigest - beforeDigest
print("The digest generation time is " + str(eTime))
  
# printing the equivalent hexadecimal value. 
print("The hexadecimal equivalent of SHA1 digest is : ")
print(result.hexdigest())

print '='*100 
