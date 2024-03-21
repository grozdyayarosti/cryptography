from sympy import primerange
from math import sqrt, prod
from itertools import combinations

# Разделение числа на простые множители(множитель: его степень)
def prime_factorization(n):
  i = 2
  prime_factors_dict = dict()
  if n < 0:
    prime_factors_dict[-1] = 1
    n = -n
  while i * i <= n:
    while n % i == 0:
      if i in prime_factors_dict.keys(): prime_factors_dict[i] += 1
      else: prime_factors_dict[i] = 1
      n = n // i
    i += 1
  if n > 1:
    if n in prime_factors_dict.keys(): prime_factors_dict[n] += 1
    else: prime_factors_dict[n] = 1
  return prime_factors_dict

def XOR(x, y):
    return '{1:0{0}b}'.format(len(x), int(x, 2) ^ int(y, 2))

def FB_calc(border, N):
  # формируем диапазон только из простых чисел
  prime_range = list(primerange(1, border))
  FB=[-1]
  # проверяем каждое простое число(есть ли в нем x, x^2=N mod pj)
  for prime_number in prime_range:
    Nmod = N % prime_number
    for i in range(border):
      if i*i % prime_number == Nmod:
        FB.append(prime_number)
        break
  return FB


def get_Q(FB, a, border, N):
  Q = dict()
  left_border = 0 if border>a else a-border
  right_border = a + border
  for i in range(left_border, right_border):

    # вычисляем простые множители для одного Qi
    Qi = i**2 - N
    prime_factors = prime_factorization(Qi)

    # каждый Qi проверяем на гладкость
    is_smooth = True
    for prime_ground in prime_factors.keys():
      if prime_ground not in FB:
        is_smooth = False
        break

    # если Qi гладкое и непустое, то добавляем набор его простых множителей в Q под индексом
    if is_smooth and len(prime_factors.keys())>0:
      Q[i]= prime_factors

  return Q

def Q_to_string(Q, FB):
  primes_list = list(Q.values())
  bin_list = dict()
  for primes in primes_list:

    # для Qi и простого числа выбирается 1 число из ФБ если оно нечетное иначе 0
    bin_string = ""
    for prime_ground in FB:
      if prime_ground in primes.keys():
        bin_string += str( primes[prime_ground]%2 )
      else:
        bin_string += "0"

    # среди индексов Q находим тот, который соответствует набору простых множителей
    key = list(Q.keys()) [ list(Q.values()).index(primes) ]
    bin_list[key] = bin_string

  return bin_list

def get_null_combination(Q_string, FB):
  # преобразование каждой бин строки в список
  primes_string = list(Q_string.values())
  # перебор сначала комбинаций из 1 бин строки, потом из 2, из 3 и тд
  for str_amount in range(1, len(primes_string)):

    for combination in combinations(primes_string, str_amount):
      xor = "0" * len(FB)
      # ксорим все значения комбинации
      for value in combination:
        xor = XOR(xor, value)
      # Если находим комбинацию, при которой ксор дал нули, то запоминаем ее(в виде списка)
      if xor == "0" * len(FB):
        return list(combination)

def Q_to_int(Q_null_combs, Q_string, Q_int):
  Q = dict()
  for val in Q_null_combs:
    # среди индексов находим тот, который соответствует набору простых множителей
    key = list(Q_string.keys()) [ list(Q_string.values()).index(val) ]
    Q[key] = Q_int[key]
    Q_string.pop(key)
  return Q

def get_x(Q):
  Q_indexes = list(Q.keys())
  x = prod(Q_indexes)
  return x

def get_y(Q, FB):
  primes = list(Q.values())
  mult = 1
  for prime in primes:
    for base_value in FB:
      # Если число из ФБ есть среди оснований множителей, то добавляем его в степени в произведение
      if base_value in prime.keys():
        mult *= base_value**prime[base_value]
  return int(sqrt(mult))
