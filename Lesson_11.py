# Lesson 10
# Нужно создать для каждого пользователя csv файл. Имя файла это username пользователя. В файл добавить задачи
# пользователя со следующими столбцами: id, title, completed

# https://jsonplaceholder.typicode.com/todos
# https://jsonplaceholder.typicode.com/users

import requests

response_todos = requests.get('https://jsonplaceholder.typicode.com/todos')
response_users = requests.get('https://jsonplaceholder.typicode.com/users')

import csv

col_names = ["id", "title", "completed"]

tasks_for_users = {}
for task in response_todos.json():
    task_user_id = task["userId"]
    if not (task_user_id in tasks_for_users):
        tasks_for_users[task_user_id] = []
    tasks_for_users[task_user_id].append(task)

for user in response_users.json():
    list_for_csv = []
    for task in tasks_for_users[user["id"]]:
        list_for_csv.append({"id": task["id"], "title": task["title"], "completed": task["completed"]})

    with open(user['username'] + '.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, col_names)
        dict_writer.writeheader()
        dict_writer.writerows(list_for_csv)
