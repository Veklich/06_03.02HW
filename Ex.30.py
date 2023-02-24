# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для получения
# n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def ex30(a, d, n):
    my_array = list()
    for i in range(n):
        my_array.append(a + i * d)
    return my_array


result = ex30(7, 2, 5)
print(*ex30(int(input('Vvedite perviy el-t massiva: ')), int(input('Vvedite raznost: ')),
      int(input('Vvedite kol-vo el-v v massive: '))), sep='\n')
