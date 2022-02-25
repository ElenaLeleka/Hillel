# 1. В текстовый файл построчно записаны имя и фамилия учащихся класса и их оценки.
#     ```
#     Андрей Говорухи               6  6  1  4  9  9  10 4  8  2  3  8
#     Василий Петров                2  9  4  7  6  6  3  6  5  5  2  4
#     Гавриил Варфаломеев           10 10 4  10 7  9  4  6  8  1  1  1
#     Игнат Тюльпанов               8  1  4  1  1  5  2  5  2  2  10 8
#     Илья Муромцев                 1  6  4  7  10 9  5  3  7  4  7  2
#     Кощей Бессмертный             3  10 1  4  1  8  10 6  2  10 7  4
#     Максим Мухин                  10 8  9  9  5  8  6  5  7  2  4  10
#     Маргарита Мартынова           9  1  5  1  10 10 2  4  4  9  8  10
#     Петр Николаев                 2  9  5  9  1  2  8  7  8  1  9  1
#     Полина Гусева                 9  2  8  7  3  9  9  5  1  9  2  6
#     Спиридов Тереньтьев           4  7  7  3  10 9  7  2  10 9  8  1
#     Станислав Трердолобов         8  1  6  1  4  1  10 8  8  1  8  8
#     ```
#     Вывести на экран всех учащихся, чей средний балл меньше 5, также посчитать и вывести средний балл по классу. Так же,
#     записать в новый файл всех учащихся в формате "Фамилия И.       Ср. балл":
#
#     ```
#     Говорухи А.         5.83
#     Петров В.           4.92
#     Варфаломеев Г.      5.92
#     Тюльпанов И.        4.08
#     Муромцев И.         5.42
#     Бессмертный К.      5.5
#     Мухин М.            6.92
#     Мартынова М.        6.08
#     Николаев П.         5.17
#     Гусева Г.           5.83
#     Тереньтьев С.       6.42
#     Трердолобов С.      5.33
#     ```
#
#     Выравнивание колонок - желательно!
#

in_file = open("Lesson_9.txt", 'rt', encoding="utf-8")
average_mark_list = []
names_list = []
total_class_marks = 0
student_count = 0
mark_count = 0

for line in in_file:
    curr_line_parsed = line.split()
    names_list.append(f"{curr_line_parsed[1]} {curr_line_parsed[0][:1]}.")
    total_marks = 0
    for curr_mark in curr_line_parsed[2:]:
        total_marks += int(curr_mark)

    total_class_marks += total_marks
    student_count += 1

    mark_count = len(curr_line_parsed[2:])
    avg_mark = float(total_marks) / float(mark_count)
    average_mark_list.append(avg_mark)

    if avg_mark < 5:
        print(f"{curr_line_parsed[1]} {curr_line_parsed[0]} средний балл ученика: {avg_mark:.2f}")

class_avg_mark = float(total_class_marks) / float(student_count * mark_count)
print(f"Средняя оценка по классу:{class_avg_mark:.2f}")

out_file = open("Lesson_9_out.txt", "wt", encoding="utf-8")
curr_mark_index = 0
for student in names_list:
    print(student)
    out_file.write(f"{student: <30} {average_mark_list[curr_mark_index]:.2f}\n")
    curr_mark_index += 1
out_file.close()

# 2. Создать текстовый файл, записать в него построчно данные, которые вводит пользователь. Окончанием ввода пусть служит
# пустая строка. Каждая введённая строка, в файле, должна начинаться с новой строки.

print('Please enter text and end each line with "Enter". Empty line will finish the session. All lines will be written to IO_test.txt')

out_file = open("IO_test.txt", "at", encoding="utf-8")

out_file.write(f"\n")
while True:
    curr_line = input(">>>")
    if len(curr_line)>0:
        out_file.write(f"{curr_line}\n")
        out_file.flush()
    else:
        break

print('Session is finished.')
