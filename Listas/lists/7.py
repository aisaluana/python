#Faça um programa que crie uma matriz aleatoriamente. O tamanho da matriz deve ser informado pelo usuário.
matriz = []
rang = int(input("Digite o tamanho e dígito que você quer que a matriz tenha: "))
for i in range(rang):
    matriz.append([rang]*3)

print(matriz)