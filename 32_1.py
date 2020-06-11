from scipy.stats import norm

a = float(input("Введите уровень значимости:"))
n_1_n = float(input("Введите кол-во исходов в первом варианте опыта:"))
n_1_1 = float(input("Введите кол-во удачных исходов в первом варианте опыта:"))
n_2_n = float(input("Введите кол-во исходов во втором варианте опыта:"))
n_2_1 = float(input("Введите кол-во удачных исходов во втором варианте опыта:"))
n_1_2 = n_1_n - n_1_1
n_2_2 = n_2_n - n_2_1
n_n_1 = n_1_1 + n_2_1
n_n_2 = n_1_2 + n_2_2
n = n_1_n + n_2_n
p1 = n_1_1 / n_1_n
p2 = n_2_1 / n_2_n
T = (p1 - p2)/((n_n_1 / n)*(1 - n_n_1 / n)*(1 / n_1_n + 1 / n_2_n))**0.5
Ho = 0
Ha = 0
if p1 > p2:
    if T > norm.ppf(1 - a):
        Ha = 1
    else:
        Ho = 1
    P = 1 - norm.cdf(T)
if p1 < p2:
    if T < norm.ppf(a):
        Ha = 1
    else:
        Ho = 1
    P = norm.cdf(T)
if p1 == p2:
    if T < norm.ppf(a / 2) and T > norm.ppf(1 - a / 2):
        Ha = 1
    else:
        Ho = 1
    P = min(2*norm.cdf(T), 2 - 2*norm.cdf(T))
if Ho:
    print("Принимаем гипотезу, что вероятность удачного исхода для двух опытов одинакова")
else:
    print("Принимаем гипотезу, что вероятность удачного исхода для двух опытов различается")
print('P=', P, "T=", T)
