a = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
b = []
c = []
d = []
print(a[1:10])
print(a[8:14])
for x in a:
    if x % 2 == 0:
        b.append(x)
    else:
        c.append(x)
print(b)
print(c)
for x in a:
    if x % 2 == 0 and x % 3 == 0 and x % 4 == 0:
        d.append(x)
    else:
        continue
print(d)
print(a[::-1])
total1 = 0
total2 = 0
for x in a[10:16]:
    total1 = total1 + x
for x in a[3:10]:
    total2 = total2 + x
razao = total1/total2 
print(razao)
tot1 = 0
tot2 = 0
for x in a:
    if x in a[10:16]:
        tot1 = tot1 + x
    elif x in a[3:10]:
        tot2 = tot2 + x
    else: continue
raz = tot1/tot2
print(raz)