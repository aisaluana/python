#Faça um programa que leia um número indeterminado de notas. Após esta entrada de dados, faça o seguinte:
# • Mostre a quantidade de notas que foram lidas.
# • Exiba todas as notas na ordem em que foram informadas.
# • Exiba todas as notas na ordem inversa à que foram informadas, uma abaixo do outra
# • Calcule e mostre a soma das notas.
# • Calcule e mostre a média das notas.
# • Calcule e mostre a quantidade de notas acima da média calculada.
grades = []
quantity = 0
highAvrgGrades = []
while True:
    put = int(input("Type a grade from 0-10 (if done, type 11): "))
    if put == 11:
        break
    else:
        grades.append(put)
        quantity += 1

print(len(grades))
print(grades)
for g in grades[::-1]:
    print(g)
print(sum(grades))
avrgGrades = sum(grades)/quantity
print(avrgGrades)
for g in grades:
    if g > avrgGrades:
        highAvrgGrades.append(g)
print(highAvrgGrades)