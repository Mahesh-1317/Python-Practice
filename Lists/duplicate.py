list = [1,5,4,2,1,6,4]
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i] == list[j]:
            print(list[i])

# numbers = [1, 5, 4, 2, 1, 6, 4]
# printed = []
# for num in numbers:
#     if numbers.count(num) > 1 and num not in printed:
#         print(num)
#         printed.append(num)