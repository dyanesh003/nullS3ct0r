from Crypto.Util.number import long_to_bytes, getPrime, bytes_to_long, isPrime
flag = b"******************"

p = getPrime(1024)
while not isPrime(p+2):
    p = getPrime(1024)

q = p+2
N = p*q
e = 65537
ct = pow(bytes_to_long(flag),e,N)

f = open('output.txt','w')
f.write("N = "+str(N)+'\n')
f.write("e = "+str(e)+'\n')
f.write("ct = "+str(ct)+'\n')