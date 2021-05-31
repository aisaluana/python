#Faça um programa que crie uma matriz m (com valores informados do usuário) e mostra a matriz com o dobro dos valores lidos:
m =[]
sizeI = int(input("Digite quantas linhas sua matriz vai ter: "))
sizeJ = int(input("Digite quantas colunas sua matriz vai ter: "))
for i in range(sizeI):
    m.append([0]*sizeJ)
    for j in range(sizeJ):
        request = int(input("Digite um valor para sua matriz: "))
        m[i][j] = request*2
print(m)