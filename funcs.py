from sympy import primerange
from math import sqrt,floor, gcd, log,e
from itertools import permutations, combinations

# Разделение числа на словарь
# Ключи- простые множители
# Значения - используемые степени
def prim(n):
  i = 2
  d = {}
  if n < 0:
    d[-1] = 1
    n = -n
  while i * i <= n:
    while n % i == 0:
      if i in d.keys(): d[i] += 1
      else: d[i] = 1
      n = n // i
    i = i + 1
  if n > 1:
    if n in d.keys(): d[n] += 1
    else: d[n] = 1
  return d

# Вспомогательное: xor и получение ключа по значению
def XOR(x, y):
    return '{1:0{0}b}'.format(len(x), int(x, 2) ^ int(y, 2))

def GetKey(d, val):
  return list(d.keys())[list(d.values()).index(val)]

# Создание факторной базы по модулю N до значения n
def CreateFB(n, N):
  prange = list(primerange(1,n))
  FB=[-1]
  for prime in prange:
    m = N%prime
    for i in range(n):
      if i**2 % prime == m:
        FB.append(prime)
        break
  return FB

# Получение массива гладких по факторной базе корней
# Использует модуль и границу поиска (в обе стороны)
def Qs(ran,N, FB):
  a = floor(sqrt(N))
  print(f"a = {a}")
  arr = {}
  for i in range(max(a-ran,0),a+ran):
    Qi = i**2 - N
    pr = prim(Qi)
    smooth = True
    for mult in pr.keys():
      if mult not in FB:
        smooth = False
        break
    if smooth and len(pr.keys())>0:
      arr[i]= pr
  return arr

# Превращение разложения на простые множители в бинарную строку
def Stringify(d, FB):
  valuelist = list(d.values())
  valarr = {}
  for val in valuelist:
    valstr = ""
    for key in FB:
      if key in val.keys():
        valstr+=str(val[key]%2)
      else: valstr+="0"
    valarr[GetKey(d,val)] = valstr
  l = 3
  return valarr

# Перебор комбинаций бинарных строк
# Если в итоге комбинации соберется полный квадрат - он возвращается
def Combine(arr, FB):
  leave = False
  for length in range(1,len(arr)):
    for permutation in combinations(arr, length):
      xor= "0"*len(FB)
      for val in permutation:
        xor = XOR(xor,val)
      if xor == "0"*len(FB):
        return [x for x in permutation]

# Обратное преобразование из бинарных строк в словарь значений
def Destringify(arr, strdict, intdict):
  ans = {}
  holder = strdict
  for val in arr:
    key = GetKey(holder, val)
    ans[key] = intdict[key]
    del holder[key]
  return ans

# Нахождение Х
def FindX(arr):
  mult = 1
  for val in arr: mult *= val
  return mult

# Нахождение Y
def FindY(arr, N, FB):
  mult = 1
  for val in arr:
    for base in FB:
      if base in val.keys():
        mult *= (base**val[base])
  return int(sqrt(mult))
