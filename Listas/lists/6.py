#Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Em seguida, calcule a média anual das temperaturas e mostre a média calculada juntamente com todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
order = []
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
monNum = 0
highAvrg = []
highAvrgNum = []
for x in range(12):
    temp = float(input("Digite: "))
    order.append(temp)
    summ = sum(order)
    avrg = summ / 12
    monNum += 1
    if temp > avrg:
        highAvrg.append(temp)
        highAvrgNum.append(months[monNum])
print("In the months" , highAvrgNum , " the temperatures were, respectively " , highAvrg , ", higher than the average: ", avrg , ".")

    
