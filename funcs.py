from math import prod

a = 2
b = 62
q = 181

def prime_factorization(n):

  prime_factors_dict = dict()
  i = 1
  while i**2 <= n:
    i += 1

    while n % i == 0:
      n //= i
      if i in prime_factors_dict.keys():
        prime_factors_dict[i] += 1
      else:
        prime_factors_dict[i] = 1

  if n > 1:
    if n in prime_factors_dict.keys():
      prime_factors_dict[n] += 1
    else:
      prime_factors_dict[n] = 1

  print(f'\n{prime_factors_dict=}')
  return prime_factors_dict

def create_r_table(prime_factors):

  prime_grounds = prime_factors.keys()
  r_table = dict()
  for pi in prime_grounds:  # строки
    print()
    r_table[pi] = dict()

    for j in range(pi):  # столбцы
      degree = j * (q - 1) // pi
      r_table[pi][j] = int(
        (a ** degree) % q
      )
      print(f"r_table({pi},{j}) = {r_table[pi][j]}")

  print()
  return r_table

def logarithm_calc(r_table, prime_factors):

  modules = []  # модули
  remains = []  # остатки от деления
  prime_grounds = prime_factors.keys()
  # [a-.]
  for pi in prime_grounds:  # строки
    ai = prime_factors[pi]  # степень простого множителя
    bj = b
    x = 0

    # [i,ii,...]
    for j in range(ai):
      degree = (q - 1) // pi ** (j + 1) # показатель степени для левой части
      left_part = (bj ** degree) % q
      xj = [i for i in r_table[pi] if r_table[pi][i]==left_part] [0] # номер столбца с совпавшим значением
      x += xj * pi ** j
      bj = int(bj * pow(a, -xj * (pi ** j), q))

    # формируем итоговую систему уравнений с модулями и остатками
    print(f"X = {x} mod {pi ** ai}")
    remains.append(x)
    modules.append(pi ** ai)

  print()
  return remains, modules

# КТО
def Chinese_theorem(remains, modules):
  mult = prod(modules)
  x = 0
  for i in range(len(modules)):
    Mi = mult // modules[i]
    Yi = pow(Mi, -1, modules[i])
    print(f"Mi = {Mi}, Yi = {Yi}")
    x += remains[i] * Mi * Yi
  res = x % mult
  print(f"\nВычисленная степень: {res}")
