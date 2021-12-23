# Дан массив целых чисел длины N. Нужно найти в нем заданное число x и 
# вернуть его индекс. Если x в массиве не встречается - вернуть -1. 

# Решить задачу применяя алгоритм бинарного поиска

def sort(n): 
    for y in range(len(n)):
        for i in range(len(n)-y-1):
            if n[i] > n[i+1]:
                n[i], n[i+1] = n[i+1], n[i]
    return n 

def binary_search(numbers, x):
    sor = sort(numbers)    
    l = len(sor)-1     
    mid = len(sor) //2     
    zero = 0             
    print('Отсортированный список: ', sor)
    while sor[mid] != x and zero <= l:  
        if x > sor[mid]:
            zero = mid +1
        else:
            l = mid -1
        mid = (zero + l) // 2
    if zero > l:
        return -1
    else:
        return mid

list_num = list(map(int, input('Задайте список: ').split())) 
x = int(input('Введите число, индекс которого нужно найти: ')) 
с = binary_search(list_num, x)

if с == -1:
    print('Всё работает, такого числа нет', с)
elif с != -1:
    print('Всё работает, такое число есть. Число', x ,'под индексом', с)
else:
    print('Ничего не работает, ошибка!!!')