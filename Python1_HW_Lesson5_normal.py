# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import os
import Python1_HW_Lesson5_easy as some_place


print('Утилита по работе с папками')

answer = ''

while answer != 'q':
    answer = input('Желаете продолжить? (Y/N/q)')
    if answer == 'Y':
        print('Вам доступны следующие действия:')
        print('[1] Перейти в папку')
        print('[2] Просмотреть содержимое текущей папки')
        print('[3] Удалить папку')
        print('[4] Создать папку')

        what_to_do = int(input('Укажите номер действия:'))

        if what_to_do == 1:
            print('В какую папку текущей директории желаете перейти?')
            dir_to_go = input('Имя папки:')
            full_name_to_go = os.path.join(f'{os.getcwd()}/{dir_to_go}')
            os.chdir(full_name_to_go)
            print(f'Текущая директория: {os.getcwd()}')

        elif what_to_do == 2:
            some_place.show_this_dir_files()

        elif what_to_do == 3:
            dir_to_del = input('Какую папку желаете удалить?')
            try:
                some_place.del_dir(dir_to_del)
                print(f'Папка {dir_to_del} успешно удалена!')
            except FileNotFoundError:
                print('Ошибка!: Вы ввели имя файла или несуществующей папки')

        elif what_to_do == 4:
            dir_to_create = input('Введите имя новой папки:')
            try:
                some_place.make_new_dir(dir_to_create)
                print(f'Папка {dir_to_create} успешно создана!')
            except FileExistsError:
                print('Такая папка уже существует!')

        else:
            print('Вы ввели некорректный символ')
    elif answer == 'N':
        print('До свидания!')
    else:
        print('Неизвестная команда. Введите Y / N / q')
