# Дан массив целых чисел длины N. Нужно найти в нем заданное число x и 
# вернуть его индекс. Если x в массиве не встречается - вернуть -1. 

# Решить задачу применяя алгоритм бинарного поиска

def linear_search(array, number):
    for i in range(0, len(array) - 1):
        if array[i] == number:
            return i


print(linear_search([1, 2, 3, 6, 7, 8, 9, 0, 10], 3))