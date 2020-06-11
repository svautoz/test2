from scipy.stats import norm


a = 0.05
city = [130, 110, 120, 140, 200, 130, 140, 170, 160, 140]
aver_city = 0
for i in range(len(city)):
    aver_city += city[i]
aver_city /= len(city)
m = len(city)
city.sort()
vill = [120, 190, 130, 160, 150, 120, 110, 120, 200]
aver_vill = 0
for i in range(len(vill)):
    aver_vill += vill[i]
aver_vill /= len(vill)
n = len(vill)
vill.sort()
list_len = len(city) + len(vill)
R = 0
mean = 1
amount = 1
vill_am = 0
if vill[0] < city[0]:
    num =  vill[0]
    vill.pop(0)
    R += 1
else:
    num = city[0]
    city.pop(0)


for r in range(2, list_len+1):
    if len(city) == 0:
        R += r
        vill.pop(0)
        continue
    if len(vill) != 0 and vill[0] == num:
        amount += 1
        mean += r
        vill_am += 1
        vill.pop(0)
        continue
    if city[0] == num:
        amount += 1
        mean += r
        city.pop(0)
        continue
    if len(vill) != 0 and vill[0] == city[0] and vill[0] != num:
        num = vill[0]
        R += (mean / amount) * vill_am
        amount = 1
        mean = r
        vill_am = 1
        vill.pop(0)
        continue
    if len(vill) != 0 and vill[0] < city[0]:
        R += r
        R += (mean / amount)*vill_am
        vill.pop(0)
        continue
    if len(vill) != 0 and vill[0] > city[0]:
        R += (mean / amount) * vill_am
        amount = 1
        vill_am = 0
        city.pop(0)
        continue

R += (mean / amount) * vill_am


MW = n / 2 * (n + m + 1)
DW = m*n / 12 * (n + m + 1)
W = (R - MW)/(DW**0.5)



Ho = 0
Ha = 0
if aver_vill < aver_city:
    if W < norm.ppf(a):
        Ha = 1
    else:
        Ho = 1
    P = 1 - norm.cdf(W)
if aver_vill > aver_city:
    if W > norm.ppf(1 - a):
        Ha = 1
    else:
        Ho = 1
    P = norm.cdf(W)
if aver_vill == aver_city:
    if W < norm.ppf(a / 2) and W > norm.ppf(1 - a / 2):
        Ha = 1
    else:
        Ho = 1
    P = min(2*norm.cdf(W), 2 - 2*norm.cdf(W))
if Ho:
    print("Принимаем гипотезу, что разность средних значений случайна")
else:
    print("Принимаем гипотезу, что разность средних значений неслучайна")
print('P=', P, "W=", W)
