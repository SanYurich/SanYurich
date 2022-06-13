# 1 -  Написать программу вычисления арифметического выражения заданного строкой. Используются операции +,-,/,*. приоритет операций стандартный. Функцию eval не использовать!
# Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
# Дополнительно: Добавить возможность использования скобок, меняющих приоритет операций. 
# Пример: 1+2*3 => 7; (1+2)*3 => 9;

# from functools import reduce
# import re

# prioritet = [1,2,3,4]
# operator = ['*','/','+','-']
# formula = '100-21*3+55/5'

# def calculator(formula):
#     for i in range(len(prioritet)):
#         if prioritet[i] == 1:
#             proiz_list = re.findall(r'(\d+)[*](\d+)', formula)
#             v_str_prz = (reduce( 0, proiz_list))
#             rez_prz = int(v_str_prz[0]) * int(v_str_prz[1])
#             spis_prz = re.sub(r'(\d+[*]\d+)', str(rez_prz) , formula)

#         if prioritet[i] == 2:
#             split_list = re.findall(r'(\d+)[/](\d+)', spis_prz)
#             v_str_spl = (reduce( 0, split_list))
#             rez_spl = int(v_str_spl[0]) / int(v_str_spl[1])
#             spis_spl = re.sub(r'(\d+[/]\d+)', str(rez_spl) , spis_prz)

#         if prioritet[i] == 3:
#             sum_list = re.findall(r'(\d+)[+](\d+)', spis_spl)
#             v_str_sum = (reduce( 0, sum_list))
#             rez_sum = int(v_str_sum[0]) + int(v_str_sum[1])
#             spis_sum = re.sub(r'(\d+[+]\d+)', str(rez_sum) , spis_spl)

#         if prioritet[i] == 4:
#             neg_list = re.findall(r'(\d+)[-](\d+)', spis_sum)
#             v_str_neg = (reduce( 0, neg_list))
#             rez_neg = int(v_str_neg[0]) - int(v_str_neg[1])
#             spis_neg = re.sub(r'(\d+[-]\d+)', str(rez_neg) , spis_sum)
#     return spis_neg

# print(calculator(formula))


# 2 - Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных файлах 
# (в одном файлике отрывок из какой-то книги, а втором файлике — сжатая версия этого текста). 

# with open('text_file.txt', 'w') as rec_tf:
#     rec_tf.write('We do not remember days, we remember moments.')

# def compressed(original,compress):
#     with open(original, 'r') as read_orig:
#         for i in read_orig:
#             spisok = ''.join(str(i))
#     comp_spisok = ''
#     i = 0
#     while (i <= len(spisok) - 1):
#         count = 1
#         ch = spisok[i]
#         j = i
#         while (j < len(spisok) - 1):
#             if spisok[j] == spisok[j + 1]:
#                 count +=1
#                 j +=1
#             else:
#                 break
#         comp_spisok += str(count) + ch
#         i = j + 1
#     with open(compress, 'w') as cf:
#         cf.write(comp_spisok)

# compressed('text_file.txt', 'cprs_file.txt')

# def decryption(compress, original):
#     with open(compress, 'r') as cprs:
#         for i in cprs:
#             spisok = ''.join(str(i))
#     dcrypt = ''
#     i = 0
#     j = 0
#     while (i <= len(spisok) - 1):
#         count = int(spisok[i])
#         word = spisok[i + 1]
#         for j in range(count):
#             dcrypt += word
#             j +=1
#         i += 2
#     with open(original, 'a') as rdf:
#         rdf.writelines('\n' + dcrypt + ' - decryption')

# decryption('cprs_file.txt', 'text_file.txt')

# 3 -  ROT13 - это простой шифр подстановки букв, который заменяет букву буквой, которая идет через 13 букв после нее в алфавите. ROT13 является примером шифра Цезаря.
# Создайте функцию, которая принимает строку и возвращает строку, зашифрованную с помощью Rot13 . Если в строку включены числа или специальные символы, они должны быть возвращены как есть. 
# Также создайте функцию, которая расшифровывает эту строку обратно (некий начальный аналог шифрования сообщений). 
# Не использовать функцию encode.

# def encryption (text, key):
#     alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
#     rezult = ''
#     for i in text.upper():
#         if i in alphabet:
#             rezult += alphabet[(alphabet.find(i) + key) % len(alphabet)]
#         else:
#             rezult += i
#     return rezult 

# def enc_Rot13(text):
#     return encryption(text,13)

# def dec_Rot13(text):
#     return encryption(text,-13)

# print(enc_Rot13('Прости Прощай'))
# print(dec_Rot13(enc_Rot13('Прости Прощай')))


# Экстра-задачи:
# 1.Рассмотрим все целочисленные комбинации ab для 2 ≤ a ≤ 5 и 2 ≤ b ≤ 5:
# 22=4, 23=8, 24=16, 25=32
# 32=9, 33=27, 34=81, 35=243
# 42=16, 43=64, 44=256, 45=1024
# 52=25, 53=125, 54=625, 55=3125
# Если их расположить в порядке возрастания, исключив повторения, мы получим следующую последовательность из 15 различных членов:
# 4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125
# Сколько различных членов имеет последовательность ab для 2 ≤ a ≤ 100 и 2 ≤ b ≤ 100?

# 2. Число 197 называется круговым простым числом, потому что все перестановки его цифр с конца в начало являются простыми числами: 197, 719 и 971.
# Существует тринадцать таких простых чисел меньше 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79 и 97.
# Сколько существует круговых простых чисел меньше миллиона?

# 3. Пятиугольные числа вычисляются по формуле: Pn=n(3n−1)/2. Первые десять пятиугольных чисел:
# 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
# Можно убедиться в том, что P4 + P7 = 22 + 70 = 92 = P8. Однако, их разность, 70 − 22 = 48, не является пятиугольным числом.
# Найдите пару пятиугольных чисел Pj и Pk, для которых сумма и разность являются пятиугольными числами и значение D = |Pk − Pj| минимально, и дайте значение D в качестве ответа.