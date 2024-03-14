from funcs import prime_factorization, Chinese_theorem, q, b, a, create_r_table, logarithm_calc

# Разложим q-1 на простые множители
prime_factors = prime_factorization(q - 1)

# Составим таблицы r(pi,j) для поля
r_table = create_r_table(prime_factors)

# Находим отдельные дискретные логарифмы x=log a(b) mod q
remains,modules = logarithm_calc(r_table, prime_factors)

# Решаем систему уравнений с помощью китайской теоремы об остатках
Chinese_theorem(remains, modules)