import numpy as np


def create_list(min, max, size):
    random_list = np.random.randint(min, max, size)
    return random_list


def print_result(message, item_to_print):
    print(message, end=' -> ')
    print(item_to_print)


list_for_search = np.random.randint(20, size=30)
print_result('Исходный список элементов', list_for_search)
uniq_list = np.unique(list_for_search)
print_result('Список уникальных элементов', uniq_list)
uniq_count = uniq_list.size
print_result('Количество уникальных элементов', uniq_count)
