# 1. Дано целое число (int). Определить сколько нулей в этом числе.

number = 13560560890000056700034
number_str = str(number)
number_zero = number_str.count('0')
print(number_zero)

# 2. Дано целое число (int). Определить сколько нулей в конце этого числа. Например для числа 1002000 - три нуля

number = 1002000
number_str = str(number)
number_zero_end=0
for digit in number_str[::-1]:
    if digit == '0':
        number_zero_end=number_zero_end+1
    else: break
print(number_zero_end)

#
# 3. Даны списки my_list_1 и my_list_2.
# Создать список my_result в который вначале поместить
# элементы на четных местах из my_list_1, а потом все элементы на нечетных местах из my_list_2.

my_list_1=['a','b','c','d','e']
my_list_2=[1,2,3,4,5]
my_result=[]
for index in range(len(my_list_1)):
    my_result.append(my_list_1[index])
    my_result.append(my_list_2[index])
print(my_result)


#
# 4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
# стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1]

my_list = [1,2,3,4]
new_list = my_list[1:]+my_list[:1]
print(new_list)

#
# 5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
# [1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)

my_list = [1,2,3,4]
my_list.append(my_list.pop(0))
print(my_list)
#
# 6. Дана строка в которой есть числа (разделяются пробелами).
# Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
# Для данного примера ответ - 133. (используйте split и проверку isdigit)


test_string="43 больше чем 34 но меньше чем 56"
substr_list=test_string.split(' ')
print(substr_list)
total_sum=0
for item in substr_list:
    if item.isdigit():
        total_sum+=int(item)
print(total_sum)



#
# 7. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
# my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".

my_str = "My long string"
l_limit = "o"
r_limit = "g"
index_left=my_str.index(l_limit)
print(index_left)
index_right=my_str[::-1].index(r_limit)
index_right_corrected=len(my_str)-index_right
print(index_right)
sub_str=my_str[index_left+1:index_right_corrected-1]
print(sub_str)


#
# 8. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
# Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
# быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']
# (используйте срезы длинны 2)

my_str='abcde'
split_number=len(my_str)//2
result_list=[]
for split_index in range(split_number+1):
    current_piece=my_str[split_index*2:split_index*2+2]
    if len(current_piece)==1:
        current_piece+='_'
    result_list.append(current_piece)
print(result_list)


#
# 9. Дан список чисел. Определите, сколько в этом списке элементов,
# которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
# Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.

# my_list=[2,4,1,5,3,9,0,7]
# values_count=0
# for index in range(len(my_list)-2):
#     left_neighbour=my_list[index]
#     right_neighbour=my_list[index+2]
#     value=my_list[index+1]
#     if value>(left_neighbour+right_neighbour):
#         values_count+=1
# print(values_count)
