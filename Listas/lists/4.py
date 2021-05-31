#Ler um vetor com 20 idades e exibir a maior e a menor.
a = []
lessThan = 0
moreThan = 0
for x in range(20):
    age = int(input("Digite sua idade: "))
    a.append(age)
    if x == 0:
        lessThan = age
        moreThan = age
    elif age < lessThan:
        lessThan = age
    elif age > moreThan:
        moreThan = age
print(a)
print("The youngest age is: %d years old!" %lessThan)
print("The oldest age is: %d years old!" %moreThan)            