#Задания:
# 1) У вас есть список my_list с значениями типа int.
# Распечатать те значения, которые больше 100.
# Задание выполнить с помощью цикла for.

my_list = [1,200,5,103,7,9]
for i in my_list:
    if i >100:
        print(i)
#
# 2) У вас есть список my_list с значениями типа int, и пустой список my_results.
# Добавить в my_results те значения, которые больше 100.
# Распечатать список my_results.
# Задание выполнить с помощью цикла for.

my_list = [1,200,5,103,7,9]
my_results = []
for i in my_list:
    if i >100:
        my_results.append(i)

for i in my_results:
    print(i)
#
# 3) У вас есть список my_list с значениями типа int.
# Если в my_list количество элементов меньше 2, то в конец добавить значение 0.
# Если количество элементов больше или равно 2, то добавить сумму последних двух элементов.
# Количество элементов в списке можно получить с помощью функции len(my_list)

my_list = [1,200,5,103,7,9]
if len(my_list)<2:
    my_list.append(0)

if len(my_list)>=2:
    my_list.append(my_list[-1]+my_list[-2])

print(my_list)
#
#
# #####################################################
# Еще один пример - вложенные циклы (цикл в цикле).
# my_string_1 = "12"
# my_string_2 = "34"
# for symb_1 in my_string_1:
# 	for symb_2 in my_string_2:
# 		print(symb_1 + symb_2)
#
#
#
# Результат:
# "13"	# перебирается все элементы из my_string_2 для элемента "1" из my_string_1
# "14"
# "23"	# перебирается все элементы из my_string_2 для элемента "2" из my_string_1
# "24"
# #####################################################
#
# 4) У вас есть строка my_string = '0123456789'.
# Сгенерировать целые числа (тип int) от 0 до 99 и поместить их в список.
# Задание нужно выполнить ТОЛЬКО через цикл в цикле(См. пример выше) и приведение типов.
# Генерирование через range или другие "фишки" я засчитывать не буду ))

my_string = '0123456789'
my_results=[]
for d2 in my_string:
    digit2=int(d2)
    for d1 in my_string:
        digit1=int(d1)
        my_results.append(digit2*10+digit1)
print(my_results)


