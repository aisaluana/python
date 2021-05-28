#Ler uma lista de 5 números inteiros e mostre cada número juntamente com a sua posição na lista.
a  = [1,2,3,4,5]
for i,p in enumerate(a):
    print(i + 1, '=>', p)