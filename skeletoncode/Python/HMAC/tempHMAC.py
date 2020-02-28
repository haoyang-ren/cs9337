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

digest_maker = hmac.new(secret_key)#in your code replace key

f = open('lorem.txt', 'rb')
try:
    while True:
        block = f.read(1024)
        if not block:
            break
        digest_maker.update(block)
finally:
    f.close()

beforeGeneration = time.time() 
digest = digest_maker.hexdigest()
afterGeneration = time.time()
dTime = afterGeneration - beforeGeneration
print("The signature generation time is " + str(dTime))

print '='*100 
print "HMAC digest generated for \"lorem.txt\" file is:", digest
print '='*100 
