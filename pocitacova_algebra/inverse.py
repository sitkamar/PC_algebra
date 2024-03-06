import timeit, time
import random
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
def inverseFermat(a,p):
    return pow(a,p-2,p)
eukleid = []
fermat = []
times_eukleid = []
times_fermat = []
for i in range(1000):
    a = random.randint(2,180252380737439-1)
    time1 = time.perf_counter()
    b = inverseEukleid(a, 180252380737439)
    time2 = time.perf_counter()
    c = inverseFermat(a, 180252380737439)
    time3 = time.perf_counter()
    eukleid.append(b)
    fermat.append(c)
    times_eukleid.append(time2-time1)
    times_fermat.append(time3-time2)
print(sum(times_eukleid)/len(times_eukleid))
print(sum(times_fermat)/len(times_fermat))