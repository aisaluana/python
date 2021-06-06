allAnswers = []
quantity = 0
w = 0
u = 0
l = 0
n = 0
m = 0
o = 0
while True:
    answer = int(input("Qual o melhor Sistema Operacional para uso em servidores? Digite o número correspondente à sua resposta. (1 - Windows XP; 2 - Unix; 3 - Linux; 4 - Netware; 5 - Mac OS; 6 - Outro) - MENSAGEM AO ADM: CASO TODOS OS PARTICIPANTES TENHAM RESPONDIDO, DIGITE 0 E O PROGRAMA SERÁ ENCERRADO."))
    if answer == 0:
        break
    else:
        allAnswers.append(answer)
        quantity += 1
for a in allAnswers:
    if a == 1:
        w += 1
    elif a == 2:
        u += 1
    elif a == 3:
        l += 1
    elif a == 4:
        n += 1
    elif a == 5:
        m += 1
    elif a == 6:
        o += 1
print("Sistemas Operacionais - Votos %")
print(" - Windowns XP", w, (w/quantity)*100 "%")
print(" - Unix", u, (u/quantity)*100 "%")
print(" - Linux", l, (l/quantity)*100 "%")
print(" - Netware", n, (n/quantity)*100 "%")
print(" - Mac OS", m, (m/quantity)*100 "%")
print(quantity)
print("O Sistema Operacional mais votado foi o")