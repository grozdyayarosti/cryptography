from math import prod

# Возвращает словарь простых множителей
# d[основание] = степень
def prim(n):
  i = 2
  d = {}
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

# Китайская теорема об остатках
# k - остатки от деления
# m - модули
def China(k,m):
  M = prod(m)
  x = 0
  for i in range(len(m)):
    Mi = M//m[i]
    Yi = pow(Mi,-1,m[i])
    print(f"Mi = {Mi}, Yi = {Yi}")
    x += k[i]*Mi*Yi
  return x%M

# Получение ключа по значению
def GetKey(dic, v):
  return [i for i in dic if dic[i]==v][0]