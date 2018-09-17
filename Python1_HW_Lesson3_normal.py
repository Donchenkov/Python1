__autor__ = 'Mikhail Donchenkov'

# Задание - 1
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000
# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
# Есть условие, не отображать людей получающих более зарплату 500000, как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.
# Так же при выводе имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.

names = ['Ivan', 'Pablo', 'Suzanna', 'Stone', 'Mike', 'Dunkan']
salaries = [5000, 3000, 4500, 1200, 600000, 425555]

result = dict(zip(names, salaries))
with open('salary.txt', 'w') as file:
    for names, salaries in result.items():
        what_export = (f'{names} - {salaries}')
        file.write(what_export + '\n')

with open('salary.txt') as file:
    for line in file:
        split_for_tax = line.strip().split()
        tax_free = float(split_for_tax[2]) * 0.87
        if tax_free < 500000:
            print(f'{split_for_tax[0].upper()} {split_for_tax[1]} {tax_free}')