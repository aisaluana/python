#Inicialize uma lista de 20 números inteiros. Armazene os números pares em uma lista PAR e os números ímpares em uma lista IMPAR. Imprima as listas PAR e IMPAR.
even = []
uneven = []
for x in range(20):
    num = int(input("Digite: "))
    if num % 2 == 0:
        even.append(num)
    else:
        uneven.append(num)
print("The even numbers are: " , even)
print("The uneven numbers are: " , uneven)