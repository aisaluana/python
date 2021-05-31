a = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
b = []
c = []
d = []
#intervalo de 1 a 9:
print(a[1:10])
#intervalo de 8 a 13:
print(a[8:14])
#números pares:
for x in a:
    if x % 2 == 0:
        b.append(x)
    else:
        c.append(x)
print(b)
#números impares:
print(c)
#todos os múltiplos de 2,3 e 4:
for x in a:
    if x % 2 == 0 and x % 3 == 0 and x % 4 == 0:
        d.append(x)
    else:
        continue
print(d)
#lista reversa:
print(a[::-1])
#razão entre a soma dos intervalo de 10 a 15 pelo intervalo de 3 a 9 em float! (forma lenta)
total1 = 0
total2 = 0
for x in a[10:16]:
    total1 = total1 + x
for x in a[3:10]:
    total2 = total2 + x
razao = total1/total2 
print(razao)
#razão entre a soma dos intervalo de 10 a 15 pelo intervalo de 3 a 9 em float! (forma rápida)
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