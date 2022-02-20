# 1) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена самых молодых.
#

dict_list=[{"name": "Jack", "age": 45}, {"name": "John", "age": 15}  ,{"name": "Mary", "age": 17} ,{"name": "Sarah", "age": 35}, {"name": "Jo", "age": 15}]
youngest_persons=[]
for person in dict_list:
    if len(youngest_persons)==0:
        youngest_persons.append(person)
    else:
        if youngest_persons[0]['age']==person['age']:
            youngest_persons.append(person)
        else:
            if youngest_persons[0]['age']>person['age']:
                youngest_persons.clear()
                youngest_persons.append(person)
for person in youngest_persons:
    print(person['name'])

#б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.

dict_list=[{"name": "Jack", "age": 45}, {"name": "John", "age": 15}  ,{"name": "Mary", "age": 17} ,{"name": "Sarah", "age": 35}, {"name": "Jo", "age": 15}, {"name": "Elena", "age": 15}]
longest_name_persons=[]
for person in dict_list:
    if len(longest_name_persons)==0:
        longest_name_persons.append(person)
    else:
        if len(longest_name_persons[0]['name'])==len(person['name']):
            longest_name_persons.append(person)
        else:
            if len(longest_name_persons[0]['name'])<len(person['name']):
                longest_name_persons.clear()
                longest_name_persons.append(person)
for person in longest_name_persons:
    print(person['name'])

# в) Посчитать среднее количество лет всех людей из списка.

dict_list=[{"name": "Jack", "age": 45}, {"name": "John", "age": 15}  ,{"name": "Mary", "age": 17} ,{"name": "Sarah", "age": 35}, {"name": "Jo", "age": 15}, {"name": "Elena", "age": 15}]
age_sum=0
for person in dict_list:
    age_sum+=person['age']

print(age_sum/len(dict_list))

#
# 2. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.
#

line_1='olena'
line_2='helena'
def same_letters(str1,str2):
    shortest_str=str1
    other_str=str2
    if len(str2)<len(str1):
        shortest_str=str2
        other_str=str1
    result_list=[]
    for symbol in shortest_str:
        if other_str.find(symbol)!=-1:
            result_list.append(symbol)
    return result_list
print(same_letters(line_1,line_2))



# 3. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.

line_1='olena'
line_2='helena'
def same_letters_no_repeat(str1,str2):
    shortest_str=str1
    other_str=str2
    if len(str2)<len(str1):
        shortest_str=str2
        other_str=str1
    result_list=[]
    for symbol in shortest_str:
        if other_str.find(symbol)!=-1:
            if (len(shortest_str.split(symbol))<=2) and (len(other_str.split(symbol))<=2):
                result_list.append(symbol)
    return result_list
print(same_letters_no_repeat(line_1,line_2))


#
# 4. Даны списки names и domains (создать самостоятельно).
# Написать функцию для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
# Строку и число генерировать случайным образом.

#
# Пример использования функции:
# names = ["king", "miller", "kean"]
# domains = ["net", "com", "ua"]
# e_mail = create_email(domains, names)
# print(e_mail)
# >>>miller.249@sgdyyur.com

import random
names = ["smith", "berg", "black"]
domains = ["za", "pl", "us"]
def create_email(names_list,domains_list):
    rand_number=random.randint(100,999)
    rand_domain_char_number=random.randint(5,7)
    rand_str=''
    for i in range(rand_domain_char_number):
        rand_str+=chr(random.randint(97,122))
    return f"{names_list[random.randint(0,len(names_list)-1)]}.{str(rand_number)}@{rand_str}.{domains_list[random.randint(0,len(domains_list)-1)]}"
print(create_email(names,domains))
