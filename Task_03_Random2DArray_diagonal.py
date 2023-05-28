import numpy as np


def print_result(message, item_to_print):
    print(f'{message}:')
    print(f'{item_to_print}\n')


def create_random_matrix():
    # size_x = size_y = np.random.randint(4, 10)
    size_matrix = tuple(np.random.randint(4, 10, 2))
    return np.random.randint(10, size=size_matrix)


def get_list_index(array, value):
    tuple_index = np.where(array == value)
    return list(zip(tuple_index[0], tuple_index[1]))


array_2d = create_random_matrix()
print_result('Исходный двумерный массив', array_2d)

min_value = np.min(array_2d)
list_min_value = get_list_index(array_2d, min_value)
print_result('Значение минимального элемента', min_value)
print_result('Индексы минимальных элементов', list_min_value)

max_value = np.max(array_2d)
list_max_value = get_list_index(array_2d, max_value)
print_result('Значение максимального элемента', max_value)
print_result('Индексы максимальных элементов', list_max_value)

diagonal_value = np.diagonal(array_2d)
print_result('Главная диагональ массива', diagonal_value)
