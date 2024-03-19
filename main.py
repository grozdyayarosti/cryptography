from math import sqrt, gcd, log,e
from funcs import CreateFB, FindX, FindY, Destringify, Qs, Stringify, Combine

N = 540143
# BaseEdge = 500
# NumRange = 5000
Ln = int(e**(sqrt(log(N)*log(log(N)))))
NumRange = Ln*2
BaseEdge = Ln//2

FB = CreateFB(BaseEdge,N)
print(f"Факторная база: {FB}")
Qpre = Qs(NumRange, N, FB)
Qstr = Stringify(Qpre, FB)
Qset = Combine(list(Qstr.values()),FB)
Qpost = Destringify(Qset, Qstr, Qpre)
print(f"Числа - участники квадрата: {list(Qpost.keys())}")
x = FindX(list(Qpost.keys()))
print(f"x = {x}")
y = FindY(list(Qpost.values()), N, FB)
print(f"y = {y}")

xmy = x-y
xpy = x+y

print(f"p = {gcd(xmy,N)}; q = {gcd(xpy,N)}")