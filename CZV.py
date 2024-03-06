import time,random
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
def lagrange(m,u):
    mul_cel = 1
    for i in range(len(m)):
        mul_cel *= m[i]
    mul = []
    for i in range(len(m)):
        mul.append(mul_cel//m[i])
    inv = []
    for i in range(len(m)):
        inv.append(inverseEukleid(mul[i],m[i]))
    res = 0
    for i in range(len(m)):
        res += u[i]*mul[i]*inv[i]
    return res % mul_cel
def garner(m,u):
    a = u[0]
    m_now = m[0]
    for i in range(1,len(m)):
        m_now *= m[i]
        q = inverseEukleid(m_now,m[i])
        y = (u[i]-a)*q % m[i]
        a += y*m_now
    return a % m_now
lagrange_vys = []
garner_vys = []
times_lagrange = []
times_garner = []
for i in range(1000):
    m = [random.randint(2,180252380737439-1) for i in range(10)]
    u = [random.randint(2,180252380737439-1) for i in range(10)]
    time1 = time.perf_counter()
    a = lagrange(m,u)
    time2 = time.perf_counter()
    b = garner(m,u)
    time3 = time.perf_counter()
    lagrange_vys.append(a)
    garner_vys.append(b)
    times_lagrange.append(time2-time1)
    times_garner.append(time3-time2)
print(sum(times_lagrange)/len(times_lagrange))
print(sum(times_garner)/len(times_garner))