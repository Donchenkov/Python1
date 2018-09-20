import os
import shutil


# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

def make_new_dir(name):
    os.mkdir(name)


def del_dir(name):
    os.rmdir(name)


for i in range(1, 10):
    try:
        make_new_dir('dir_' + str(i))
    except FileExistsError:
        print('директория уже существует')

for i in range(1, 10):
    del_dir('dir_' + str(i))


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def show_this_dir_files():
    files = os.listdir()
    dir_only = []
    for f in files:
        if os.path.isdir(f):
            dir_only.append(f)

    print(dir_only)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
def duplicate_file(file_to_dupl):
    if os.path.isfile(file_to_dupl):
        newfile = file_to_dupl + '.dupl'
        shutil.copy(file_to_dupl, newfile)
        if os.path.exists(newfile):
            print("Файл ", newfile, " был успешно создан")
        else:
            print("Возникли проблемы при копировании")


this_file_name = os.path.basename(__file__)
duplicate_file(this_file_name)
