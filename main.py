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

a = 2
b = 62
q = 181
# Ответ 100 (работает)

# a = 2
# b = 28
# q = 37
# Ответ 34 (работает)

# a = 2
# b = 7
# q = 61
# Ответ 49 (работает)

# a = 3
# b = 11
# q = 17
# Ответ 7 (работает)


# [1]
# Разложение на простые множители
p = prim(q-1)
print(p)

# [2]
# Создание таблицы r(pi,j) которая в середине 134 страницы Сон Яна
r = {}
for pi in p.keys():
  print()
  r[pi] = {}
  for j in range(pi):
    right = (a**(j*(q-1)//pi))%q
    r[pi][j] = int(right)
    print(f"r({pi},{j}) = {r[pi][j]}")
print()

# [3-1]
# Вычисление отдельных дискретных логарифмов
k = [] # Остатки от деления
m = [] # Модули
# [a-.]
for pi in p.keys():
  ai = p[pi]
  bj = b
  x = 0
  # [i,ii,...]
  for j in range(ai):
    # print(f"Итерация №{j} для Pi={pi}")
    # Левая часть которую можем высчитать
    left = (bj**((q-1)//pi**(j+1))) % q
    # Находим, при каком значении второго индекса (xj) r(pi,xj) совпадет с результатом вычисления
    xj = GetKey(r[pi], left)
    # Добавляем к сумме формируя итоговый X
    x += xj*pi**j
    # Подготовка к новой итерации
    bj = int(bj *  pow(a,-xj*(pi**j), q))
  # [Последняя строка a-.]
  # Смотрим и сохраняем итоговое уравнение
  print(f"X = {x} mod {pi**ai}")
  k.append(x)
  m.append(pi**ai)
print()

# Решаем систему уравнений по китайской теореме об остатках
print(f"Факторизованная степень: {China(k,m)}")