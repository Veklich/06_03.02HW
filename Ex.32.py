# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

def new_array(l):
    new_array = list()
    for i in range(l):
        new_array.append(int(input('Vvodite znaheniya massiva: ')))
    return new_array


def ex_32 (my_array, a, b,):
    my_list = list()
    for i in range(len(my_array)):
        if my_array[i] >= a and my_array[i] <= b:
            my_list.append(i)
    return my_list

ex_array = new_array(int(input('Vvedite kol-vo el-v v massive: ')))

print(ex_32(ex_array, int(input('Vvedite minimum: ')), int(input('Vvedite maximum: '))))