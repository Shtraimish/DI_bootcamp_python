# list1 = [5, 10, 15, 20, 25, 50, 20]
# list1[list1.index(20)]=200
# print(list1)

# a_tuple = (10, 20, 30, 40)
# print(a_tuple[0])
# print(a_tuple[1])
# print(a_tuple[2])
# print(a_tuple[3])


current = 0
while current <= 10:
    
    current += 1
    if 3 < current < 7:
        continue
    print(current)
    