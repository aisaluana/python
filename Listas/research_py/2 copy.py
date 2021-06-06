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

first = 0
last = len(list) - 1
medium_point = int(last/2)
print(first)
print(last)
print(medium_point)

while True:
    if search == list[medium_point]:
        print("Your element was found at position: ", (int(medium_point + 1)))
        break
    else:
        if search < list[medium_point]:
            last = medium_point - 1
            medium_point = int(last/2)
        else:
            first = medium_point + 1
            medium_point = int((first + last)/2)

print("%s" %(time.time()-start_time))
