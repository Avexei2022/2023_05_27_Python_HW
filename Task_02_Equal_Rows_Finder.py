import numpy as np


def print_result(message, item_to_print):
    print(f'\n{message}:')
    print(f'{item_to_print}\n')


def get_result(array_2d, uniq_rows):
    if array_2d.size != uniq_rows.size:
        return 'Да'
    else:
        return "Нет"


array_2d = np.random.randint(2, size=(5, 5))
print_result('Исходный двумерный массив', array_2d)
uniq_rows = np.unique(array_2d, axis=0)
result_msg = get_result(array_2d, uniq_rows)
print_result('Наличие одинаковых строк', result_msg)
