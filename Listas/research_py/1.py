x = []

while True:
    n = int(input("Type in a number: "))
    if n == -999:
        break
    else:
        x.append(n)


search = int(input("Type in the number you want to find: "))
acum = 0

for i, j in enumerate(x):
    acum += 1
    if j == search:
        print("Your number was found at position: ", (i + 1))
        break
    else:
        if j == x[-1]:
            print("Your number was not found.")
        else:
            continue