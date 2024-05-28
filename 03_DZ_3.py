my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
print(my_list)
while index < len(my_list):
    index += 1
    if my_list[index - 1] == 0:
        continue
    elif my_list[index - 1] < 0:
        break
    else:
        print(my_list[index - 1])









##print(len(my_list)) # 12
#print(index)
# Чтобы не выйти за границу списка,
# в условии цикла while рекомедуется сравнивать текущий индекс и длину списка (функция len()).
#
#
# # кол-во чисел в списке
# index = 0                                 # я думала, index = my_list[4]
#









