#Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# “Tinha dívidas com a vítima?"
# "Já trabalhou com a vítima?“
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita“; entre 3 e 4 como "Cúmplice" e; 5 como "Assassino".
#Caso contrário, ele será classificado como "Inocente".
answers = []
yes = 0
q1 = input("Telefonou para a vítima?")
q2 = input("Esteve no local do crime?")
q3 = input("Mora perto da vítima?")
q4 = input("Tinha dívidas com a vítima?")
q5 = input("Já trabalhou com a vítima?")
answers.append(q1)
answers.append(q2)
answers.append(q3)
answers.append(q4)
answers.append(q5)
for a in answers:
    if a == 'sim':
        yes += 1
if yes == 2:
    print("Suspeita!")
elif yes == 3 or yes == 4:
    print("Cúmplice!")
elif yes == 5:
    print("Assassino!")
else: 
    print("Innocent!")