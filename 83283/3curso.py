my_list = [3,15, 13,2,3]
largest = my_list[0]

for i in range(len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]

print(largest)
