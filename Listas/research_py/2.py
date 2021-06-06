import time
start_time = time.time()

# list = []

# while True:
#     num = int(input("Type in a number: "))
#     if num == -999:
#         break
#     else:
#         list.append(num)

list = [1,2,3,4,5,6,7,8,9,10]
list.sort()
print(list)
search = 1


#search = int(input("Type in the element you want to find: "))

last = len(list)-1
mediumPoint = int(last/2)

while True:
    if search == list[mediumPoint]:
        print("Your element was found at position: ", (mediumPoint + 1))
        break
    else:
        if search < list[mediumPoint]:
            list = list[0:mediumPoint]
            last = mediumPoint - 1
            mediumPoint = int(last/2)
        else:
            list = list[(mediumPoint+1):(last+1)]
            last = len(list)-1
            mediumPoint = int(last/2)

print("%s" %(time.time()-start_time))