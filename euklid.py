def gcd(a,b):
    u0, u1 = 1, 0
    v0, v1 = 0, 1
    while b != 0:
        q, r = divmod(a,b)
        a, b = b, r
        u0, u1 = u1, u0 - q*u1
        v0, v1 = v1, v0 - q*v1
    return a, u0, v0
def inverseEukleid(a,p):
    d, u, v = gcd(a,p)
    if d == 1:
        return u % p
    else:
        return None
n = 0x8610a01d832e697a9f5dd31fd36cfd96e10c2594876e6f831a74ba11a1392f8ab205c9eba464c4515d1bb4a15820a37057030fa385cddacbf8d0eb60c083cdc488f7cb360dd00281877f0f35983a51cd489b10fd53387fff0eeeeef0b6fda12ecde457bf899d559925bb0bee07d0110435e162d4c54328f0ac029eada56403f3
n1 =  0x7720f8e16ce58bfd2da783b1df7f470c356d7250c75a402aa98ed5c76977d7bb40f7aeb68b98bafcd2d29088a477dcd6d0f0e4f9433ca4ab8d62941769d005f76a67c3fce01f07f2e228abd5457762d4610d907d4369add2ade45a7b8edf4dafae331c4df016e318fdd66931daf8e492a75e60cbc0460c553bfee08de9c98465
p = gcd(n,n1)[0]
q = n//p
print(p*q==n)
n_lamda = (p-1)*(q-1)//gcd(p-1,q-1)[0]
e = 65537
d = inverseEukleid(e,n_lamda)
c = 0x4f7a74ab7da5b0a448c99317e3afb2ba2b50e78639c39039000a5bd900c8d6c0bd2834b140c643a7c6d1928bfbf06c5e8bfea7a3c7ddf5a9f5a8cb387b0d56b9d03e5893e9d292aece7538c493d7a5f17eb3e6e7ecc2bd68bcf045d9c71b92d0685d050f847b436a3bd994da9e0375d70789fcc101e8494f31818ee39ee5690a
m = pow(c,d,n)
help = len(hex(m)[2:])
text = hex(m)[2:]
print(bytes.fromhex(text).decode("ASCII"))
