#Following code reads its source file and computes an HMAC signature for it:
import hmac
import sys
import time
#secret_key = 'secret-shared-key-goes-here'
secret_key = ""
try:
    source = open(sys.argv[1])
    for line in source:
        secret_key += line
    source.close()
except:
    print("Cannot open source file!")
    sys.exit()

beforeEncrypt = time.time()
digest_maker = hmac.new(secret_key)#in your code replace key
afterEncrypt = time.time()
eTime = afterEncrypt - beforeEncrypt
print("The encryption time is " + str(eTime))
f = open('lorem.txt', 'rb')
try:
    while True:
        block = f.read(1024)
        if not block:
            break
        digest_maker.update(block)
finally:
    f.close()

beforeDecrypt = time.time() 
digest = digest_maker.hexdigest()
afterDecrypt = time.time()
dTime = afterDecrypt - beforeDecrypt
print("The decryption time is " + str(dTime))

print("The total time is " + str(eTime + dTime))
print '='*100 
print "HMAC digest generated for \"lorem.txt\" file is:", digest
print '='*100 
