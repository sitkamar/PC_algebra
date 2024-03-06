import math
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

def multiplyRecursive(p,q):
    n1 = len(p)
    m = len(q)
    n = 2**math.ceil(math.log2(max(n1,m)))
    N = 2*(n+1)*max(p)*max(q)
    q += (n-m)*[0]
    p += (n-n1)*[0]
    om, M = omega(n,N)
    pa = FFT(p,om,M)
    qa = FFT(q,om,M)
    r = multiplyInFFT(pa,qa,M,om,n)
    ominv = inverseEukleid(om,M)
    h = FFT(r,ominv,M)
    koef = inverseEukleid(n,M)
    for i in range(len(h)):
        h[i] = (h[i]*koef) % M
    return h

def multiplyIterrative(p,q):
    n1 = len(p)
    m = len(q)
    n = 2**math.ceil(math.log2(max(n1,m)))
    N = 2*(n+1)*max(p)*max(q)
    q += (n-m)*[0]
    p += (n-n1)*[0]
    om, M = omega(n,N)
    pa = FFTiter(p,om,M)
    qa = FFTiter(q,om,M)
    r = multiplyInFFT(pa,qa,M,om,n)
    ominv = inverseEukleid(om,M)
    h = FFTiter(r,ominv,M)
    koef = inverseEukleid(n,M)
    for i in range(len(h)):
        h[i] = (h[i]*koef) % M
    return h

def multiplyInFFT(p, q, M,om,n):
    r = (n)*[0]
    for i in range(n):
        try:
            r[i] = (p[i]*q[i]) % M
        except:
            r[i] = 0
    return r

def printPoly(p):
    string = ""
    for i in range(len(p)-1,-1,-1):
        if p[i] == 1:
            pass
        elif p[i] != 0:
            string += str(p[i])
        if p[i] != 0:
            if i == 0:
                string += " + "
            elif i == 1:
                string += "x + "
            else:
                string += "x^" + str(i) + " + "
    print(string[:-3])

def omega(n, N):
    u=1
    M = 2**(u*n//2)+1
    while M<N:
        u +=1
        M = 2**(u*n//2)+1
    return 2**(u),M

def FFT(p,omega,M):
    if len(p)==1:
        return p
    if len(p)%2 == 1:
        p.append(0)
    n = len(p)
    s = FFT(p[0::2],omega**2,M)
    t = FFT(p[1::2],omega**2,M)
    y = [0]*n
    ni = 1
    for k in range(n//2):
        y[k] = (s[k]+ni*t[k]) % M
        y[k+n//2] = (s[k]-ni*t[k]) % M
        ni*=omega
    return y

def FFTiter(p,omega,M):
    k = int(math.log2(len(p)))
    n = len(p)
    ome = [0]*(k-1) + [omega]
    A = [0]*n
    for i in range(n):
        bini = bin(i)[2:]
        inv = int(((k-len(bini))*"0"+bini)[::-1],2)
        A[i] = p[inv]
    
    for i in range(1,k):
        ome[k-i-1] = ome[k-i]**2 % M
    for i in range(1,k+1):
        m = 2**i
        for j in range(0,n-m+1,m):
            ni = 1
            for l in range(m//2):
                s = A[j+l]
                t = A[j+l+m//2]*ni
                ni *= ome[i-1]
                A[j+l] = (s+t) % M
                A[j+l+m//2] = (s-t) % M
    return A
                
#print(FFT([4,2,1,0],2,5))
#print(FFTiter([4,2,1,0],2,5))
printPoly(multiplyRecursive([1,2,1,2,1],[0,1]))
printPoly(multiplyIterrative([1,2,1,2,1],[0,1]))